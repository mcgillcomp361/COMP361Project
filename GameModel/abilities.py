'''
Created on Dec 29, 2011

@author: Bazibaz
'''

class Ability(object):
    '''
    This class contains the attributes to an ability for a given unit.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.cool_down = 0 #Amount of time needed to use the ability again (in seconds)
        self.damage = 0 #Amount of damage
        self.used = False #Prevents the same ability from being used successively.