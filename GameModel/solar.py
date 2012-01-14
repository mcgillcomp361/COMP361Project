'''
Created on 7 janv. 2012

@author: Bazibaz
'''
from constants import *
from abc import ABCMeta, abstractmethod

class SphericalBody(object):
    __metaclass__ = ABCMeta
    
    '''
    Abstract class defining a radius and a position
    '''
    
    @abstractmethod
    def __init__(self, position, radius):
        '''
        Constructor
        @param position: Point3D, position in space
        @param radius: float, body radius
        '''
        self.radius =  radius 
        self.position = position


class Star(SphericalBody):
    '''
    Class star contain attributes of the star and
    a list of all the planets orbiting the star.
    '''

    def __init__(self, position, radius):
        '''
        Constructor for class star: creates a dead star object, initializing the star's attributes with 
        the given parameters. 
        @param position : Point3D, the position of the center of the star
        @param radius : float, star radius
        '''
        super(Star, self).__init__(position, radius)
        self.lifetime = 0
        self._planets = []
        
    def activateStar(self, lifetime=1800000):
        '''
        Activates a constructed dead star object, starting the lifetime counter with the assigned default value while
        the Game Engine calls the graphic engine to display the corresponding animation.
        @param lifetime : integer, the counter for the star's life in seconds (Game time)
        '''
        self.lifetime = lifetime
        
    def addPlanet(self, planet):
        '''
        Adds a planet to the star system
        @param: planet object
        '''
        if(self._planets < MAX_NUMBER_OF_PLANETS):
            self._planets.append(planet)
        
    def removePlanet(self, planet):
        '''
        removes a planet from the star system
        @param planet object
        '''
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
            
    def getNumberOfPlanets(self):
        '''
        Returns the number of planets currently orbiting the star
        '''
        len(self._planets)


class Planet(SphericalBody): 
    '''
    Planet contains units and structures
    '''

    def __init__(self, position, radius, parent_star=None):
        '''
        Constructor for class planet.
        @param position: Point3D, position in space
        @param radius: float, body radius
        '''
        super(Planet, self).__init__(position, radius)
        self.orbital_velocity = 0
        self.parent_star = parent_star
        self._orbiting_units = []
        self._surface_structures = []
        
    def activatePlanet(self, orbital_velocity):
        '''
        Activates a constructed dead planet object, starting the orbital movement with the assigned value while
        the Game Engine calls the graphic engine to display the corresponding animation.
        @param orbital_velocity: the speed at which the planet rotates the star
        @precondition: MIN_PLANET_VELOCITY < orbital_velocity < MAX_PLANET_VELOCITY
        '''
        self.orbital_velocity = orbital_velocity
    
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
            
    def getNumberOfUnits(self):
        '''
        Returns the number of hosted units from the planet
        '''
        len(self._orbiting_units)
            
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
        len(self._surface_structures)
            
    
    