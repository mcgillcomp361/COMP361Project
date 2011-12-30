'''
Created on Dec 29, 2011

@author: Eran-Tasker
'''
from Structure import Structure

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._damage = 0
        
    def setDamage(self, damage):
        self._damage = damage
        
    def getDamage(self):
        return self._damage