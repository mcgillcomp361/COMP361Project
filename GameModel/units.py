'''
Created on Dec 29, 2011

@author: Bazibaz
'''
from abc import ABCMeta, abstractmethod

_default_energy = 0

class Unit(object):
    __metaclass__ = ABCMeta
    '''
    General information and functions of units.
    '''

    def __init__(self, host_planet=None, max_velocity=0, energy=0, damage=0, unit_abilities=[]):
        '''
        Constructor
        @name : ??
        TODO : add the rest
        '''
        self.host_planet = host_planet
        #TODO : calculate starting position base on host_planet
        self.position = position
        self.max_velocity = max_velocity
        self.energy = energy
        self.damage = damage
        self.deep_space = False
        self._unit_abilities = unit_abilities
      
    def move(self, target_planet):
        '''Moves the unit from host_planet to target_planet''' 
        host_planet = target_planet
           
    def attack(self):
        '''Deals damage to an opposing unit.'''
        #TODO: ...
        pass
    
    def useAbility(self, ability):
        '''
        Uses the ability that has been assigned to the unit, if any.
        @param ability: Unit ability
        ''' 
        ability.use(self, self.position)
        
    def abilities(self):
        '''
        Generator iterating over the abilities.
        '''
        for ability in self._unit_abilities:
            yield ability
 
 
class Swarm(Unit):
    '''
    Subclass of Structure that focuses on production of units of all Tiers.
    '''
    def __init__(self, name, host_planet):
        '''
        Constructor
        @param host_planet : The planet where the structure is constructed on
        '''
        super(Swarm, self).__init__(host_planet, SWARM_VELOCITY, SWARM_MAX_ENERGY, SWARM_DAMAGE, []) 
