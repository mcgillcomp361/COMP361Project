'''
Created on Dec 29, 2011

@author: Bazibaz
'''
from abc import ABCMeta, abstractmethod
from constants import *

class Unit(object):
    __metaclass__ = ABCMeta
    '''
    General information and functions of units.
    '''

    def __init__(self, host_planet, max_velocity, energy, damage, unit_abilities=[]):
        '''
        Constructor
        @param host_planet : the current planet where the unit is being built
        @param max_velocity : the highest speed of the unit
        @param energy : the max energy the unit has when is ready to be used
        @param damage : the max damage the unit can deal to an enemy unit or structure
        @unit abilities : the abilities the unit has either unlocked or locked
        '''
        self.host_planet = host_planet
        #TODO : calculate starting position base on host_planet
        self.position = None
        self.max_velocity = max_velocity
        self.energy = energy
        self.damage = damage
        self.deep_space = False
        self._unit_abilities = unit_abilities
      
    def move(self, target_planet):
        '''
        Moves the unit from host_planet to target_planet
        If the target planet is in another solar system make the go into deep spave travel untill it
        reaches it's destination
        ''' 
        if(target_planet.parent_star==self.host_planet.parent_star):
            host_planet = target_planet
        else:
            self.deep_space = True
            #TODO : The unit will NOT be select-able for the duration of travel
            #TODO : keep track when the unit reaches the target planet then change the host
            host_planet = target_planet
           
    def attack(self, target_unit):
        '''Deals damage to an opposing unit.'''
        #TODO: Does this make sense, what if there is an interruption or a movement by the player
        while(target_unit.energy>=0):
            target_unit.energy =- self.damage
            
    
    def useAbility(self, ability):
        '''
        Uses the ability that has been assigned to the unit, if any.
        @param ability: Unit ability
        ''' 
        #TODO: this stuff are deep insanity !
        ability.use(self, self.position)
        
    def abilities(self):
        '''
        Generator iterating over the abilities.
        '''
        for ability in self._unit_abilities:
            yield ability
 
#TODO: create abilities for each unit when they are constructed 
class Swarm(Unit):
    '''
    Subclass of Units, Tier 1 Swarm
    '''
    def __init__(self, host_planet):
        '''
        Constructor
        @param host_planet : The planet where the unit is constructed
        '''
        super(Swarm, self).__init__(host_planet, SWARM_VELOCITY, SWARM_MAX_ENERGY, SWARM_DAMAGE, []) 
        
class Horde(Unit):
    '''
    Subclass of Units, Tier 2 Horde
    '''
    def __init__(self, host_planet):
        '''
        Constructor
        @param host_planet : The planet where the unit is constructed
        '''
        super(Horde, self).__init__(host_planet, HORDE_VELOCITY, HORDE_MAX_ENERGY, HORDE_DAMAGE, []) 
        
class Hive(Unit):
    '''
    Subclass of Units, Tier 3 Hive
    '''
    def __init__(self, host_planet):
        '''
        Constructor
        @param host_planet : The planet where the unit is constructed
        '''
        super(Hive, self).__init__(host_planet, HIVE_VELOCITY, HIVE_MAX_ENERGY, HIVE_DAMAGE, []) 
