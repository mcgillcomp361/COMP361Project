'''
Created on Dec 29, 2011

@author: Eran-Tasker
'''
from panda3d.core import Point3

class Unit(object):
    '''
    classdocs
    '''


    def __init__(self, _host_planet):
        '''
        Constructor
        '''
        self._energy = 0
        self._damage = 0
        self._host_planet = _host_planet
        self._position = Point3(0, 0, 0)
        self._velocity = 0;
        self._unit_abilities = []
        self._deep_space = False
        
    def Unit(self, name, _host_planet):
        self._host_planet = _host_planet
        
    def setAbilities(self, abilities):
        self._unit_abilities.extend(abilities)
        
    def getAbilities(self):
        return self._unit_abilities
        
    def set_energy(self, _energy):
        self._energy = _energy
        
    def get_energy(self):
        return self._energy
    
    def set_damage(self, _damage):
        self._damage = _damage
        
    def get_damage(self):
        return self._damage
    
    def setHostPlanet(self,_host_planet):
        self._host_planet = _host_planet
        return self._host_planet == _host_planet
        
    def getHostPlanet(self):
        return self._host_planet
    
    def useAbility(self, ability):
        'Fill in code here'
        return True
        
    def destroyUnit(self):
        'Please double check this'
        self._energy = 0
        self._damage = 0
        self._host_planet = None
        self._position = Point3(0, 0, 0)
        self._velocity = 0;
        self._unit_abilities = []
        self._deep_space = False
        self = None
        
    def attack(self):
        'To do later'
        
    def set_velocity(self,velo):
        self._velocity = velo
        
    def get_velocity(self):
        return self._velocity
    
    def setDeepSpace(self, bol):
        self._deep_space = bol
        
    def getDeapSpace(self):
        return self._deep_space
    
    def set_position(self, pos):
        self._position = pos
        
    def get_position(self):
        return self._position