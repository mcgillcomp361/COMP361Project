'''
Created on Dec 29, 2011

@author: Eran-Tasker
'''
from Structure import Structure

class Defense(Structure):
    '''
    Subclass of Structure that focuses on defense.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._damage = 0 #Amount of damage
    
    '''
    Setters and Getters
    ''' 
    def setDamage(self, damage):
        self._damage = damage
        
    def getDamage(self):
        return self._damage