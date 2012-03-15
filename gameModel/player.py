'''
Created on Jan 2, 2012

@author: Bazibaz
'''
from constants import MINERAL_STARTING_AMOUNT
from constants import GRAVITY_ENGINE_STARTING_AMOUNT

class Player(object):
    '''
    Player class
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.selectedPlanet = None
        self.selectedUnits = []
        self.planets = []
        self.structures = None
        self.units = None
        self.minerals = MINERAL_STARTING_AMOUNT
        self.ge_amount = GRAVITY_ENGINE_STARTING_AMOUNT
        
    