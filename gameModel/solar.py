'''
Created on 7 janv. 2012

@author: Bazibaz
'''
from observable import Observable
#from gameEngine.gameEngine import *
from constants import MAX_NUMBER_OF_PLANETS, MAX_NUMBER_OF_STRUCTURE, LIFETIME, MAX_STAR_RADIUS
from time import time
from threading import Timer

import math

class SphericalBody(Observable):
    
    '''
    Abstract class defining a radius and a position
    '''
    
    def __init__(self, position, radius, activated, player):
        '''
        Constructor
        @param position: Point3D, position in space
        @param radius: float, body radius
        @param activated: boolean, determine whether the spherical body is activated by the player or not
        @param player: the player who owns the solar object
        '''
        super(SphericalBody,self).__init__()
        self.radius =  radius 
        self.position = position
        self.activated = activated
        self.player = player
        self.spin_velocity = 0
        
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
        self.counter = None
    
    def select(self):
        '''
        This method observes the events on the star and calls the related methods
        and notifies the corresponding objects based on the state of the star
        '''
        if(self.activated):
            self.notify('starLifetime')
        else:
            self.notify('initiateStar')
            self.activateStar()
        
    def activateStar(self):
        '''
        Activates a constructed dead star object, starting the lifetime counter with the assigned default value while
        the Game Engine calls the graphic engine to display the corresponding animation.
        '''
        self.lifetime = LIFETIME
        self.stage = 1
        self.activated = True
        self.radius = MAX_STAR_RADIUS
        '''TODO : get the player from the game engine '''
        #self.player = GameEngine.player
        self.counter = Timer(1.0, self.tackStarLife)
        self.counter.start()
        
    def tackStarLife(self):
        #elapsed_time = math.floor(time() - self.birth_time)
        self.lifetime = self.lifetime - float(self.getNumberOfActivePlanets())/(2)
        self.notify('updateTimer')
   #     print self.lifetime
        if(self.lifetime <= LIFETIME - LIFETIME/6 and self.stage == 1):
            self.stage = 2
            self.notify('starStage2')
        elif(self.lifetime <= LIFETIME - LIFETIME/3 and self.stage == 2):
            self.stage = 3
            self.notify('starStage3')
        elif(self.lifetime <= LIFETIME - LIFETIME/2 and self.stage == 3):
            self.stage = 4
            self.notify('starStage4')
        elif(self.lifetime <= LIFETIME - 2*LIFETIME/3 and self.stage == 4):
            self.stage = 5
            self.notify('starStage5')
        if(self.lifetime <= 0):
            self.stage = 6
            self.notify('starStage6')
            '''TODO : tell all the other planets to start moving into the black hole '''
        else:
            self.counter = Timer(1.0, self.tackStarLife)
            self.counter.start()
        
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
        sum = 0
        for planet in self.planets():
            if(planet.activated):
                sum = sum + 1
        return sum
                 


class Planet(SphericalBody): 
    '''
    Planet contains units and structures
    '''

    def __init__(self, position, radius, parent_star=None, prev_planet=None, player=None):
        '''
        Constructor for class planet.
        @param position: Point3D, position in space
        @param radius: float, body radius
        @param player: Player, the owner of the planet
        @param parent_star: Star, the specific star the planet is orbiting around
        @param prev_planet: previous planet in the star system, if None then the planet is the first
        '''
        super(Planet, self).__init__(position, radius, False, player)
        self.orbital_velocity = 0
        self.parent_star = parent_star
        self.prev_planet = prev_planet
        self.next_planet = None
        self._orbiting_units = []
        self._surface_structures = []
    
    def select(self):
        '''
        This method observes the events on the planet and calls the related methods
        and notifies the corresponding objects based on the state of the planet
        '''
        if(self.activated):
            print "prev_planet:" + str(self.prev_planet)
            print "next_planet:" + str(self.next_planet)
            self.notify('planetSelected')
        else:
            ''' TODO : get the player who selected the planet '''
            if((self.prev_planet == None or self.prev_planet.activated) and self.parent_star.activated):
                self.notify('initiatePlanet')
                self.activatePlanet(None)         
        
    def activatePlanet(self, player):
        '''
        Activates a constructed dead planet object, starting the orbital movement with the assigned value while
        the Game Engine calls the graphic engine to display the corresponding animation.
        @param player: Player, the player who controls the planet
        @precondition: MIN_PLANET_VELOCITY < orbital_velocity < MAX_PLANET_VELOCITY
        '''
        self.player = player
        self.activated = True
        
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
            
    
    