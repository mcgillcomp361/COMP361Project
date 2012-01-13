'''
Created on Dec 29, 2011

@author: Bazibaz
'''

class Unit(object):
    '''
    General information and functions of units.
    '''

    def __init__(self, name, host_planet=None, position=None, max_velocity=0, energy=0, damage=0, unit_abilities=[]):
        '''
        Constructor
        '''
        self.name = name
        self.host_planet = host_planet
        self.position = position
        self.max_velocity = max_velocity
        self.energy = energy
        self.damage = damage
        self.deep_space = False
        self._unit_abilities = unit_abilities
        
    
    def useAbility(self, ability):
        '''
        Uses the ability that has been assigned to the unit, if any.
        @param ability: Unit ability
        ''' 
        pass
    
    
    def attack(self):
        '''Deals damage to an opposing unit.'''
        #TODO: ...
        pass
    
        
    def abilities(self):
        '''
        Generator iterating over the abilities.
        '''
        for ability in self._unit_abilities:
            yield ability
