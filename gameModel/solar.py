'''
Created on 7 janv. 2012

@author: Bazibaz
'''
from observable import Observable
from pandac.PandaModules import CollisionNode, CollisionBox, CollisionSphere, TransparencyAttrib, TextureStage, Texture
from direct.showbase import DirectObject 
from panda3d.core import Vec3,Vec4,Point2, Point3, BitMask32
from direct.directtools.DirectGeometry import LineNodePath
from gameModel.constants import MAX_STAR_RADIUS, MAX_PLANET_RADIUS, PLANET_SPIN_VELOCITY
from gui.Timer import Timer
from panda3d.core import Filename,Buffer,Shader, CardMaker
from panda3d.core import PandaNode,NodePath
from panda3d.core import AmbientLight,DirectionalLight, PointLight
from direct.task import Task
#from gameEngine.gameEngine import *
from constants import MAX_NUMBER_OF_PLANETS, MAX_NUMBER_OF_STRUCTURE, LIFETIME, MAX_STAR_RADIUS, AI_ESCAPE_WAIT_TIME
import math

from graphicEngine import shapes


class SphericalBody(Observable):
    
    '''
    Abstract class defining a radius and a position
    '''
    star_dead_tex = None
    star_stage1_tex = None
    star_stage2_tex = None
    star_stage3_tex = None
    star_stage4_tex = None
    star_stage5_tex = None
    star_stage6_tex = None
    dead_planet_tex = None
    planet_activated_tex = None
    planet_forge_tex = None
    planet_nexus_tex = None
    planet_extractor_tex = None
    planet_phylon_tex = None
    planet_generatorCore_tex = None
    
    def __init__(self, position, radius, activated, player):
        '''
        Constructor
        @param position: Point3D, position in space
        @param radius: float, body radius
        @param activated: boolean, determine whether the spherical body is activated by the player or not
        @param player: the player who owns the solar object
        '''
        super(SphericalBody,self).__init__()
        self.radius = radius
        self.position = position
        self.activated = activated
        self.player = player
        
        #Pre_Loading the star textures
        SphericalBody.star_dead_tex = loader.loadTexture("models/stars/white_dwarf2.jpg")
        SphericalBody.star_stage1_tex = loader.loadTexture("models/stars/star_stage1_tex.png")
        SphericalBody.star_stage2_tex = loader.loadTexture("models/stars/star_stage2_tex.png")
        SphericalBody.star_stage3_tex = loader.loadTexture("models/stars/star_stage3_tex.png")
        SphericalBody.star_stage4_tex = loader.loadTexture("models/stars/star_stage4_tex.png")
        SphericalBody.star_stage5_tex = loader.loadTexture("models/stars/star_stage5_tex.png")
        SphericalBody.star_stage6_tex = loader.loadTexture("models/stars/star_stage6_tex.png")
        
        #Pre_Loading the planet textures
        SphericalBody.dead_planet_tex = loader.loadTexture("models/planets/dead_planet_tex.jpg")
        SphericalBody.planet_activated_tex = loader.loadTexture("models/planets/planet_activated_tex.png")
        SphericalBody.planet_forge_tex = loader.loadTexture("models/planets/planet_forge_tex.png")
        SphericalBody.planet_nexus_tex = loader.loadTexture("models/planets/planet_nexus_tex.png")
        SphericalBody.planet_extractor_tex = loader.loadTexture("models/planets/planet_extractor_tex.png")
        SphericalBody.planet_phylon_tex = loader.loadTexture("models/planets/planet_phylon_tex.png")
        SphericalBody.planet_generatorCore_tex = loader.loadTexture("models/planets/planet_generatorCore_tex.png")
        
    #def __str__(self) :
    #   '''To String method'''
    #  return str(self.__dict__)

    #def __eq__(self, other) : 
    #   '''Compare to object of SphericalBody class for equality'''
    #  return self.__dict__ == other.__dict__
    

    #def _getRadius(self):
        #return self._radius
    
    #def _setRadius(self, radius):
    #    self.select()
    
    #def _delRadius(self):
    #    del self._radius
    
    #radius = property(_getRadius, _setRadius, _delRadius, "Sphere radius")


