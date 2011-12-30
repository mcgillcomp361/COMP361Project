'''
Created on Dec 29, 2011

@author: Eran-Tasker
'''
from Structure import Structure

class Lab(Structure):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._research = []
        
    def addToResearch(self, res):
        self._research.append(res)
        
    def removeResearch(self):
        self._research.pop()