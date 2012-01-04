'''
Created on 2011-11-25

@author: Terminal
'''

class Planet(object):
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
        
        
    
        