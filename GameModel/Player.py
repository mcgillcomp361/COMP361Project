'''
Created on Jan 2, 2012

@author: Bazibaz
'''

class Player(object):
    '''
    Player class
    '''

    def __init__(self, name, reasearch_tree, planets=None, structures=None, units=None):
        '''
        Constructor
        '''
        self.name = name
        self.research_tree = reasearch_tree
        self.planets = planets
        self.structures = structures
        self.units = units
        