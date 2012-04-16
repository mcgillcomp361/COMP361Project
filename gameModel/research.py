'''
Created on 7 janv. 2012

@author: Bazibaz
'''

class ResearchTree(object):
    '''
    Evolution tree of unit abilities and tier's of technology
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._level = 1
        self.capture = False
        self.cloak = False
        self.vision = False
        self.burrow = False
        self.healing_aura = False
        self.harvest = False
        self.ring_of_fire = False
        self.control_wave = False
        self.generate_black_hole = False
        
    '''
    Increments the level of the Tier by 1
    '''    
    def incrementLevel(self, player):
        self._level = self._level + 1 if self._level < 4 else self._level
        if(player.selected_planet != None):
            from gameEngine.gameEngine import updateGUI
            updateGUI.refreshUnitsAndConstructions(player.selected_planet)
    
    '''
    Decrements the level of the Tier by 1
    '''
    def decrementLevel(self):
        self._level = self._level - 1 if self._level > 0 else self._level
    
    '''
    Get current tier level
    '''
    def getLevel(self):
        return self._level