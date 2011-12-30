'''
Created on Dec 29, 2011

@author: Eran-Tasker
'''

class Structure(object):
    '''
    Contains the general information for structures.
    '''


    def __init__(self, energy):
        '''
        Constructor
        '''
        self._energy = energy
        
    def set_energy(self, energy):
        self._energy = energy
        
    def get_energy(self):
        return self._energy