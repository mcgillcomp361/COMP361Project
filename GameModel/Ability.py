'''
Created on Dec 29, 2011

@author: Eran-Tasker
'''

class Ability(object):
    '''
    This class contains the attributes to an ability for a given unit.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._cool_down = 0 #Amount of time needed to use the ability again (in seconds)
        self._damage = 0 #Amount of damage
        self._used = False #Prevents the same ability from being used successively.
        
    '''
    Setters and Getters
    '''    
    def setCoolDown(self, cool_down):
        self._cool_down = cool_down
        
    def getCoolDown(self):
        return self._cool_down
    
    def set_damage(self, dmg):
        self._damage = dmg
        
    def get_damage(self):
        return self._damage
    
    def set_used(self, bol):
        self._used = bol
        
    def get_used(self):
        return self._used