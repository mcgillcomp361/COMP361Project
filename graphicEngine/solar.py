'''
Created on 7 janv. 2012

@author: Bazibaz
'''
import random

from pandac.PandaModules import CollisionNode, CollisionSphere
#from pandac.PandaModules import Vec3, Point2
from panda3d.core import Vec3,Vec4,Point2,BitMask32
from direct.directtools.DirectGeometry import LineNodePath
from gameModel.constants import MAX_STAR_RADIUS, MAX_PLANET_RADIUS
from panda3d.core import Filename,Buffer,Shader
from panda3d.core import PandaNode,NodePath
from panda3d.core import AmbientLight,DirectionalLight

class SphericalDraw(object):
    '''
    Information about a spherical object in the scene graph.
    It also encompasses a collision sphere of identical
    position and size.
    '''
    def __init__(self, SphericalBody, point_path=None):
        self.model = SphericalBody
        self.pos = Vec3(SphericalBody.position)
        self.vel = Vec3()
        self.radius = SphericalBody.radius
        
        # Dummy parent paths for both model & collision sphere
        #-----------------------------------------------------
        # root_path: This dummy node copying the parent position
        # is used as a center of orbit. The copy is necessary
        # so that the rotation of the orbiting body does not
        # affect the parent object.
        #
        # point_path: This dummy node path is only used to
        # displace the object, not to scale them. If we were to
        # scale them here, the scaling would propagate to child
        # nodes and make the sizes written set in the model very
        # strange. In short, the POSITIONS ARE RELATIVE but the
        # SCALING IS NOT. (Hence the "point" name.)
        #-----------------------------------------------------
        self.root_path = None
        if point_path == None:
            self.point_path = render.attachNewNode("sphere_node")
        else:
            self.root_path = point_path.attachNewNode("orbit_root_node")
            self.point_path = self.root_path.attachNewNode("sphere_node")
        self.point_path.setPos(self.pos)
        
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
    
    def update(self, event):
        if event == 'starLifetime':
                pass
                '''TODO : show star lifetime counter'''
        elif event == 'initiateStar':
                self.initiateStar()
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
        self.star_tex = loader.loadTexture("models/stars/bstar.png")
        self.model_path.setTexture(self.star_tex, 1)


class PlanetDraw(SphericalDraw):
    '''
    Animating and rendering of a 3d planet object.
    '''
    
    def __init__(self, planet, star_point_path):
        super(PlanetDraw, self).__init__(planet, star_point_path)
        self.orbital_velocity = planet.orbital_velocity
        self.spin_velocity = planet.spin_velocity
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
        self.lines = LineNodePath(parent = self.root_path, thickness = 4.0, colorVec = Vec4(1.0, 1.0, 1.0, 1.0))
        self.lines.setColor(Vec4(1.0, 1.0, 1.0, 0.05))

#        self.lines.reparentTo(self.point_path)
    
    def update(self, event):
        if event == 'initiatePlanet':
            self.initiatePlanet()
        elif event == 'planetSelected':
            '''TODO: hightlight the planet'''
            pass
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
        self.startOrbit()
        self.drawLines()
        
    def startSpin(self):
        self.day_period = self.model_path.hprInterval(self.spin_velocity, Vec3(360, 0, 0))
        self.day_period.loop()
    
    def startOrbit(self):
        self.orbit_period = self.root_path.hprInterval(
                                    self.orbital_velocity,
                                    Vec3(360, 0, 0))
        self.orbit_period.loop()

    def drawLines(self): 
        self.lines.reset()
        self.lines.drawLines([((0,0, 0),
                               (self.point_path.getX(), self.point_path.getY(), 0))])
        self.lines.create()