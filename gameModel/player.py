'''
Created on Jan 2, 2012

@author: Bazibaz
'''
from constants import MINERAL_STARTING_AMOUNT, GRAVITY_ENGINE_STARTING_AMOUNT, \
                    FORGE_BUILD_TIME, NEXUS_BUILD_TIME, EXTRACTOR_BUILD_TIME, PHYLON_BUILD_TIME, GENERATOR_CORE_BUILD_TIME, \
                    SWARM_BUILD_TIME, SWARM_MINERAL_COST
from structures import *
from units import *

class Player(object):
    '''
    Player class
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.selected_planet = None
        self.selected_star = None
        self.selecteUnit = None
        self.selectedUnits = []
        self.planets = []
        self.structures = []
        self.units = []
        self.minerals = MINERAL_STARTING_AMOUNT
        self.ge_amount = GRAVITY_ENGINE_STARTING_AMOUNT
        
    ''' TODO: only one task can be running at a planet, check for that so in other words a timer should not be running '''
    ''' TODO: check duplicates of structures '''
    ''' TODO: use Multi-Texturing '''
    ''' TODO: add different units, units have different models and animations '''
    
    def addStructure(self, structure):
        '''
        Building a structure on the player's planet
        '''
        if(self.selected_planet != None and self.selected_planet.player == self):
            if(structure == "forge"):
                self.selected_planet.task_timer = taskMgr.doMethodLater(FORGE_BUILD_TIME, self._constructForge, 'buildForge', extraArgs =[self.selected_planet], appendTask=True)
            elif(structure == "nexus"):
                self.selected_planet.task_timer = taskMgr.doMethodLater(NEXUS_BUILD_TIME, self._constructNexus, 'buildNexus', extraArgs =[self.selected_planet], appendTask=True)
            elif(structure == "extractor"):
                self.selected_planet.task_timer = taskMgr.doMethodLater(EXTRACTOR_BUILD_TIME, self._constructExtractor, 'buildExtractor', extraArgs =[self.selected_planet], appendTask=True)
            elif(structure == "phylon"):
                self.selected_planet.task_timer = taskMgr.doMethodLater(PHYLON_BUILD_TIME, self._constructPhylon, 'buildPhylon', extraArgs =[self.selected_planet], appendTask=True)
            elif(structure == "generatorCore"):
                self.selected_planet.task_timer = taskMgr.doMethodLater(GENERATOR_CORE_BUILD_TIME, self._constructGeneratorCore, 'buildGeneratorCore', extraArgs =[self.selected_planet], appendTask=True)

    def _constructForge(self, planet, task):
            forge = Forge(planet)
            self.structures.append(forge)
            return task.done
      
    def _constructNexus(self, planet, task):
            nexus = Nexus(planet)
            self.structures.append(nexus)
            return task.done
    
    def _constructExtractor(self, planet, task):
            extractor = Extractor(planet)
            self.structures.append(extractor)
            return task.done
    
    def _constructPhylon(self, planet, task):
            phylon = Phylon(planet)
            self.structures.append(phylon)
            return task.done
    
    def _constructGeneratorCore(self, planet, task):
            generatorCore = GeneratorCore(planet)
            self.structures.append(generatorCore)
            return task.done
      
    def addUnit(self, unit):
        '''
        constructing a unit using the forge
        '''
        
        ''' TODO: check for forge to be present on the planet'''
        
        if(self.selected_planet != None and self.selected_planet.player == self):
            if(unit == "swarm" and self.minerals > SWARM_MINERAL_COST):
                self.minerals = self.minerals - SWARM_MINERAL_COST
#               taskMgr.add(host_planet.drawConnections, 'DrawConnections')
                self.selected_planet.task_timer = taskMgr.doMethodLater(SWARM_BUILD_TIME, self._constructSwarm, 'buildSwarm', extraArgs =[self.selected_planet], appendTask=True)                
            from gameEngine.gameEngine import updateGUI
            updateGUI.refreshResources()
            updateGUI.value = self.minerals
            updateGUI.printResources()

    def _constructSwarm(self, planet, task):
            swarm = Swarm(planet, self)
            swarm.startOrbit()
            self.units.append(swarm)
            return task.done
    