'''
Created on Dec 29, 2011

@author: Eran-Tasker
'''

class Structure(object):
    '''
    classdocs
    '''


    def __init__(self, _energy):
        '''
        Constructor
        '''
        self._energy = _energy
        
    def set_energy(self, _energy):
        self._energy = _energy
        
    def get_energy(self):
        return self._energy