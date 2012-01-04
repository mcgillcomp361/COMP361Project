'''
Created on Jan 2, 2012

@author: Eran-Tasker
'''

class ResearchTree(object):
    '''
    classdocs
    '''


    def __init__(self, unitList, structList):
        '''
        Constructor
        '''
        self._level = 0
        self._unitTier = self._sortMap(unitList)
        self._structTier = self._sortMap(structList)
        
    '''
    Prepares the maps by sorting the levels in increasing order.
    The key will represent the level, while the values will be a list of
    available units/Structures up until that level.
    '''
    def _sortMap(self, strOrUnlist):
        return strOrUnlist
        
    
    '''
    Increments the level of the Tier by 1
    '''    
    def incrementLvl(self):
        if self._level != 4:
            self._level++
        #This statement is not necessary but a safety precaution
        elif self._level > 4:
            self._level = 4
    
    '''
    Decrements the level of the Tier by 1
    '''
    def decrementLvl(self):
        if self._level != 0:
            self._level--
        #This statement is not necessary but a safety precaution
        elif self._level < 0:
            self._level = 0
    
    '''
    Getter method
    '''
    def getLevel(self):
        return self._level
    
    