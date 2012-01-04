'''
Created on 2011-11-25

@author: Terminal
'''
from direct.showbase import DirectObject 
from pandac.PandaModules import Vec3,Vec2 
import math 
from direct.interval.IntervalGlobal import *

class Planet(DirectObject.DirectObject): 
    '''
    Class planet contains the attributes of the object planet and the it's functions.
    '''
    _orbitingUnits = None
    _surfaceStructures = None
    _orbital_velocity = None
    _rotate_velocity = None
    _center = None
    _radius = None

    def __init__(self, orbitalVelocity, rotateVelocity, center, radius):
        '''
        Constructor for class planet: creates a planet object, initializing the planet's attributes with 
        the given parameters. 
        orbitalVelocity : double (direction vector ?)
        rotateVelocity : double
        center : Point3D
        radius : double 
        '''
        
        self._center = center
        self._radius = radius
        self._orbital_velocity = orbitalVelocity
        self._orbitingUnits = rotateVelocity
        self.orbitingUnits = []
        self._surfaceStructures = []
        self.orbitscale = 10
        self.loadPlanet()
        self.rotatePlanet()      
        
    def getOrbitalVelocity(self):
        '''
        Getter method which returns the remaining time to the star's death 
        '''        
        return self._orbital_velocity
 
    def setOrbitalVelocity(self, orbitalVelocity):
        '''
        Setter method which set the orbital velocity of the planet to the given parameter
        '''        
        self._orbital_velocity = orbitalVelocity
        
    def loadPlanet(self):
        self.orbit_root_mercury = render.attachNewNode('orbit_root_mercury')

    
        self.mercury = loader.loadModel("../models/planet_sphere")
        self.mercury_tex = loader.loadTexture("../models/mercury_1k_tex.jpg")
        self.mercury.setTexture(self.mercury_tex, 1)
        self.mercury.reparentTo(self.orbit_root_mercury)
        self.mercury.setPos( 0.38 * self.orbitscale, 0, 0)
        self.mercury.setScale(0.385 * self._radius)
    
    def rotatePlanet(self):
        self.orbit_period_mercury = self.orbit_root_mercury.hprInterval(
          (0.241 * self._orbital_velocity), Vec3(360, 0, 0))
        self.day_period_mercury = self.mercury.hprInterval(
          (59 * self._orbitingUnits), Vec3(360, 0, 0))
    
        self.orbit_period_mercury.loop()
        self.day_period_mercury.loop()
       
      #end RotatePlanets()
        
            