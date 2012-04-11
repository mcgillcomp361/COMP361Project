'''
Created on Dec 29, 2011

@author: Bazibaz
'''
from abc import ABCMeta, abstractmethod
from constants import *
from pandac.PandaModules import CollisionNode, CollisionBox, CollisionSphere, CollisionTraverser, TransparencyAttrib
from direct.showbase import DirectObject
from direct.showbase import Audio3DManager
from direct.interval.IntervalGlobal import *
from panda3d.core import Vec3, Vec4, Point2, Point3, BitMask32, CardMaker
import math
import gameEngine


from panda3d.physics import BaseParticleEmitter,BaseParticleRenderer
from panda3d.physics import PointParticleFactory,SpriteParticleRenderer
from panda3d.physics import LinearNoiseForce,DiscEmitter
from panda3d.core import Filename
from direct.particles.Particles import Particles
from direct.particles.ParticleEffect import ParticleEffect
from direct.particles.ForceGroup import ForceGroup
import sys



class Unit(object):
    __metaclass__ = ABCMeta
    '''
    General information and functions of units.
    '''

    def __init__(self, host_planet, player, max_velocity, energy, damage, unit_abilities=[]):
        '''
        Constructor
        @param host_planet : the current planet where the unit is being built
        @param max_velocity : the highest speed of the unit
        @param energy : the max energy the unit has when is ready to be used
        @param damage : the max damage the unit can deal to an enemy unit or structure
        @unit abilities : the abilities the unit has either unlocked or locked
        '''
        self.host_planet = host_planet
        self.position = None
        self.player = player
        self.max_velocity = max_velocity
        self.energy = energy
        self.damage = damage
        self.target = None
        self.between_orbits = False
        self.deep_space = False
        self.host_planet.addOrbitingUnit(self)
        self._unit_abilities = unit_abilities
        self.__initSceneGraph()
        ''' TODO: add the cool down attack effect '''
        self.task_observe_enemy = taskMgr.doMethodLater(1, self._observeEnemy, 'observeEnemy')
         
    def _loadSounds(self, unit_name):
        '''
        Method to load sounds.
        '''
        #base.cTrav = CollisionTraverser()
        #audio3d = Audio3DManager.Audio3DManager(base.sfxManagerList[0], gameEngine.gameEngine._game_camera)
        
        self.move_unit = None
        self.select_unit = None
        self.attack_unit = None
        
        from gameModel.player import Player
        if(type(self.player)==Player):
            
            location = "sound/effects/units/" + unit_name + "/birth.wav"
            #base.loader.loadSfx(location).setLoop(False)
            base.loader.loadSfx(location).play()
            #audio3d.loadSfx(location).play()
        
            location = "sound/effects/units/" + unit_name + "/move.wav"
            self.move_unit = base.loader.loadSfx(location)
            #self.move_unit = audio3d.loadSfx(location)
            #self.move_unit.setLoop(False)
            self.move_unit.setVolume(0.7)
            #audio3d.setSoundVelocityAuto(self.move_unit)
            #audio3d.setListenerVelocityAuto()
            #audio3d.attachSoundToObject(self.move_unit, self)
        
            location = "sound/effects/units/" + unit_name + "/select.wav"
            self.select_unit = base.loader.loadSfx(location)
            #self.select_unit = audio3d.loadSfx(location)
            #self.select_unit.setLoop(False)
            self.select_unit.setVolume(0.7)
            #audio3d.setSoundVelocityAuto(self.select_unit)
            #audio3d.setListenerVelocityAuto()
            #audio3d.attachSoundToObject(self.select_unit, self)
        
        location = "sound/effects/units/" + unit_name + "/death.wav"
        self.death_unit = base.loader.loadSfx(location)
        #self.death_unit = audio3d.loadSfx(location)
        self.death_unit.setVolume(0.6)
        #audio3d.setSoundVelocityAuto(self.death_unit)
        #audio3d.setListenerVelocityAuto()
        #audio3d.attachSoundToObject(self.death_unit, self)
        
        if unit_name != "analyzer" and unit_name != "mathematica" and unit_name != "blackholegen":
            location = "sound/effects/units/" + unit_name + "/attack.wav"
            self.attack_unit = base.loader.loadSfx(location)
            #self.attack_unit = audio3d.loadSfx(location)
            #self.attack_unit.setLoop(False)
            self.attack_unit.setVolume(0.5)
            #audio3d.setSoundVelocityAuto(self.attack_unit)
            #audio3d.setListenerVelocityAuto()
            #audio3d.attachSoundToObject(self.attack_unit, self)
        
    
    def __initSceneGraph(self):
        
        self.point_path = self.host_planet.point_path.attachNewNode("unit_center_node")
        self.model_path = self.point_path.attachNewNode("unit_node")
        self.model_path.reparentTo(self.point_path)
        self.model_path.setPos(Vec3(0,6,0))
        
        self.model_path.setPythonTag('pyUnit', self)
        
        rad = 1
        cnode = CollisionNode("coll_sphere_node")
        cnode.addSolid(CollisionBox(Point3(-rad,-rad,-rad),Point3(rad,rad,rad)))
        cnode.setIntoCollideMask(BitMask32.bit(1))
        cnode.setTag('unit', str(id(self)))
        self.cnode_path = self.model_path.attachNewNode(cnode)
        #self.cnode_path.show()
        
        tex = loader.loadTexture("models/billboards/flare.png")
        cm = CardMaker('quad')
        cm.setFrameFullscreenQuad()
        self.quad_path = self.model_path.attachNewNode(cm.generate())
        self.quad_path.setTexture(tex)
        self.quad_path.setTransparency(TransparencyAttrib.MAlpha)
        self.quad_path.setBillboardPointEye()

        self.quad_path.setColor(self.player.color)
    
    def _observeEnemy(self, task):
        if not self.deep_space:
            if self.target != None and self.target.energy > 0 and \
                self.host_planet == self.target.host_planet and \
                not self.target.deep_space:
                self._attack(self.target)
                
            else:
                if(self.damage == 0):
                    return task.done
                self.target = None
                for unit in self.host_planet.unitsOfEnemyLowestEnergy(self.player):
                    self.target = unit
                    break
