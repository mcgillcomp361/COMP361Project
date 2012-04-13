'''
Created on Jan 2, 2012

@author: Bazibaz
'''
from constants import MINERAL_STARTING_AMOUNT, GRAVITY_ENGINE_STARTING_AMOUNT, MAX_NUMBER_OF_STRUCTURE, \
                    FORGE_BUILD_TIME, NEXUS_BUILD_TIME, EXTRACTOR_BUILD_TIME, PHYLON_BUILD_TIME, GENERATOR_CORE_BUILD_TIME, \
                    SWARM_BUILD_TIME, SWARM_MINERAL_COST, GLOBE_BUILD_TIME, GLOBE_MINERAL_COST, ANALYZER_BUILD_TIME, ANALYZER_MINERAL_COST, \
                    HORDE_BUILD_TIME, HORDE_MINERAL_COST, SPHERE_BUILD_TIME, SPHERE_MINERAL_COST, \
                    HIVE_BUILD_TIME, HIVE_MINERAL_COST, PLANETARIUM_BUILD_TIME, PLANETARIUM_MINERAL_COST, MATHEMATICA_BUILD_TIME, MATHEMATICA_MINERAL_COST, \
                    GRAVITY_ENGINE_BUILD_TIME, GRAVITY_ENGINE_MINERAL_COST, BLACK_HOLE_GENERATOR_BUILD_TIME, BLACK_HOLE_GENERATOR_MINERAL_COST, \
                    GENERATOR_CORE_RESOURCE_GENERATION_RATE, PHYLON_RESOURCE_GENERATION_RATE, EXTRACTOR_RESOURCE_GENERATION_RATE, \
                    PLANETARY_DEFENSE_I_BUILD_TIME, PLANETARY_DEFENSE_II_BUILD_TIME, PLANETARY_DEFENSE_III_BUILD_TIME, PLANETARY_DEFENSE_IV_BUILD_TIME
from structures import *
from units import *
from research import *
from direct.showbase import DirectObject
from graphicEngine import indicators

