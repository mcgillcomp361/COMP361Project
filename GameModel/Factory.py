'''
Created on Dec 29, 2011

@author: Eran-Tasker
'''

from Structure import Structure

class Factory(Structure):
    '''
    Subclass of Structure that focuses on producing units.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._units_in_construction = [] #Queue for units waiting to be trained.
        
    def addToQueue(self, unitType):
        self._units_in_construction.append(unitType)
        
    def removeFromQueue(self):
        return self._units_in_construction.pop()