class Star(SphericalBody):
    '''
    Class star contain attributes of the star and
    a list of all the planets orbiting the star.
    '''

    def __init__(self, position, radius, player=None):
        '''
        Constructor for class star: creates a dead star object, initializing the star's attributes with 
        the given parameters. 
        @param position : Point3D, the position of the center of the star
        @param radius : float, star radius
        @param player: Player, the owner of the star
        @param activated: boolean, determine whether star is activated by the player or not
        @param stage: Integer, is the stage in which the star is in; consists of 6 stages
        @param counter: Timer, is the count-down timer for the star's life
        '''
        super(Star, self).__init__(position, radius, False, player)
        self.lifetime = 0
        self._planets = []
        self.stage = 0
        self.timer_task = None
        
        self.t = Timer(self) 
        self.__initSceneGraph()
    
    def __initSceneGraph(self):
        # Parent node for relative position (no scaling)
        self.point_path = render.attachNewNode("star_node")
        self.point_path.setPos(self.position)
        
        #For transforming the object with scaling, colors, shading, etc.
        # Hosting the actual 3d model object.
        #Models & textures
        self.flare_ts = TextureStage('flare')
        self.flare_ts.setMode(TextureStage.MModulateGlow)
        self.model_path = loader.loadModel("models/stars/planet_sphere")
        self.model_path.setTexture(SphericalBody.star_dead_tex, 1)
        self.model_path.reparentTo(self.point_path)
        self.model_path.setScale(self.radius)
        self.model_path.setPythonTag('pyStar', self);
        
        # Collision sphere for object picking
        #-----------------------------------------------------
        # As described in the Tut-Chessboard.py sample: "If this model was
        # any more complex than a single polygon, you should set up a collision
        # sphere around it instead."
        cnode = CollisionNode("coll_sphere_node")
        cnode.setTag('star', str(id(self)))
        #We use no displacement (0,0,0) and no scaling factor (1)
        cnode.addSolid(CollisionSphere(0,0,0,1))
        cnode.setIntoCollideMask(BitMask32.bit(1))
        self.cnode_path = self.model_path.attachNewNode(cnode)
        #For temporary testing, display collision sphere.
#        self.cnode_path.show()
        self.quad_path = None
 
    def activateHighlight(self, thin):
        if thin:
            tex = base.loader.loadTexture("models/billboards/thin_ring.png")
        else:
            tex = base.loader.loadTexture("models/billboards/ring.png")
        cm = CardMaker('highlight')
        cm.setFrameFullscreenQuad() # so that the center acts as the origin (from -1 to 1)
        self.quad_path = self.point_path.attachNewNode(cm.generate())        
        self.quad_path.setTransparency(TransparencyAttrib.MAlpha)
        self.highlight_ts = TextureStage('flare')
        self.quad_path.setTexture(self.highlight_ts, tex)
        if thin:
            self.quad_path.setColor(Vec4(1.0, 1.0, 1.0, 1))
        else:
            self.quad_path.setColor(Vec4(1.0, 0.3, 0.2, 1))
        self.quad_path.setScale(12)
        self.quad_path.setPos(Vec3(0,0,0))
        self.quad_path.setBillboardPointEye()
    
    def deactivateHighlight(self):
        if self.quad_path:
            self.quad_path.detachNode()
            self.quad_path = None

    def select(self, player):
        '''
        @param player, the player who has selected
        This method observes the events on the star and calls the related methods
        and notifies the corresponding objects based on the state of the star
        '''
        player.selected_planet = None
        
        if(player.ge_amount != 0 and self.activated == False and \
           player.selected_star == self):
            player.ge_amount = player.ge_amount - 1
            self.activateStar(player)
            self.notify("updateGE")
        else:
            from gameEngine.gameEngine import all_stars 
            for star in all_stars:
                if(star != self):
                    star.deactivateHighlight()
            from gameEngine.gameEngine import all_planets
            for planet in all_planets:
                planet.deactivateHighlight()
            '''TODO: fix the conflict problem with highlight and star flare ''' 
            #self.activateHighlight(False)
            
        player.selected_star = self
        
    def activateStar(self, player):
        '''
        Activates a constructed dead star object, starting the lifetime counter with the assigned default value while
        the Game Engine calls the graphic engine to display the corresponding animation.
        @param player, the player who has activated the star
        '''
        self.lifetime = LIFETIME
        self.stage = 1
        self.activated = True
        self.radius = MAX_STAR_RADIUS
        self.player = player
        self.timer_task = taskMgr.doMethodLater(1, self.trackStarLife, 'starLifeTick')
        player.selected_star = self
        
