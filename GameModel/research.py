'''
Created on 7 janv. 2012

@author: bazibaz
'''

_nb_of_tiers = 4

class ResearchTree(object):
    '''
    Research tree of player abilities
    '''

    def __init__(self, unit_list, struct_list):
        '''
        Constructor
        '''
        self._level = 0
        #TODO: why sort here? what?
        #Please use python built-in data structures: Ordered(Something)
        self.unit_tier = self._sort_map(unit_list)
        self.struct_tier = self._sort_map(struct_list)
        
    '''
    Prepares the maps by sorting the levels in increasing order.
    The key will represent the level, while the values will be a list of
    available units/Structures up until that level.
    '''
    def _sortMap(self, strOrUnlist):
        raise NotImplementedError("Research sort not implemented.")
    
    '''
    Increments the level of the Tier by 1
    '''    
    def incrementLevel(self):
        self._level = self._level + 1 if self._level < _nb_of_tiers else self._level
    
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