#        if(self.host_planet.player != self.player and self.host_planet.getNumberOfStructures()!=0):
#            for structure in self.host_planet.structures():
#                self._attack(structure)
        return task.again
    
    def highlight(self):
        self.cone_path = loader.loadModel("models/units/cone")
        self.cone_path.reparentTo(self.model_path)
        self.cone_path.setTransparency(TransparencyAttrib.MAlpha)
#        self.cone_path.setScale(2)
        self.cone_path.setPos(Vec3(0, 0, 3))
        self.cone_path.setP(180)
        self.cone_path.setColor(Vec4(0.3, 1, 0.2, 0.6))
    
    def is3dpointIn2dRegion(self, point1, point2): 
        """This function takes a 2d selection box from the screen as defined by two corners 
        and queries whether a given 3d point lies in that selection box 
        Returns True if it is 
        Returns False if it is not""" 
        #node is the parent node- probably render or similar node 
        #point1 is the first 2d coordinate in the selection box 
        #point2 is the opposite corner 2d coordinate in the selection box 
        #point3d is the point in 3d space to test if that point lies in the 2d selection box 
         
        # Convert the point to the 3-d space of the camera 
        p3 = base.cam.getRelativePoint(self.model_path, Vec3(0,0,0)) 

        # Convert it through the lens to render2d coordinates 
        p2 = Point2() 
        if not base.camLens.project(p3, p2): 
            return False 
         
        r2d = Point3(p2[0], 0, p2[1]) 

        # And then convert it to aspect2d coordinates 
        a2d = base.aspect2d.getRelativePoint(render2d, r2d) 
        #Find out the biggest/smallest X and Y of the 2- 2d points provided. 
        if point1.getX() > point2.getX(): 
            bigX = point1.getX() 
            smallX = point2.getX() 
        else: 
            bigX = point2.getX() 
            smallX = point1.getX() 
             
        if point1.getY() > point2.getY(): 
            bigY = point1.getY() 
            smallY = point2.getY() 
        else: 
            bigY = point2.getY() 
            smallY = point2.getY() 
         
        pX = a2d.getX() 
        pY = a2d.getZ()  #aspect2d is based on a point3 not a point2 like render2d. 
         
        if pX < bigX and pX > smallX: 
            if pY < bigY and pY > smallY: 
                 
                return True 
            else: return False 
        else: return False
    
    def deselect(self):
        self.cone_path.removeNode()
        
    def select(self):
        self.player.selected_units.append(self)
        if(len(self.player.selected_units) == 1):
            ''' TODO: show the statics of the unit in the characteristic panel on the GUI '''
            self.highlight()
            for unit in self.player.selected_units:
                if(unit.move_unit != None and unit.move_unit.status() == unit.move_unit.PLAYING):
                    unit.move_unit.stop()
            self.select_unit.play()
    
    def startOrbit(self):
        self.orbit_period = self.point_path.hprInterval(10, Vec3(-360, 0, 0))
        self.orbit_period.loop()
    
    def moveUnitPrev(self):
        self.move(self.host_planet.prev_planet)

    def moveUnitNext(self):
        self.move(self.host_planet.next_planet)
        
    def moveDeepSpace(self, planet):
        self.move(planet)
        #self.deep_space = True
        '''TODO : fix this method, deep space should be set to False when the unit arrives at destination'''
      
    def move(self, target_planet):
        '''
        Moves the unit from host_planet to target_planet
        If the target planet is in another solar system make the go into deep space travel until it
        reaches it's destination
        ''' 
        '''TODO: Speed coefficient based on unit type '''
        if self.between_orbits:
            pass
        else:
            self.between_orbits = True
    #       relativePos = target_planet.point_path.getPos(self.point_path)
            relativePos = self.point_path.getPos(target_planet.point_path)
            length = math.sqrt(relativePos.length())
            self.host_planet.removeOrbitingUnit(self)
            self.host_planet = target_planet
            target_planet.addOrbitingUnit(self)
            self.point_path.reparentTo(target_planet.point_path)
            self.point_path.setPos(relativePos)
            myseq = Sequence(
                LerpPosInterval(self.point_path,
                    self.max_velocity*length/11.0,
                    Point3(0,0,0),
    #               startPos=None,
    #                   other=self.host_planet.parent_star.point_path,
                    blendType='easeInOut',
                    bakeInStart=0
                ),
                Func(self._onPlanet)
             )
            myseq.start()
            #else:
            #   self.deep_space = True
                #TODO : The unit will NOT be select-able for the duration of travel
        if(self.select_unit != None and self.select_unit.status() == self.select_unit.PLAYING):
            self.select_unit.stop()
                
    def _onPlanet(self):
        self.between_orbits = False
    
    def _changeHostPlanet(self, target_planet):
        relativePos = target_planet.point_path.getPos(self.point_path)
        self.host_planet.removeOrbitingUnit(self)
        self.host_planet = target_planet
        target_planet.addOrbitingUnit(self)
        self.point_path.reparentTo(target_planet.point_path)
        self.point_path.setPos(relativePos)
            
    def _attack(self, target):
        '''Deals damage to an opposing unit or structure only if the unit is capable of attacking'''
        if(target.energy>0 and target != None):
            target.energy = max(0, target.energy-self.damage)
            if(self.attack_unit != None):
                self.attack_unit.play()
            
    
    def useAbility(self, ability):
        '''
        Uses the ability that has been assigned to the unit, if any.
        @param ability: Unit ability
        ''' 
        #TODO: this stuff are deep insanity !
        ability.use(self, self.position)
        
    def abilities(self):
        '''
        Generator iterating over the abilities.
        '''
        for ability in self._unit_abilities:
            yield ability
    
    def removeFromGame(self):
        self.death_unit.play()
        self.damage = 0
        self.task_observe_enemy = None
        self.target = None
        self.point_path.removeNode()
        
        '''TODO: remove the unit abilities '''
        #self._unit_abilities = unit_abilities
 
