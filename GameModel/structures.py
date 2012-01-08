'''
Created on 7 janv. 2012

@author: num3ric
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
        

class Lab(Structure):
    '''
    Subclass of Structure that focuses on research.
    '''
    
    def __init__(self, energy=_default_energy):
        '''
        Constructor
        @param energy: Structure energy
        '''
        super(Lab, self).__init__(energy)
        self._research = []
        
    def addToResearch(self, research):
        self._research.append(research)
        
    def removeResearch(self, research):
        self._research.remove(research)

       
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


class Factory(Structure):
    '''
    Subclass of Structure that focuses on producing units.
    '''
    
    def __init__(self, energy=_default_energy):
        '''
        Constructor
        @param energy: Structure energy
        '''
        super(Factory, self).__init__(energy)
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