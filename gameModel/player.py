'''
Created on Jan 2, 2012

@author: Bazibaz
'''
from constants import MINERAL_STARTING_AMOUNT, GRAVITY_ENGINE_STARTING_AMOUNT, FORGE_BUILD_TIME
from structures import *

class Player(object):
    '''
    Player class
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.selected_planet = None
        self.selected_star = None
        self.selecteUnit = None
        self.selectedUnits = []
        self.planets = []
        self.structures = []
        self.units = []
        self.minerals = MINERAL_STARTING_AMOUNT
        self.ge_amount = GRAVITY_ENGINE_STARTING_AMOUNT
        
    def addStructure(self, structure):
        '''
        Building a structure on the player's planet
        '''
        if(self.selected_planet != None and self.selected_planet.player == self):
            if(structure == "forge"):
                self.selected_planet.task_timer = taskMgr.doMethodLater(FORGE_BUILD_TIME, self._construct, 'buildForge')
        
    def _construct(self, task):
        forge = Forge(self.selected_planet)
        self.structures.append(forge)
        return task.done
    