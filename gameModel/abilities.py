'''
Created on Dec 29, 2011

@author: Bazibaz
'''
from abc import ABCMeta, abstractmethod

class Ability(object):
    __metaclass__ = ABCMeta
    '''
    This class contains the attributes to an ability for a given unit.
    '''

    def __init__(self, cool_down):
        '''
        Constructor
        @param cool_down : int, amount of time need t use the ability again (in seconds)
        '''
        self.cool_down = cool_down
        self.used = False #Prevents the same ability from being used successively.
        self.position = None #Position at which the ability is initiated 
        
    def use(self, unit_position):
        '''
        initiate ability based on type at given position of the unit
        '''
        if(self.used == False):
            self.position = unit_position