#TODO: create abilities for each unit when they are constructed 
class Swarm(Unit):
    '''
    Subclass of Units, Tier 1 Swarm
    '''
    def __init__(self, host_planet, player):
        '''
        Constructor
        @param host_planet : The planet where the unit is constructed
        '''
        base.enableParticles()
        super(Swarm, self).__init__(host_planet, player, SWARM_VELOCITY, SWARM_MAX_ENERGY, SWARM_DAMAGE, [])
        self.quad_path.setScale(2)
#        self.quad_path.removeNode()
        self._loadSounds("swarm")
        self.model_path.setColor(Vec4(1,1,1,0.1))
        self.model_path.setLightOff()
        self.p = ParticleEffect()
        self.p.loadConfig('models/units/swarm/swarm.ptf')
        self.p.start(self.model_path)
        #TODO:Remove
                   
class Horde(Unit):
    '''
    Subclass of Units, Tier 2 Horde
    '''
    def __init__(self, host_planet, player):
        '''
        Constructor
        @param host_planet : The planet where the unit is constructed
        '''
        super(Horde, self).__init__(host_planet, player, HORDE_VELOCITY, HORDE_MAX_ENERGY, HORDE_DAMAGE, []) 
        self.quad_path.setScale(3)
        self._loadSounds("horde")
        
class Hive(Unit):
    '''
    Subclass of Units, Tier 3 Hive
    '''
    def __init__(self, host_planet, player):
        '''
        Constructor
        @param host_planet : The planet where the unit is constructed
        '''
        super(Hive, self).__init__(host_planet, player, HIVE_VELOCITY, HIVE_MAX_ENERGY, HIVE_DAMAGE, [])
        self.quad_path.setScale(4)
        self._loadSounds("hive")
        
