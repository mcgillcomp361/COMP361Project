'''
Created on 7 janv. 2012

@author: Bazibaz
'''
import random, math

from pandac.PandaModules import CollisionNode, CollisionBox, CollisionSphere, TransparencyAttrib
#from pandac.PandaModules import Vec3, Point2
from direct.showbase import DirectObject 
from panda3d.core import Vec3,Vec4,Point2, Point3, BitMask32
from direct.directtools.DirectGeometry import LineNodePath
from gameModel.constants import MAX_STAR_RADIUS, MAX_PLANET_RADIUS
from gui.Timer import Timer
from panda3d.core import Filename,Buffer,Shader, CardMaker
from panda3d.core import PandaNode,NodePath
from panda3d.core import AmbientLight,DirectionalLight
from direct.task import Task

class SphericalDraw(object):
    '''
    Information about a spherical object in the scene graph.
    It also encompasses a collision sphere of identical
    position and size.
    '''
    def __init__(self, SphericalBody, star_point_path=None):
        self.model = SphericalBody
        self.pos = Vec3(SphericalBody.position)
        self.radius = SphericalBody.radius
        # point_path: This dummy node path is only used to
        # displace the object, not to scale them. If we were to
        # scale them here, the scaling would propagate to child
        # nodes and make the sizes written set in the model very
        # strange. In short, the POSITIONS ARE RELATIVE but the
        # SCALING IS NOT. (Hence the "point" name.)
        if star_point_path == None:
            self.point_path = render.attachNewNode("sphere_node")
        else:
            self.point_path = star_point_path.attachNewNode("sphere_node")
        self.point_path.setPos(self.pos)
        
        #For transforming the object with scaling, colors, shading, etc.
        # Hosting the actual 3d model object.
        self.model_path = None
        
        # Collision sphere for object picking
        #-----------------------------------------------------
        # As described in the Tut-Chessboard.py sample: "If this model was
        # any more complex than a single polygon, you should set up a collision
        # sphere around it instead."
        self.cnode = CollisionNode("coll_sphere_node")
        #We use no displacement (0,0,0) and no scaling factor (1)
        self.cnode.addSolid(CollisionSphere(0,0,0,1))
        self.cnode.setIntoCollideMask(BitMask32.bit(1))
        self.cnode_path = render.attachNewNode(self.cnode)
        #For temporary testing, display collision sphere.
#        self.cnode_path.show()
    
    def select(self):
        self.model.select();

class StarDraw(SphericalDraw):
    '''
    Animating and rendering of a 3d star object.
    '''
    
    def __init__(self, star):
        super(StarDraw, self).__init__(star)
        #Models & textures
        self.model_path = loader.loadModel("models/stars/planet_sphere")
        self.star_tex = loader.loadTexture("models/stars/white_dwarf2.jpg")
        self.model_path.setTexture(self.star_tex, 1)
        self.model_path.reparentTo(self.point_path)
        self.model_path.setScale(self.radius)
        self.model_path.setPythonTag('pyStar', self);
        
        self.cnode.setTag('star', str(id(self)))
        # Reparenting the collision sphere so that it 
        # matches the star perfectly.
        self.cnode_path.reparentTo(self.model_path)
        self.star = star
        self.t = Timer(star)
    
    def update(self, event):
        if event == 'starLifetime':
                pass
                '''TODO : show star lifetime counter'''
        elif event == 'initiateStar':
                self.initiateStar()
        elif event == 'starStage2':
            self.changeStarStage(2)
        elif event == 'starStage3':
            self.changeStarStage(3)
        elif event == 'starStage4':
            self.changeStarStage(4)
        elif event == 'starStage5':
            self.changeStarStage(5)
        elif event == 'starStage6':
            '''TODO : black hole animation goes here'''
            '''TODO : planet movement animation into black hole'''
            self.changeStarStage(6)
        elif event == 'updateTimer':
            self.updateTimer()
        else:
            raise Exception, "Event received by spherical draw does not exist."
        
    def initiateStar(self):
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
        self.star_tex = loader.loadTexture("models/stars/star_stage1_tex.png")
        self.model_path.setTexture(self.star_tex, 1)

    def changeStarStage(self, stage):
        '''
        Changes the graphical aspects of the star according to its stage, including any animations needed
        @param stage : Integer, is the stage in which the star is in; consists of 6 stages
        '''
        self.planet_tex = loader.loadTexture("models/stars/star_stage"+str(stage)+"_tex.png")
        self.model_path.setTexture(self.planet_tex, 1)
        
        
    def updateTimer(self):
        self.t.refresh()
        self.t.star = self.star
        #TODO: There may be a threading problem here so I have left the updating of the time in comments.
        # I have gotten a deadlock error a couple times because of this.. 
        self.t.printTime()

class PlanetDraw(SphericalDraw):
    '''
    Animating and rendering of a 3d planet object.
    '''
    
    def __init__(self, planet, star_point_path):
        super(PlanetDraw, self).__init__(planet, star_point_path)
        self.orbital_velocity = planet.orbital_velocity
        self.spin_velocity = planet.spin_velocity
        self.orbital_radius = planet.orbital_radius
        self.orbital_angle = planet.orbital_angle
        print self.orbital_angle
        
        #Models & textures
        self.model_path = loader.loadModel("models/planets/planet_sphere")
        self.planet_tex = loader.loadTexture("models/planets/dead_planet_tex.jpg")
        self.model_path.setTexture(self.planet_tex, 1)
        self.model_path.reparentTo(self.point_path)
        self.model_path.setScale(self.radius)
        self.model_path.setPythonTag('pyPlanet', self);
        
        self.cnode.setTag('planet', str(id(self)))
        # Reparenting the collision sphere so that it 
        # matches the planet perfectly.
        self.cnode_path.reparentTo(self.model_path)
        
        self.star_point_path = star_point_path

        self.connections = LineNodePath(parent = self.star_point_path, thickness = 1.0, colorVec = Vec4(0,0,1.0,0.7))
        self.connections.create()
        self.lines = LineNodePath(parent = self.star_point_path, thickness = 4.0, colorVec = Vec4(1.0, 1.0, 1.0, 0.2))

        self.quad_path = None
