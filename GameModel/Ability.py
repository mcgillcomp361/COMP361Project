'''
Created on Dec 29, 2011

@author: Eran-Tasker
'''

class Ability(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._cool_down = 0
        self._damage = 0
        self._used = False
        
    def setCoolDown(self, _cool_down):
        self._cool_down = _cool_down
        
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