class Globe(Unit):
    '''
    Subclass of Units, Tier 1 Globe
    '''
    def __init__(self, host_planet, player):
        '''
        Constructor
        @param host_planet : The planet where the unit is constructed
        '''
        super(Globe, self).__init__(host_planet, player, GLOBE_VELOCITY, GLOBE_MAX_ENERGY, GLOBE_DAMAGE, [])
        unit_model_path = loader.loadModel("models/units/globe/sphere")
        tex = loader.loadTexture("models/units/globe/globe_tex.jpg")
        unit_model_path.setTexture(tex)
        unit_model_path.reparentTo(self.model_path)
        unit_model_path.setScale(1.1)
        self.quad_path.setScale(2)
        self._loadSounds("globe")

class Sphere(Unit):
    '''
    Subclass of Units, Tier 2 Sphere
    '''
    def __init__(self, host_planet, player):
        '''
        Constructor
        @param host_planet : The planet where the unit is constructed
        '''
        super(Sphere, self).__init__(host_planet, player, SPHERE_VELOCITY, SPHERE_MAX_ENERGY, SPHERE_DAMAGE, [])
        unit_model_path = loader.loadModel("models/units/sphere/sphere")
        tex = loader.loadTexture("models/units/sphere/sphere_tex.jpg")
        unit_model_path.setTexture(tex)
        unit_model_path.reparentTo(self.model_path)
        unit_model_path.setScale(1.7)
        self.quad_path.setScale(3)
        self._loadSounds("sphere")

class Planetarium(Unit):
    '''
    Subclass of Units, Tier 3 Planetarium
    '''
    def __init__(self, host_planet, player):
        '''
        Constructor
        @param host_planet : The planet where the unit is constructed
        '''
        super(Planetarium, self).__init__(host_planet, player, PLANETARIUM_VELOCITY, PLANETARIUM_MAX_ENERGY, PLANETARIUM_DAMAGE, [])
        unit_model_path = loader.loadModel("models/units/planetarium/sphere")
        tex = loader.loadTexture("models/units/planetarium/planetarium_tex.jpg")
        unit_model_path.setTexture(tex)
        unit_model_path.reparentTo(self.model_path)
        unit_model_path.setScale(2.5)
        self.quad_path.setScale(4.2)
        self._loadSounds("planetarium")        

class Analyzer(Unit):
    '''
    Subclass of Units, Tier 1 Analyzer
    '''
    def __init__(self, host_planet, player):
        '''
        Constructor
        @param host_planet : The planet where the unit is constructed
        '''
        super(Analyzer, self).__init__(host_planet, player, ANALYZER_VELOCITY, ANALYZER_MAX_ENERGY, ANALYZER_DAMAGE, [])
        unit_model_path = loader.loadModel("models/units/analyzer/SpaceDock")
        unit_model_path.reparentTo(self.model_path)
        unit_model_path.setScale(0.02)
        self.quad_path.setScale(1)
        self._loadSounds("analyzer")

class Mathematica(Unit):
    '''
    Subclass of Units, Tier 3 Mathematica
    '''
    def __init__(self, host_planet, player):
        '''
        Constructor
        @param host_planet : The planet where the unit is constructed
        '''
        super(Mathematica, self).__init__(host_planet, player, MATHEMATICA_VELOCITY, MATHEMATICA_MAX_ENERGY, MATHEMATICA_DAMAGE, [])
        unit_model_path = loader.loadModel("models/units/mathematica/SpaceDock")
        unit_model_path.reparentTo(self.model_path)
        unit_model_path.setScale(0.05)
        self.quad_path.setScale(2)
        self._loadSounds("mathematica")

class BlackHoleGenerator(Unit):
    '''
    Subclass of Units, Tier 4 BlackHoleGenerator
    '''
    def __init__(self, host_planet, player):
        '''
        Constructor
        @param host_planet : The planet where the unit is constructed
        '''
        super(BlackHoleGenerator, self).__init__(host_planet, player, BLACK_HOLE_GENERATOR_VELOCITY, BLACK_HOLE_GENERATOR_MAX_ENERGY, BLACK_HOLE_GENERATOR_DAMAGE, [])
        unit_model_path = loader.loadModel("models/units/blackholegen/Icosahedron")
        tex = loader.loadTexture("models/units/planetarium/special_tex.jpg")
        unit_model_path.setTexture(tex)
        unit_model_path.reparentTo(self.model_path)
        unit_model_path.setScale(0.3)
        self.quad_path.setScale(1.5)
        self._loadSounds("blackholegen")