#        self.lines.reparentTo(self.point_path)
    
    def highlight(self):
        flare_tex = base.loader.loadTexture("models/units/flare.png")
        cm = CardMaker('quad')
        cm.setFrameFullscreenQuad() # so that the center acts as the origin (from -1 to 1)
        self.quad_path = render.attachNewNode(cm.generate())
        self.quad_path.reparentTo(self.point_path)
        
        self.quad_path.setTransparency(TransparencyAttrib.MAlpha)
        self.quad_path.setTexture(flare_tex)
        self.quad_path.setColor(Vec4(0.2, 1.0, 0.3, 1))
        self.quad_path.setScale(15)
        self.quad_path.setPos(Vec3(0,0,0))
        self.quad_path.setBillboardPointEye()
    
    def update(self, event):
        if event == 'initiatePlanet':
            self.initiatePlanet()#also know as starStage1
        elif event == 'planetSelected':
            if not self.quad_path:
                self.highlight()
        elif event == 'planetUnselected':
            if self.quad_path:
                self.quad_path.detachNode()
                self.quad_path = None
        else:
            raise Exception, "Event received by spherical draw does not exist."
    def initiatePlanet(self):
        '''TODO : display planet creation animation '''
        '''TODO : add energy ray from planet to star that moves with the planet '''
        
        sound = base.loader.loadSfx("sound/effects/planet/planetCreation.wav")
        sound.setLoop(False)
        sound.setVolume(0.23)
        sound.play()
        
        self.radius = MAX_PLANET_RADIUS
        self.model_path.setScale(self.radius)
        
        #rand = random.randrange(1,8,1)
        self.star_tex = loader.loadTexture("models/planets/planet_activated_tex.png")
        self.model_path.setTexture(self.star_tex, 1)
        
        self.startSpin()
        self.drawLines()
        self.orbitTask = taskMgr.add(self.stepOrbit, 'planetOrbit')
        
    def startSpin(self):
        self.day_period = self.model_path.hprInterval(self.spin_velocity, Vec3(360, 0, 0))
        self.day_period.loop()
    
    def stepOrbit(self, task):
        self.orbital_angle = self.orbital_angle + self.orbital_velocity
        self.orbital_angle = math.fmod(self.orbital_angle, 2.0*math.pi);
        self.point_path.setPos(self.orbital_radius * math.cos(self.orbital_angle),
                               self.orbital_radius * math.sin(self.orbital_angle), 0)
        self.model.position = self.point_path.getPos()
        self.drawLines()
        return task.cont
        
#    def startOrbit(self):
#        self.orbit_period = self.root_path.hprInterval(
#                                    self.orbital_velocity,
#                                    Vec3(360, 0, 0))
#        self.orbit_period.loop()
        

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
        
    def drawConnections(self, pairedPlanetDraw, point_list):
#        cur_pos = self.point_path.getPos()
#        paired_pos = pairedPlanetDraw.point_path.getPos()
#        paired_pos = self.point_path.getRelativePoint(pairedPlanetDraw.point_path, pairedPlanetDraw.point_path.getPos())
#        print pairedPlanetDraw.point_path.getX(), pairedPlanetDraw.point_path.getY(), pairedPlanetDraw.point_path.getZ()
        self.connections.reset()
        self.connections.drawLines(point_list)
        self.connections.create()

class UnitDraw(object):
    def __init__(self, unit, host_draw_planet):
        self.host_draw_planet = host_draw_planet
        self.model = unit
        
        self.point_path = self.host_draw_planet.point_path.attachNewNode("unit_center_node")
        self.model_path = self.point_path.attachNewNode("unit_node")
        self.model_path.setPythonTag('pyUnit', self);
        self.model_path.setPos(Vec3(0,10,0))
        
        rad = 1
        self.cnode = CollisionNode("coll_sphere_node")
        self.cnode.addSolid(CollisionBox(Point3(-rad,-rad,-rad),Point3(rad,rad,rad)))
        self.cnode.setIntoCollideMask(BitMask32.bit(1))
        self.cnode.setTag('unit', str(id(self)))
        self.cnode_path = self.model_path.attachNewNode(self.cnode)
        self.cnode_path.show()
        
        
        self.tex = loader.loadTexture("models/units/flare.png")
        cm = CardMaker('quad')
        cm.setFrameFullscreenQuad()
        self.quad_path = self.model_path.attachNewNode(cm.generate())
        self.quad_path.setTexture(self.tex)
        self.quad_path.setTransparency(TransparencyAttrib.MAlpha)
        self.quad_path.setColor(Vec4(1.0, 0.3, 0.3, 1))
        self.quad_path.setScale(5)
        self.quad_path.setBillboardPointEye()
    
    def startOrbit(self):
        self.orbit_period = self.point_path.hprInterval(1, Vec3(-360, 0, 0))
        self.orbit_period.loop()

    def select(self):
        pass
