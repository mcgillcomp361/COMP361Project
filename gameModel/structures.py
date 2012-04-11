'''
Created on 7 Jan. 2012

@author: Bazibaz
'''
from abc import ABCMeta, abstractmethod
from constants import FORGE_MAX_ENERGY, NEXUS_MAX_ENERGY, EXTRACTOR_MAX_ENERGY, PHYLON_MAX_ENERGY,\
GENERATOR_CORE_MAX_ENERGY, PLANETARY_DEFENSE_I_MAX_ENERGY, PLANETARY_DEFENSE_I_DAMAGE, PLANETARY_DEFENSE_II_MAX_ENERGY,\
PLANETARY_DEFENSE_II_DAMAGE, PLANETARY_DEFENSE_III_MAX_ENERGY, PLANETARY_DEFENSE_III_DAMAGE,\
 PLANETARY_DEFENSE_IV_MAX_ENERGY, PLANETARY_DEFENSE_IV_DAMAGE
from panda3d.core import Vec3, Vec4
from pandac.PandaModules import TransparencyAttrib
_default_energy = 0

''' TODO : add the planet defence model and functionality '''

class Structure(object):
    __metaclass__ = ABCMeta
    '''
    Contains the general information for structures.
    '''
    
    @abstractmethod
    def __init__(self, energy, host_planet):
        '''
        Constructor
        @param energy: Structure's energy
        @param host_planet : The planet where the structure is constructed on
        '''
        self.energy = energy
        self.host_planet = host_planet
        self.host_planet.addSurfaceStructure(self)
        
#        self.model_path = loader.loadModel("models/planets/torus")       
#        self.model_path.reparentTo(self.host_planet.model_path)
#        self.model_path.setScale(1.0)
#        self.model_path.setSx(0.45)
#        self.model_path.setSy(0.45)
#        self.model_path.setSz(0.7)
        
class Forge(Structure):
    '''
    Subclass of Structure that focuses on production of units of all Tiers.
    @param host_planet : The planet where the structure is constructed on
    '''
    
    def __init__(self, host_planet):
        '''
        Constructor
        '''
        super(Forge, self).__init__(FORGE_MAX_ENERGY, host_planet)
        self._units_in_construction = [] #Queue for units waiting to be trained.
        self.host_planet.setTexture("forge")
        
##        self.model_path.setTextureOff()
#        self.model_path.setColor(Vec4(0.99, 0.12, 0.10, 0.8))
#        self.model_path.setTransparency(TransparencyAttrib.MAlpha)
        
    '''TODO : manage build time '''
    def addToConstructionQueue(self, unit): 
        self._units_in_construction.append(unit)
        
    def removeFromConstructionQueue(self):
        return self._units_in_construction.pop()


class Nexus(Structure):
    '''
    Subclass of Structure that unlocks the evolution tree and speeds up evolution by NEXUS_RESEARCH_INCREASE_RATE.
    Kept track by the Game Engine
    '''
    
    def __init__(self, host_planet):
        '''
        Constructor
        @param host_planet : The planet where the structure is constructed on
        '''
        super(Nexus, self).__init__(NEXUS_MAX_ENERGY, host_planet)
        
        self.host_planet.setTexture("nexus")
        
#        self.model_path.setPos(0,0,-0.2)
##        self.model_path.setTextureOff()
#        self.model_path.setColor(Vec4(0.1, 0.12, 0.99, 0.8))
#        self.model_path.setTransparency(TransparencyAttrib.MAlpha)


class Extractor(Structure):
    '''
    Subclass of Structure that focuses on Tier I mineral harvesting.
    Adds up EXTRACTOR_RESOURCE_GENERATION_RATE to mineral harvesting 
    Kept track by the Game Engine
    '''

    def __init__(self, host_planet):
        '''
        Constructor
        @param host_planet : The planet where the structure is constructed on
        '''
        super(Extractor, self).__init__(EXTRACTOR_MAX_ENERGY, host_planet)
        self.host_planet.setTexture("extractor")
#        self.model_path.setPos(0,0,0.2)
##        self.model_path.setTextureOff()
#        self.model_path.setColor(Vec4(0.1, 0.92, 0.29, 0.8))
#        self.model_path.setTransparency(TransparencyAttrib.MAlpha)


class Phylon(Structure):
    '''
    Subclass of Structure that focuses on Tier II mineral harvesting.
    Adds up PHYLON_RESOURCE_GENERATION_RATE to mineral harvesting 
    Kept track by the Game Engine
    '''

    def __init__(self, host_planet):
        '''
        Constructor
        @param host_planet : The planet where the structure is constructed on
        '''
        super(Phylon, self).__init__(PHYLON_MAX_ENERGY, host_planet)
        self.host_planet.setTexture("phylon")
#        self.model_path.setPos(0,0,0.4)
##        self.model_path.setTextureOff()
#        self.model_path.setColor(Vec4(0.9, 0.12, 0.99, 0.8))
#        self.model_path.setTransparency(TransparencyAttrib.MAlpha)


class GeneratorCore(Structure):
    '''
    Subclass of Structure that focuses on Tier III mineral harvesting.
    Adds up GENERATOR_CORE_RESOURCE_GENERATION_RATE to mineral harvesting 
    Kept track by the Game Engine
    '''

    def __init__(self, host_planet):
        '''
        Constructor
        @param host_planet : The planet where the structure is constructed on
        '''
        super(GeneratorCore, self).__init__(GENERATOR_CORE_MAX_ENERGY, host_planet) 
        self.host_planet.setTexture("generatorCore")
#        self.model_path.setPos(0,0,-0.4)
##        self.model_path.setTextureOff()
#        self.model_path.setColor(Vec4(0.1, 0.92, 0.99, 0.8))
#        self.model_path.setTransparency(TransparencyAttrib.MAlpha)

               
class PlanetaryDefenseI(Structure):
    '''
    Subclass of Structure that focuses on Tier I defense systems.
    '''

    def __init__(self, host_planet):
        '''
        Constructor
        @param host_planet : The planet where the structure is constructed on
        '''
        super(PlanetaryDefenseI, self).__init__(PLANETARY_DEFENSE_I_MAX_ENERGY, host_planet)
        self.damage = PLANETARY_DEFENSE_I_DAMAGE


class PlanetaryDefenseII(Structure):
    '''
    Subclass of Structure that focuses on Tier II defense systems.
    '''

    def __init__(self, host_planet):
        '''
        Constructor
        @param host_planet : The planet where the structure is constructed on
        '''
        super(PlanetaryDefenseII, self).__init__(PLANETARY_DEFENSE_II_MAX_ENERGY, host_planet)
        self.damage = PLANETARY_DEFENSE_II_DAMAGE


class PlanetaryDefenseIII(Structure):
    '''
    Subclass of Structure that focuses on Tier III defense systems.
    '''

    def __init__(self, host_planet):
        '''
        Constructor
        @param host_planet : The planet where the structure is constructed on
        '''
        super(PlanetaryDefenseIII, self).__init__(PLANETARY_DEFENSE_III_MAX_ENERGY, host_planet)
        self.damage = PLANETARY_DEFENSE_III_DAMAGE        


class PlanetaryDefenseIV(Structure):
    '''
    Subclass of Structure that focuses on Tier IV defense systems.
    '''

    def __init__(self, host_planet):
        '''
        Constructor
        @param host_planet : The planet where the structure is constructed on
        '''
        super(PlanetaryDefenseIV, self).__init__(PLANETARY_DEFENSE_IV_MAX_ENERGY, host_planet)
        self.damage = PLANETARY_DEFENSE_IV_DAMAGE