#        point_light = PointLight("starLight")
#        point_light.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
#        pt_node = render.attachNewNode(point_light)
##        pt_node.setHpr(60, 0, 90)
#        pt_node.setPos(Vec3(0, 0, -40.0))
#        render.setLight(pt_node)
        
        point_light = PointLight("starLight")
        point_light.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        point_light.setPoint(Point3(0, 0, 0))
        pt_node = render.attachNewNode(point_light)
#        pt_node.setHpr(60, 0, 90)
        render.setLight(pt_node)
        
        '''TODO : display star birth animation '''
        sound1 = base.loader.loadSfx("sound/effects/star/starCreation1.wav")
        sound1.setLoop(False)
        sound1.setVolume(0.5)
        sound1.play()
        sound2 = base.loader.loadSfx("sound/effects/star/starCreation2.wav")
        sound2.setLoop(False)
        sound2.setVolume(0.45)
        sound2.play()
        
        self.radius = MAX_STAR_RADIUS
        self.model_path.setScale(self.radius)
        self.model_path.setTexture(self.flare_ts, SphericalBody.star_stage1_tex)
        self._activateSunflare()
    
    def _activateSunflare(self):
        self.deactivateHighlight()
        flare_tex = base.loader.loadTexture("models/billboards/sunflare.png")
        cm = CardMaker('flare')
        cm.setFrameFullscreenQuad() # so that the center acts as the origin (from -1 to 1)
        self.flare_path = self.point_path.attachNewNode(cm.generate())        
        self.flare_path.setTransparency(TransparencyAttrib.MAlpha)
        self.flare_path.setTexture(self.flare_ts,flare_tex)
        self.flare_path.setColor(Vec4(1.0, 1.0, 1.0, 1))
        self.flare_path.setScale(32)
        self.flare_path.setPos(Vec3(0,0,0))
        self.flare_path.setBillboardPointEye()
        
    def trackStarLife(self, task):
        self.lifetime = self.lifetime - float(self.getNumberOfActivePlanets())/(2)
        self.updateTimer()
        if(self.lifetime <= LIFETIME - LIFETIME/6 and self.stage == 1):
            self.stage = 2
            self.model_path.setTexture(self.flare_ts, SphericalBody.star_stage2_tex)
        elif(self.lifetime <= LIFETIME - LIFETIME/3 and self.stage == 2):
            self.stage = 3
            self.model_path.setTexture(self.flare_ts, SphericalBody.star_stage3_tex)
        elif(self.lifetime <= LIFETIME - LIFETIME/2 and self.stage == 3):
            self.stage = 4
            self.model_path.setTexture(self.flare_ts, SphericalBody.star_stage4_tex)
        elif(self.lifetime <= LIFETIME - 2*LIFETIME/3 and self.stage == 4):
            self.stage = 5
            self.model_path.setTexture(self.flare_ts, SphericalBody.star_stage5_tex)
        elif(self.lifetime <= 0 and self.stage == 5):
            self.lifetime = 0
            self.stage = 6
            self.model_path.setTexture(SphericalBody.star_stage6_tex, 1)
            timer_destruction= taskMgr.doMethodLater(1, self._consumeSolarSystem, 'consumeSolarSystem')
            '''calls the escape solar system routine from the AI class'''
            from gameEngine.gameEngine import ai
            task = taskMgr.doMethodLater(AI_ESCAPE_WAIT_TIME, ai.escapeStar, 'AIescapeStar', extraArgs =[self], appendTask=True)
            return task.done
        return task.again
    
    def _consumeSolarSystem(self, task):
        for planet in self.planets():
            ''' TODO: move it smoothly '''
            ''' TODO: make the unactivated planets move '''
            planet.orbital_radius = planet.orbital_radius - 1
            planet.max_orbital_velocity = planet.max_orbital_velocity + 0.0002
            planet.orbital_velocity = planet.orbital_velocity + 0.0002
            #taskMgr.add(planet.accelerateOrbit, 'accelerateOrbit', taskChain = 'orbitChain')
            if(planet.orbital_radius <= 0):
                self._consumePlanet(planet)
                if(planet.next_planet == None):
                    planet = None
                    return task.done
                planet = None
        return task.again
    
    def _consumePlanet(self, planet):
        ''' TODO : remove planet properly, destroy orbiting unit and surface structures'''
        self.removePlanet(planet)
        planet.orbital_radius = 0
        planet.max_orbital_velocity = 0
        planet.orbital_velocity = 0
        ''' TODO : delete planet model '''
        planet._consumeUnits()
        planet._consumeStructures()
        
    def updateTimer(self):
        self.notify("updateTime")
        
    def addPlanet(self, planet):
        '''
        Adds a planet to the star system
        @param: planet object
        '''
        if(len(self._planets) < MAX_NUMBER_OF_PLANETS):
            self._planets.append(planet)
        
    def removePlanet(self, planet):
        '''
        removes a planet from the star system
        @param planet object
        '''
        if len(self._planets) != 0:
            self._planets.remove(planet)
        
    def removeAllPlanets(self):
        '''
        removes all the planets in the star system
        '''
        del self._planets[:]
        
    def planets(self):
        '''
        Generator that iterates over the hosted planets.
        '''
        for planet in self._planets:
            yield planet
    
    def getPlanetAt(self, orbit):
        '''
        returns the planet object at the specified orbit number
        @param orbit, Integer : the orbit of the planet
        '''
        tmp = 0
        for planet in self.planets():
            if(orbit == tmp):
                return planet
            else:
                tmp = tmp + 1
        
    def getPlanet(self, planet):
        '''
        Returns the index of the given planet from list of planets 
        @param planet : the desired planet
        '''
        return self._planets.index(planet)
            
    def getNumberOfPlanets(self):
        '''
        Returns the number of dead planets currently around the star
        '''
        return len(self._planets)
    
    def getNumberOfActivePlanets(self):
        '''
        Returns the number of planets currently orbiting the star
        '''
        total = 0
        for planet in self.planets():
            if(planet.activated):
                total = total + 1
        return total
                 


