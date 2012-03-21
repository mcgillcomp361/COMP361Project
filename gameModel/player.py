'''
Created on Jan 2, 2012

@author: Bazibaz
'''
from constants import MINERAL_STARTING_AMOUNT, GRAVITY_ENGINE_STARTING_AMOUNT, \
                    FORGE_BUILD_TIME, NEXUS_BUILD_TIME, EXTRACTOR_BUILD_TIME, PHYLON_BUILD_TIME, GENERATOR_CORE_BUILD_TIME, \
                    SWARM_BUILD_TIME, SWARM_MINERAL_COST, \
                    HORDE_BUILD_TIME, HORDE_MINERAL_COST, \
                    HIVE_BUILD_TIME, HIVE_MINERAL_COST
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
        
    ''' TODO: use Multi-Texturing '''
    ''' TODO: add different units, units have different models and animations '''
    ''' TODO: complete all the condition checks(e.g. tech tier, existent structure, ...) '''
    
    def addStructure(self, structure):
        '''
        Building a structure on the player's planet
        '''
        if(self.selected_planet != None and self.selected_planet.activated == True and \
           self.selected_planet.player == self and self.selected_planet.task_structure_timer == None and \
           self.selected_planet.hasStructure(structure) == False):
            if(structure == "forge"):
                self.selected_planet.task_structure_timer = taskMgr.doMethodLater(1, self._constructForge, 'buildForge', extraArgs =[self.selected_planet], appendTask=True)
            elif(structure == "nexus"):
                self.selected_planet.task_structure_timer = taskMgr.doMethodLater(NEXUS_BUILD_TIME, self._constructNexus, 'buildNexus', extraArgs =[self.selected_planet], appendTask=True)
            elif(structure == "extractor" and self.selected_planet.hasStructure("phylon") == False and self.selected_planet.hasStructure("generatorCore") == False):
                self.selected_planet.task_structure_timer = taskMgr.doMethodLater(EXTRACTOR_BUILD_TIME, self._constructExtractor, 'buildExtractor', extraArgs =[self.selected_planet], appendTask=True)
            elif(structure == "phylon" and self.selected_planet.hasStructure("generatorCore") == False):
                self.selected_planet.task_structure_timer = taskMgr.doMethodLater(PHYLON_BUILD_TIME, self._constructPhylon, 'buildPhylon', extraArgs =[self.selected_planet], appendTask=True)
            elif(structure == "generatorCore"):
                self.selected_planet.task_structure_timer = taskMgr.doMethodLater(GENERATOR_CORE_BUILD_TIME, self._constructGeneratorCore, 'buildGeneratorCore', extraArgs =[self.selected_planet], appendTask=True)

    def _constructForge(self, planet, task):
            forge = Forge(planet)
            self.structures.append(forge)
            planet.task_structure_timer = None
            return task.done

    def _constructNexus(self, planet, task):
            nexus = Nexus(planet)
            self.structures.append(nexus)
            planet.task_structure_timer = None
            return task.done
    
    def _constructExtractor(self, planet, task):
            extractor = Extractor(planet)
            self.structures.append(extractor)
            planet.task_structure_timer = None
            return task.done
    
    def _constructPhylon(self, planet, task):
            phylon = Phylon(planet)
            self.structures.append(phylon)
            planet.task_structure_timer = None
            return task.done
    
    def _constructGeneratorCore(self, planet, task):
            generatorCore = GeneratorCore(planet)
            self.structures.append(generatorCore)
            planet.task_structure_timer = None
            return task.done
      
    def addUnit(self, unit):
        '''
        constructing a unit using the forge
        '''
        
        if(self.selected_planet != None and self.selected_planet.activated == True and \
           self.selected_planet.player == self and self.selected_planet.task_unit_timer == None and \
           self.selected_planet.hasStructure("forge")):
            if(unit == "swarm" and self.minerals > SWARM_MINERAL_COST):
                self.minerals = self.minerals - SWARM_MINERAL_COST
#               taskMgr.add(host_planet.drawConnections, 'DrawConnections')
                self.selected_planet.task_unit_timer = taskMgr.doMethodLater(1, self._constructSwarm, 'buildSwarm', extraArgs =[self.selected_planet], appendTask=True)         
            elif(unit == "horde" and self.minerals > HORDE_MINERAL_COST):
                self.minerals = self.minerals - HORDE_MINERAL_COST
#               taskMgr.add(host_planet.drawConnections, 'DrawConnections')
                self.selected_planet.task_unit_timer = taskMgr.doMethodLater(1, self._constructHorde, 'buildHorde', extraArgs =[self.selected_planet], appendTask=True)
            elif(unit == "hive" and self.minerals > HIVE_MINERAL_COST):
                self.minerals = self.minerals - HIVE_MINERAL_COST
#               taskMgr.add(host_planet.drawConnections, 'DrawConnections')
                self.selected_planet.task_unit_timer = taskMgr.doMethodLater(1, self._constructHive, 'buildHive', extraArgs =[self.selected_planet], appendTask=True)
            from gameEngine.gameEngine import updateGUI
            updateGUI.refreshResources()
            updateGUI.value = self.minerals
            updateGUI.printResources()

    def _constructSwarm(self, planet, task):
            swarm = Swarm(planet, self)
            swarm.startOrbit()
            self.units.append(swarm)
            planet.task_unit_timer = None
            return task.done
        
    def _constructHorde(self, planet, task):
            horde = Horde(planet, self)
            horde.startOrbit()
            self.units.append(horde)
            planet.task_unit_timer = None
            return task.done
        
    def _constructHive(self, planet, task):
            hive = Hive(planet, self)
            hive.startOrbit()
            self.units.append(hive)
            planet.task_unit_timer = None
            return task.done
    