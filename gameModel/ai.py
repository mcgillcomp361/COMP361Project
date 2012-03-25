'''
Created on March 25, 2012

@author: Bazibaz
'''
from constants import MINERAL_STARTING_AMOUNT, GRAVITY_ENGINE_STARTING_AMOUNT, AI_MINERAL_STARTING_AMOUNT, AI_GRAVITY_ENGINE_STARTING_AMOUNT, \
                    FORGE_BUILD_TIME, NEXUS_BUILD_TIME, EXTRACTOR_BUILD_TIME, PHYLON_BUILD_TIME, GENERATOR_CORE_BUILD_TIME, \
                    SWARM_BUILD_TIME, SWARM_MINERAL_COST, GLOBE_BUILD_TIME, GLOBE_MINERAL_COST, ANALYZER_BUILD_TIME, ANALYZER_MINERAL_COST, \
                    HORDE_BUILD_TIME, HORDE_MINERAL_COST, SPHERE_BUILD_TIME, SPHERE_MINERAL_COST, \
                    HIVE_BUILD_TIME, HIVE_MINERAL_COST, PLANETARIUM_BUILD_TIME, PLANETARIUM_MINERAL_COST, MATHEMATICA_BUILD_TIME, MATHEMATICA_MINERAL_COST, \
                    BLACK_HOLE_GENERATOR_BUILD_TIME, BLACK_HOLE_GENERATOR_MINERAL_COST, \
                    NUMBER_OF_STARS
from structures import *
from units import *
from solar import *
import random

class AI(object):
    '''
    Artificial opponent class
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.planets = []
        self.structures = []
        self.units = []
        self.minerals = AI_MINERAL_STARTING_AMOUNT
        self.ge_amount = AI_GRAVITY_ENGINE_STARTING_AMOUNT
        
    def activateStar(self, all_stars):
        if(self._allStarsActivated(all_stars) == False):    
            while(True):
                star = all_stars[random.randrange(0, NUMBER_OF_STARS, 1)]
                if not star.activated:
                    star.activateStar(self)
                    break
            
    def _allStarsActivated(self, all_star):
        for star in all_star:
            if(star.activated == False):
                return False
        return True
    
    def _AllPlanetsActivated(self, star):
        for planet in star.planets():
            if(planet.activated == False):
                return False
        return True
    