class Planet(SphericalBody): 
    '''
    Planet contains units and structures
    '''

    def __init__(self, orbital_radius, orbital_angle, radius, parent_star, prev_planet=None, player=None):
        '''
        Constructor for class planet.
        @param position: Point3D, position in space
        @param radius: float, body radius
        @param player: Player, the owner of the planet
        @param parent_star: Star, the specific star the planet is orbiting around
        @param prev_planet: previous planet in the star system, if None then the planet is the first
        '''
        position = Point3(orbital_radius * math.cos(orbital_angle),
                          orbital_radius * math.sin(orbital_angle), 0)
        super(Planet, self).__init__(position, radius, False, player)
        self.orbital_velocity = 0
        self.max_orbital_velocity = 0
        self.orbital_radius = orbital_radius
        self.orbital_angle = orbital_angle
        self.parent_star = parent_star
        self.prev_planet = prev_planet
        self.next_planet = None
        self._orbiting_units = []
        self._surface_structures = []
        self.__initSceneGraph()
               
        '''For the Player'''
        self.task_structure_timer = None
        self.task_unit_timer = None
        '''For the AI'''
        self.task_structure_timers = []
        self.task_unit_timers = []
        
    def __initSceneGraph(self):

        #load various texture stages of the planet
        self.forge_tex = TextureStage('forge')
        self.forge_tex.setMode(TextureStage.MDecal)
        self.nexus_tex = TextureStage('nexus')
        self.nexus_tex.setMode(TextureStage.MDecal)
        self.extractor_phylon_ge_tex = TextureStage('extractor_phylon_ge')
        self.extractor_phylon_ge_tex.setMode(TextureStage.MDecal)
        
        # Parent node for relative position (no scaling)
        self.point_path = self.parent_star.point_path.attachNewNode("planet_node")
        self.point_path.setPos(self.position)
        
        #Models & textures
        self.model_path = loader.loadModel("models/planets/planet_sphere")
        self.model_path.setTexture(SphericalBody.dead_planet_tex, 1)
        self.model_path.reparentTo(self.point_path)
        self.model_path.setScale(self.radius)
        self.model_path.setPythonTag('pyPlanet', self);
        
        cnode = CollisionNode("coll_sphere_node")
        cnode.setTag('planet', str(id(self)))
        #We use no displacement (0,0,0) and no scaling factor (1)
        cnode.addSolid(CollisionSphere(0,0,0,1))
        cnode.setIntoCollideMask(BitMask32.bit(1))
        # Reparenting the collision sphere so that it 
        # matches the planet perfectly.
        self.cnode_path = self.model_path.attachNewNode(cnode)
        
        self.lines = LineNodePath(parent = self.parent_star.point_path, thickness = 4.0, colorVec = Vec4(1.0, 1.0, 1.0, 0.2))
        self.quad_path = None
        
    def setTexture(self, structureType):
        '''
        Used whenever a structure is built on the planet
        @ StructureType is a string specifying the type of the structure
        '''
        if(structureType == "forge"):
            #SphericalBody.planet_forge_tex.setWrapU(Texture.WMInvalid)
            #SphericalBody.planet_forge_tex.setWrapV(Texture.WMInvalid)
            self.model_path.setTexture(self.forge_tex, SphericalBody.planet_forge_tex)
            #self.model_path.getTexture().setWrapU(Texture.WMClamp)
            #self.model_path.getTexture().setWrapV(Texture.WMClamp)
            self.model_path.setTexOffset(self.forge_tex, 0, 0)
            #self.model_path.setTexScale(self.forge_tex, -4, -2)
        elif(structureType == "nexus"):
            self.model_path.setTexture(self.nexus_tex, SphericalBody.planet_nexus_tex)
            self.model_path.setTexOffset(self.nexus_tex, 0, 10)
        elif(structureType == "extractor"):
            self.model_path.setTexture(self.extractor_phylon_ge_tex, SphericalBody.planet_extractor_tex)
            self.model_path.setTexOffset(self.extractor_phylon_ge_tex, 0, 20)
        elif(structureType == "phylon"):
            self.model_path.setTexture(self.extractor_phylon_ge_tex, SphericalBody.planet_phylon_tex)
            self.model_path.setTexOffset(self.extractor_phylon_ge_tex, 0, 20)
        elif(structureType == "generatorCore"):
            self.model_path.setTexture(self.extractor_phylon_ge_tex, SphericalBody.planet_generatorCore_tex)
            self.model_path.setTexOffset(self.extractor_phylon_ge_tex, 0, 20)
    
    def activateHighlight(self, thin):
        if thin:
            flare_tex = base.loader.loadTexture("models/billboards/thin_ring.png")
        else:
            flare_tex = base.loader.loadTexture("models/billboards/ring.png")
        cm = CardMaker('quad')
        cm.setFrameFullscreenQuad() # so that the center acts as the origin (from -1 to 1)
        self.quad_path = self.point_path.attachNewNode(cm.generate())        
        self.quad_path.setTransparency(TransparencyAttrib.MAlpha)
        self.quad_path.setTexture(flare_tex)
        if thin:
            self.quad_path.setColor(Vec4(1,1,1, 1))
        else:
            self.quad_path.setColor(Vec4(0.2, 0.3, 1.0, 1))
        self.quad_path.setScale(5)
        self.quad_path.setPos(Vec3(0,0,0))
        self.quad_path.setBillboardPointEye()
    
    def deactivateHighlight(self):
        if self.quad_path:
            self.quad_path.detachNode()
            self.quad_path = None
    
    def select(self, player):
        '''
        This method observes the events on the planet and calls the related methods
        and notifies the corresponding objects based on the state of the planet
        @param player, the player who has selected
        '''
        player.selected_star = None

        if(self.player == player):
            '''TODO : notify the GUI Panel about the constructions available on this planet '''
        
        if(not self.activated and player.selected_planet == self):
            if((self.prev_planet == None or self.prev_planet.activated) and \
                    self.parent_star.activated and self.parent_star.player == player):
                self.activatePlanet(player)
        else:
            from gameEngine.gameEngine import all_stars 
            for star in all_stars:
                star.deactivateHighlight()
            from gameEngine.gameEngine import all_planets
            for planet in all_planets:
                if(self != planet or self.next_planet != planet or self.prev_planet != planet):
                    planet.deactivateHighlight()
            if self.next_planet != None: self.next_planet.activateHighlight(True) 
            if self.prev_planet != None: self.prev_planet.activateHighlight(True)
            self.activateHighlight(False)
        
        player.selected_planet = self
        
    def selectRight(self, player):
        '''
        This method observes the events on the planet and calls the related methods
        and notifies the corresponding objects based on the state of the planet
        @param player, the player who has selected with right mouse click
        '''
        if(player.selected_unit != None):
            '''movement is inside the solar system'''
            if(player.selected_unit.host_planet.parent_star == self.parent_star):
                if(player.selected_unit.host_planet == self.prev_planet):
                    player.selected_unit.moveUnitNext()
                if(player.selected_unit.host_planet == self.next_planet):
                    player.selected_unit.moveUnitPrev()      
            else:
                '''movement is between solar systems in deep space mode'''
                if(self.next_planet == None and player.selected_unit.host_planet.next_planet == None):
                    player.selected_unit.moveDeepSpace(self)
       
    def activatePlanet(self, player):
        '''
        Activates a constructed dead planet object, starting the orbital movement with the assigned value while
        the Game Engine calls the graphic engine to display the corresponding animation.
        @param player: Player, the player who controls the planet
        @precondition: MIN_PLANET_VELOCITY < orbital_velocity < MAX_PLANET_VELOCITY
        '''
        self.activated = True
        player.planets.append(self)
        self.player = player

        
        sound = base.loader.loadSfx("sound/effects/planet/planetCreation.wav")
        sound.setLoop(False)
        sound.setVolume(0.23)
        sound.play()
        
        self.radius = MAX_PLANET_RADIUS
        self.model_path.setScale(self.radius)
        
        '''TODO : display planet creation animation '''
        
        #rand = random.randrange(1,8,1)
        self.model_path.setTexture(SphericalBody.planet_activated_tex, 1)
        
        self.startSpin()
        taskMgr.setupTaskChain('orbitChain')
        taskMgr.add(self.accelerateOrbit, 'accelerateOrbit', taskChain = 'orbitChain')
        self.orbitTask = taskMgr.add(self.stepOrbit, 'stepOrbit', taskChain = 'orbitChain')
        
        self.orbit_path = shapes.makeArc(360, int(self.orbital_radius))
        self.orbit_path.reparentTo(self.parent_star.point_path)
        self.orbit_path.setScale(self.orbital_radius)
    
    def startSpin(self):
        self.day_period = self.model_path.hprInterval(PLANET_SPIN_VELOCITY, Vec3(360, 0, 0))
        self.day_period.loop()
        
    def accelerateOrbit(self, task):
        
        self.orbital_angle = self.orbital_angle + self.orbital_velocity
        self.orbital_angle = math.fmod(self.orbital_angle, 2.0*math.pi);
        self.point_path.setPos(self.orbital_radius * math.cos(self.orbital_angle),
                               self.orbital_radius * math.sin(self.orbital_angle), 0)
        self.position = self.point_path.getPos()
        self.orbital_velocity = self.orbital_velocity + 0.0001
        if self.orbital_velocity > self.max_orbital_velocity:
            return task.done
        else:
            return task.cont
    
    def stepOrbit(self, task):
        self.orbital_angle = self.orbital_angle + self.orbital_velocity
        self.orbital_angle = math.fmod(self.orbital_angle, 2.0*math.pi);
        self.point_path.setPos(self.orbital_radius * math.cos(self.orbital_angle),
                               self.orbital_radius * math.sin(self.orbital_angle), 0)
        self.position = self.point_path.getPos()
        return task.cont
    
    def drawLines(self): 
        # put some lighting on the line
        # for some reason the ambient and directional light in the environment drain out
        # all other colors in the scene
        # this is a temporary solution just so we can view the lines... the light can be removed and
        #a glow effect will be added later