class Player(object):
    '''
    Player class
    '''
    
    building_complete_sound = None
    cannot_build_sound = None
    
    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.selected_planet = None
        self.selected_star = None
        self.selected_units = []
        self.planets = []
        self.structures = []
        self.units = []
        self.research = ResearchTree()
        self.color = Vec4(0, 0, 1, 1)
        self.minerals = MINERAL_STARTING_AMOUNT
        self.ge_amount = GRAVITY_ENGINE_STARTING_AMOUNT
        
        Player.building_complete_sound = base.loader.loadSfx("sound/effects/structures/building_complete.wav")
        Player.cannot_build_sound = base.loader.loadSfx("sound/effects/structures/cannot_build.wav")
    
    def addStructure(self, structure):
        '''
        Building a structure on the player's planet
        '''
        if self.selected_planet and self.selected_planet.activated and \
           self.selected_planet.player == self and self.selected_planet.task_structure_timer == None and \
           not self.selected_planet.hasStructure(structure) and self.selected_planet.getNumberOfStructures()<MAX_NUMBER_OF_STRUCTURE:
            if(structure == "forge"):
                self.selected_planet.task_structure_timer = taskMgr.doMethodLater(FORGE_BUILD_TIME, self._delayedConstructStructure, 'buildForge', extraArgs =[Forge, self.selected_planet], appendTask=True)
                self._showStructureProgress(FORGE_BUILD_TIME)
            elif(structure == "nexus"):
                self.selected_planet.task_structure_timer = taskMgr.doMethodLater(NEXUS_BUILD_TIME, self._delayedConstructStructure, 'buildNexus', extraArgs =[Nexus, self.selected_planet], appendTask=True)
                self._showStructureProgress(NEXUS_BUILD_TIME)
            elif(structure == "extractor" and self.selected_planet.hasStructure("phylon")==False  and self.selected_planet.hasStructure("generatorCore")==False):
                self.selected_planet.task_structure_timer = taskMgr.doMethodLater(EXTRACTOR_BUILD_TIME, self._delayedConstructStructure, 'buildExtractor', extraArgs =[Extractor, self.selected_planet], appendTask=True)
                self._showStructureProgress(EXTRACTOR_BUILD_TIME)
            elif(structure == "phylon" and self.research.getLevel() >= 2 and self.selected_planet.hasStructure("extractor")==False  and self.selected_planet.hasStructure("generatorCore")==False):
                self.selected_planet.task_structure_timer = taskMgr.doMethodLater(PHYLON_BUILD_TIME, self._delayedConstructStructure, 'buildPhylon', extraArgs =[Phylon, self.selected_planet], appendTask=True)
                self._showStructureProgress(PHYLON_BUILD_TIME)
            elif(structure == "generatorCore" and self.research.getLevel() >= 3 and self.selected_planet.hasStructure("extractor")==False  and self.selected_planet.hasStructure("phylon")==False):
                self.selected_planet.task_structure_timer = taskMgr.doMethodLater(GENERATOR_CORE_BUILD_TIME, self._delayedConstructStructure, 'buildGeneratorCore', extraArgs =[GeneratorCore, self.selected_planet], appendTask=True)
                self._showStructureProgress(GENERATOR_CORE_BUILD_TIME)
            elif(structure == "pd1" and self.selected_planet.hasStructure("pd2")==False and self.selected_planet.hasStructure("pd3")==False and self.selected_planet.hasStructure("pd4")==False):
                self.selected_planet.task_structure_timer = taskMgr.doMethodLater(PLANETARY_DEFENSE_I_BUILD_TIME, self._delayedConstructStructure, 'buildpd1', extraArgs =[PlanetaryDefenseI, self.selected_planet], appendTask=True)
                self._showStructureProgress(PLANETARY_DEFENSE_I_BUILD_TIME)
            elif(structure == "pd2" and self.research.getLevel() >= 2 and self.selected_planet.hasStructure("pd1")==False and self.selected_planet.hasStructure("pd3")==False and self.selected_planet.hasStructure("pd4")==False):
                self.selected_planet.task_structure_timer = taskMgr.doMethodLater(PLANETARY_DEFENSE_II_BUILD_TIME, self._delayedConstructStructure, 'buildpd2', extraArgs =[PlanetaryDefenseII, self.selected_planet], appendTask=True)
                self._showStructureProgress(PLANETARY_DEFENSE_II_BUILD_TIME)
            elif(structure == "pd3" and self.research.getLevel() >= 3 and self.selected_planet.hasStructure("pd1")==False and self.selected_planet.hasStructure("pd2")==False  and self.selected_planet.hasStructure("pd4")==False):
                self.selected_planet.task_structure_timer = taskMgr.doMethodLater(PLANETARY_DEFENSE_III_BUILD_TIME, self._delayedConstructStructure, 'buildpd3', extraArgs =[PlanetaryDefenseIII, self.selected_planet], appendTask=True)
                self._showStructureProgress(PLANETARY_DEFENSE_III_BUILD_TIME)
            elif(structure == "pd4" and self.research.getLevel() >= 4 and self.selected_planet.hasStructure("pd1")==False and self.selected_planet.hasStructure("pd2")==False  and self.selected_planet.hasStructure("pd3")==False):
                self.selected_planet.task_structure_timer = taskMgr.doMethodLater(PLANETARY_DEFENSE_IV_BUILD_TIME, self._delayedConstructStructure, 'buildpd4', extraArgs =[PlanetaryDefenseIV, self.selected_planet], appendTask=True)
                self._showStructureProgress(PLANETARY_DEFENSE_IV_BUILD_TIME)
            else:
                Player.cannot_build_sound.play()
        else:
            Player.cannot_build_sound.play()

    
    def _showStructureProgress(self, time):
        taskMgr.add(indicators.drawProgressBar, 'structureProgressBar', extraArgs =[self.selected_planet, time], appendTask=True)
    
    def _delayedConstructStructure(self, Structure, host_planet, task):
        structure = Structure(host_planet)
        self.structures.append(structure)
        host_planet.task_structure_timer = None
        Player.building_complete_sound.play()
        return task.done

    def addUnit(self, unit):
        '''
        constructing a unit using the forge
        '''
        
        if(self.selected_planet != None and self.selected_planet.activated == True and \
           self.selected_planet.player == self and self.selected_planet.task_unit_timer == None and \
           self.selected_planet.hasStructure("forge")):
            if(unit == "swarm" and self.minerals >= SWARM_MINERAL_COST):
                self.minerals = self.minerals - SWARM_MINERAL_COST
                self.selected_planet.task_unit_timer = taskMgr.doMethodLater(SWARM_BUILD_TIME, self._delayedConstructUnit, 'buildSwarm', extraArgs =[Swarm, self.selected_planet], appendTask=True)
                self._showUnitProgress(SWARM_BUILD_TIME)         
            elif(unit == "horde" and self.research.getLevel() >= 2 and self.minerals >= HORDE_MINERAL_COST):
                self.minerals = self.minerals - HORDE_MINERAL_COST
                self.selected_planet.task_unit_timer = taskMgr.doMethodLater(HORDE_BUILD_TIME, self._delayedConstructUnit, 'buildHorde', extraArgs =[Horde, self.selected_planet], appendTask=True)
                self._showUnitProgress(HORDE_BUILD_TIME)
            elif(unit == "hive" and self.research.getLevel() >= 3 and self.minerals >= HIVE_MINERAL_COST):
                self.minerals = self.minerals - HIVE_MINERAL_COST
                self.selected_planet.task_unit_timer = taskMgr.doMethodLater(HIVE_BUILD_TIME, self._delayedConstructUnit, 'buildHive', extraArgs =[Hive, self.selected_planet], appendTask=True)
                self._showUnitProgress(HIVE_BUILD_TIME)  
            elif(unit == "globe" and self.minerals >= GLOBE_MINERAL_COST):
                self.minerals = self.minerals - GLOBE_MINERAL_COST
                self.selected_planet.task_unit_timer = taskMgr.doMethodLater(GLOBE_BUILD_TIME, self._delayedConstructUnit, 'buildGlobe', extraArgs =[Globe, self.selected_planet], appendTask=True)
                self._showUnitProgress(GLOBE_BUILD_TIME)
            elif(unit == "sphere" and self.research.getLevel() >= 2 and self.minerals >= SPHERE_MINERAL_COST):
                self.minerals = self.minerals - SPHERE_MINERAL_COST
                self.selected_planet.task_unit_timer = taskMgr.doMethodLater(SPHERE_BUILD_TIME, self._delayedConstructUnit, 'buildSphere', extraArgs =[Sphere, self.selected_planet], appendTask=True)
                self._showUnitProgress(SPHERE_BUILD_TIME)  
            elif(unit == "planetarium" and self.research.getLevel() >= 3 and self.minerals >= PLANETARIUM_MINERAL_COST):
                self.minerals = self.minerals - PLANETARIUM_MINERAL_COST
                self.selected_planet.task_unit_timer = taskMgr.doMethodLater(PLANETARIUM_BUILD_TIME, self._delayedConstructUnit, 'buildPlanetarium', extraArgs =[Planetarium, self.selected_planet], appendTask=True)
                self._showUnitProgress(PLANETARIUM_BUILD_TIME)
            elif(unit == "analyzer" and self.minerals >= ANALYZER_MINERAL_COST):
                self.minerals = self.minerals - ANALYZER_MINERAL_COST
                self.selected_planet.task_unit_timer = taskMgr.doMethodLater(ANALYZER_BUILD_TIME, self._delayedConstructUnit, 'buildAnalyzer', extraArgs =[Analyzer, self.selected_planet], appendTask=True)
                self._showUnitProgress(ANALYZER_BUILD_TIME)
            elif(unit == "mathematica" and self.research.getLevel() >= 3 and self.minerals >= MATHEMATICA_MINERAL_COST):
                self.minerals = self.minerals - MATHEMATICA_MINERAL_COST
                self.selected_planet.task_unit_timer = taskMgr.doMethodLater(MATHEMATICA_BUILD_TIME, self._delayedConstructUnit, 'buildMathematica', extraArgs =[Mathematica, self.selected_planet], appendTask=True)
                self._showUnitProgress(MATHEMATICA_BUILD_TIME)
            elif(unit == "blackHoleGenerator" and self.research.getLevel() >= 4 and self.minerals >= BLACK_HOLE_GENERATOR_MINERAL_COST):
                self.minerals = self.minerals - BLACK_HOLE_GENERATOR_MINERAL_COST
                self.selected_planet.task_unit_timer = taskMgr.doMethodLater(BLACK_HOLE_GENERATOR_BUILD_TIME, self._delayedConstructUnit, 'buildBlackHoleGenerator', extraArgs =[BlackHoleGenerator, self.selected_planet], appendTask=True)
                self._showUnitProgress(BLACK_HOLE_GENERATOR_BUILD_TIME)
            elif(unit == "gravityEngine" and self.research.getLevel() >= 2 and self.minerals >= GRAVITY_ENGINE_MINERAL_COST):
                self.minerals = self.minerals - GRAVITY_ENGINE_MINERAL_COST
                self.selected_planet.task_unit_timer = taskMgr.doMethodLater(GRAVITY_ENGINE_BUILD_TIME, self._delayedConstructGravityEngine, 'buildGravityEngine', extraArgs =[self.selected_planet], appendTask=True)
                self._showUnitProgress(GRAVITY_ENGINE_BUILD_TIME)
            else:
                Player.cannot_build_sound.play()
            from gameEngine.gameEngine import updateGUI
            updateGUI.refreshResources()
            updateGUI.value = self.minerals
            updateGUI.printResources()
        else:
            Player.cannot_build_sound.play()
    
    def _showUnitProgress(self, time):
        taskMgr.add(indicators.drawUnitProgressBar, 'unitProgressBar', extraArgs =[self.selected_planet, time], appendTask=True)
    
    def _delayedConstructUnit(self, Unit, planet, task):
        unit = Unit(planet, self)
        unit.startOrbit()
        self.units.append(unit)
        planet.task_unit_timer = None
        return task.done
        
    def _delayedConstructGravityEngine(self, planet, task):
        self.ge_amount = self.ge_amount + 1
        from gameEngine.gameEngine import updateGUI
        updateGUI.refreshGE()
        updateGUI.value = self.ge_amount
        updateGUI.printGE()
        planet.task_unit_timer = None
        return task.done
        
    def trackMinerals(self, task):
