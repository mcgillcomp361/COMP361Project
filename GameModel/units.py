'''
Created on Dec 29, 2011

@author: bazibaz
'''

class Unit(object):
    '''
    General information and functions of units.
    '''

    def __init__(self, name, host_planet):
        '''
        Constructor
        '''
        self.name = name
        self.host_planet = host_planet
        self.position = None
        self.energy = 0
        self.damage = 0
        self.deep_space = False
        self._unit_abilities = set([]) #set to avoid duplicates
        
    
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
        
    def addAbility(self, ability):
        '''
        Add ability to unit
        @param ability: Unit ability
        '''
        self._unit_abilities.add(ability)
    
    def addAbilities(self, abilities):
        '''
        Add abilities to unit
        @param abilities: List of unit abilities
        '''
        self._unit_abilities.update(abilities)
        
    def abilities(self):
        '''
        Generator iterating over the abilities.
        '''
        for ability in self._unit_abilities:
            yield ability