#        alight = AmbientLight('alight')
#        alnp = render.attachNewNode(alight)
#        alight.setColor(Vec4(0.2, 0.2, 0.2, 1))
#        render.setLight(alnp)
        self.lines.reset()
        self.lines.drawLines([((0,0, 0),
                               (self.point_path.getX(), self.point_path.getY(), 0))])
        self.lines.create()
    
    def drawConnections(self, task):
#        cur_pos = self.point_path.getPos()
#        paired_pos = pairedPlanetDraw.point_path.getPos()
#        paired_pos = self.point_path.getRelativePoint(pairedPlanetDraw.point_path, pairedPlanetDraw.point_path.getPos())
#        print pairedPlanetDraw.point_path.getX(), pairedPlanetDraw.point_path.getY(), pairedPlanetDraw.point_path.getZ()
        self.connections.reset()
        if(self.next_planet):
            point_list = []
            point_list.append((self.point_path.getPos(), self.next_planet.point_path.getPos()))
            self.connections.drawLines(point_list)
            self.connections.create()
        return task.cont
        
    def changePlayer(self, player):
        '''
        Change the control of the planet from the self.player to the parameter player
        @param player: Player, the player who has captured the planet by swarms
        @precondition: the player must have used the capture ability of a swarm unit on the planet
        '''
        self.player = player
        
    def addOrbitingUnit(self, unit):
        ''' 
        Add a unit to the hosted units by the planet
        @param unit: Orbiting unit object
        '''
        self._orbiting_units.append(unit)
    
    def addOrbitingUnits(self, units):
        '''
        Add a list of units to be hosted by the planet
        @param units: iterable of units
        '''
        self._orbiting_units.extend(units)
    
    def removeOrbitingUnit(self, unit):
        ''' 
        Remove the hosted unit from the planet
        @param unit: Orbiting unit object
        '''
        self._orbiting_units.remove(unit)
    
    def removeOrbitingUnits(self, units):
        ''' 
        Remove many hosted units from the planet
        @param units: List of unit objects
        '''
        self._orbiting_units[:] = [u for u in self._orbiting_units if u not in units]
        
    def units(self):
        '''
        Generator that iterates over the hosted units.
        '''
        for unit in self._orbiting_units:
            yield unit
            
    def unitsOfPlayer(self, player):
        '''
        Generator that iterates over the hosted units belonging to the player.
        @param player, the owner of the units 
        '''
        for unit in self._orbiting_units:
            if(unit.player == player):
                yield unit
            
    def getNumberOfUnits(self):
        '''
        Returns the number of hosted units from the planet
        '''
        return len(self._orbiting_units)
    
    def getNumberOfUnitsOfPlayer(self, player):
        '''
        Returns the number of hosted units from the planet that belongs to the player
        @param player, the owner of the units
        '''
        num = 0
        for unit in self.units():
            if(unit.player == player):
                num = num + 1
        return num
    
    def _task_unit_timers(self):
        '''
        Generator that iterates over the hosted units construction tasks.
        '''
        for task_unit in self.task_unit_timers:
            yield task_unit
            
    def _task_structure_timers(self):
        '''
        Generator that iterates over the surface structure construction tasks.
        '''
        for task_structure in self.task_structure_timers:
            yield task_structure
            
    def _consumeUnits(self):
        if(self.task_unit_timer!=None):
            taskMgr.remove(self.task_unit_timer)
            self.task_unit_timer = None
        for task in self._task_unit_timers():
            if(task!=None):
                taskMgr.remove(task)
                self.task_unit_timers.remove(task)
                task = None
        for unit in self.units():
            unit.player.units.remove(unit)
            self.removeOrbitingUnit(unit)
            ''' TODO: remove unit model and its abilities if any'''
            unit = None
        
    def _consumeStructures(self):
        if(self.task_structure_timer!=None):
            taskMgr.remove(self.task_structure_timer)
            self.task_structure_timer = None
        for task in self._task_structure_timers():
            if(task!=None):
                taskMgr.remove(task)
                self.task_structure_timers.remove(task)
                task = None
        for structure in self.structures():
            self.player.structures.remove(structure)
            self.removeSurfaceStructure(structure)
            ''' TODO: remove structure texture'''
            structure = None
       
    def addSurfaceStructure(self, structure):
        ''' 
        Add a structure to the surface structures by the planet
        @param structure: Surface structure object
        '''
        if(len(self._surface_structures) < MAX_NUMBER_OF_STRUCTURE):
            self._surface_structures.append(structure)
    
    def addSurfaceStructures(self, structures):
        '''
        Add a list of structures to be hosted by the planet
        @param structures: iterable of structure
        '''
        if(len(self._surface_structures) + len(structures) <= MAX_NUMBER_OF_STRUCTURE):
            self._surface_structures.extend(structures)
    
    def removeSurfaceStructure(self, structure):
        ''' 
        Remove the surface structure from the planet
        @param structure: Surface structure object
        '''
        self._surface_structures.remove(structure)
    
    def removeSurfaceStructures(self, structures):
        ''' 
        Remove many surface structures from the planet
        @param structures: List of structure objects
        '''
        self._surface_structures[:] = [s for s in self._surface_structures if s not in structures]
        
    def structures(self):
        '''
        Generator that iterates over the surface structures.
        '''
        for structure in self._surface_structures:
            yield structure
            
    def getNumberOfStructures(self):
        '''
        Returns the number of surface structures from the planet
        '''
        return len(self._surface_structures)
        
    def hasStructure(self, structure):
        '''
        Returns true if a type of the structure already exists on the planet
        @structure: String, the desired structure type
        '''
        from structures import Forge, Nexus, Extractor, Phylon, GeneratorCore
        for surface_structure in self._surface_structures:
            if(structure == "forge" and type(surface_structure) == Forge):
                return True
            elif(structure == "nexus" and type(surface_structure) == Nexus):
                return True
            elif(structure == "extractor" and type(surface_structure) == Extractor):
                return True
            elif(structure == "phylon" and type(surface_structure) == Phylon):
                return True
            elif(structure == "generatorCore" and type(surface_structure) == GeneratorCore):
                return True
        return False
