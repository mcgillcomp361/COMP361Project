'''
Created on 2011-11-25

@author: Bazibaz
'''

class Star(object):
    '''
    Class star contains the attributes of the object star and the it's functions.
    '''
    
    _timeToExplosion = None     #The counter for the star's life in seconds (Game time) 
    _radius = None      #The radius of the star in double 
    _center = None      #The position of the center of the star in Point3D
    _planets = None      #The list of all the planets orbiting the star 

    def __init__(self, timeToExplosion, radius, center):
        '''
        Constructor for class star: creates a star object, initializing the star's attributes with 
        the given parameters. 
        timeToExplosion : integer
        radius : double 
        center : Point3D
        '''
        
        self._timeToExplosion = timeToExplosion
        self._radius =  radius 
        self._center = center
        self._planets = []
        self.loadStar()
        #for i in range(planets.size):
        #    self.planets.insert(i, planets.pop(i))
        
    def getTime(self):
        '''
        Getter method which returns the remaining time to the star's death 
        '''
        return self._timeToExplosion
    
    def setTime(self, timeToExplosion):
        '''
        Setter method which initializes the timeToExplosion attribute of star class to the parameter
        '''
        self._timeToExplosion = timeToExplosion
        
    def getRadius(self):
        '''
        Getter method which returns the star's radius
        '''
        return self._radius
        
    def setRadius(self, radius):
        '''
        Setter method which initializes the radius attribute of star class to the parameter
        '''
        self._radius = radius
        
    def addPlanet(self, planet):
        '''
        Adds a planet to the star system
        '''
        self._planets.append(planet)
        
    def removePlanet(self, planet):
        '''
        removes a planet from the star system
        '''
        #self._planets.
        #self.planets.remove(planet)
        
    def removeAllPlanets(self):
        '''
        removes all the planets in the star system
        '''
        self._planets = []
        
    
    def getCenter(self):
        '''
        Getter method which returns the star's center position
        '''
        return self._center
        
    def setCenter(self, center):
        '''
        Setter method which initializes the center attribute of star class to the parameter
        '''
        self._center = center
        
    def loadStar(self):
        self.sun = loader.loadModel("../models/planet_sphere")
        self.sun_tex = loader.loadTexture("../models/sun_1k_tex.jpg")
        self.sun.setTexture(self.sun_tex, 1)
        self.sun.reparentTo(render)
        self.sun.setScale(2 * self._radius)
    
