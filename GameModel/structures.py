'''
Created on 7 janv. 2012

@author: Bazibaz
'''
from abc import ABCMeta, abstractmethod

_default_energy = 100

class Structure(object):
    __metaclass__ = ABCMeta
    '''
    Contains the general information for structures.
    '''
    @abstractmethod
    def __init__(self, energy):
        '''
        Constructor
        @param energy: Structure energy
        '''
        self.energy = energy
        

class Nexus(Structure):
    '''
    Subclass of Structure that unlocks the evolution tree and speeds up evolution.
    '''
    
    def __init__(self, energy=_default_energy):
        '''
        Constructor
        @param energy: Structure energy
        '''
        super(Nexus, self).__init__(energy)

       
class Defense(Structure):
    '''
    Subclass of Structure that focuses on defense.
    '''


    def __init__(self, energy=_default_energy):
        '''
        Constructor
        @param energy: Structure energy
        '''
        super(Defense, self).__init__(energy)
        self.damage = 0


class Forge(Structure):
    '''
    Subclass of Structure that focuses on producing units.
    '''
    
    def __init__(self, energy=_default_energy):
        '''
        Constructor
        @param energy: Structure energy
        '''
        super(Forge, self).__init__(energy)
        self._units_in_construction = [] #Queue for units waiting to be trained.
        
    def addToConstructionQueue(self, unitType):
        self._units_in_construction.append(unitType)
        
    def removeFromConstructionQueue(self):
        return self._units_in_construction.pop()
    

class Mine(Structure):
    '''
    Subclass of Structure that focuses on resource harvesting.
    '''

    def __init__(self, energy=_default_energy):
        '''
        Constructor
        @param energy: Structure energy
        '''
        super(Defense, self).__init__(energy)