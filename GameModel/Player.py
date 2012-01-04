'''
Created on Jan 2, 2012

@author: Eran-Tasker
'''

class Player(object):
    '''
    Player class
    '''


    def __init__(self, name, planets, structures, units, reasearch_tree):
        '''
        Constructor
        '''
        self._name = name
        self._planets = planets
        self._structures = structures
        self._units = units
        self._research_tree = reasearch_tree
        
    '''
    Setters and Getters
    '''
    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name
        
    def getPlanets(self):
        return self._planets
    
    def setPlanets(self, planets):
        self._planets = planets
        
    def getStructs(self):
        return self._structures
    
    def setStructs(self, structures):
        self._structures = structures
        
    def getUnits(self):
        return self._units
    
    def setUnits(self, units):
        self._units = units
        
    def getResTree(self):
        return self._research_tree
    
    def setResTree(self, research_tree):
        return self._research_tree