#        print "structures : " + str(len(self.structures))
#        print "units : " + str(len(self.units))
#        print "selected units : " + str(len(self.selected_units))
        for structure in self.structures:
            if(type(structure) == Extractor):
                self.minerals = self.minerals + EXTRACTOR_RESOURCE_GENERATION_RATE
            elif(type(structure) == Phylon):
                self.minerals = self.minerals + PHYLON_RESOURCE_GENERATION_RATE
            elif(type(structure) == GeneratorCore):
                self.minerals = self.minerals + GENERATOR_CORE_RESOURCE_GENERATION_RATE
            from gameEngine.gameEngine import updateGUI
            updateGUI.refreshResources()
            updateGUI.value = self.minerals
            updateGUI.printResources()
        return task.again
    
    def hasCaptureTypeUnit(self):
        ''' TODO : player has researched the abilitiy '''
        for unit in self.units:
            if(type(unit) == Swarm or type(unit) == Horde or type(unit) == Hive):
                return True
        return False
        
    def getNumberOfNexus(self):
        number = 0
        for structure in self.structures:
            if(type(structure)==Nexus):
                number = number + 1
        return number 

#    def removePlanetFromPlanets(self, dead_planet):
#        for planet in self.planets:
#            if(dead_planet == planet):
#                self.planets.remove(dead_planet)
#                return
            