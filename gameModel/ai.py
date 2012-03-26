'''
Created on March 25, 2012

@author: Bazibaz
'''
from constants import MINERAL_STARTING_AMOUNT, GRAVITY_ENGINE_STARTING_AMOUNT, AI_MINERAL_STARTING_AMOUNT, AI_GRAVITY_ENGINE_STARTING_AMOUNT, \
                    FORGE_BUILD_TIME, NEXUS_BUILD_TIME, EXTRACTOR_BUILD_TIME, PHYLON_BUILD_TIME, GENERATOR_CORE_BUILD_TIME, \
                    SWARM_BUILD_TIME, SWARM_MINERAL_COST, GLOBE_BUILD_TIME, GLOBE_MINERAL_COST, ANALYZER_BUILD_TIME, ANALYZER_MINERAL_COST, \
                    HORDE_BUILD_TIME, HORDE_MINERAL_COST, SPHERE_BUILD_TIME, SPHERE_MINERAL_COST, \
                    HIVE_BUILD_TIME, HIVE_MINERAL_COST, PLANETARIUM_BUILD_TIME, PLANETARIUM_MINERAL_COST, MATHEMATICA_BUILD_TIME, MATHEMATICA_MINERAL_COST, \
                    BLACK_HOLE_GENERATOR_BUILD_TIME, BLACK_HOLE_GENERATOR_MINERAL_COST, MAX_NUMBER_OF_STRUCTURE, \
                    NUMBER_OF_STARS, MAX_NUMBER_OF_PLANETS, AI_ACTIVATE_PLANET_WAIT_TIME, AI_START_CONSTRUCTION_WAIT_TIME, AI_MAX_NUMBER_OF_UNITS, AI_ACCELERATION_TIME
from structures import *
from units import *
from solar import *
import random

'''TODO : add mineral and gravity engine functionality to the AI agent '''
'''TODO : make a list of timers for unit and structure construction for planet since the AI builds 
        everything at the same time unlike the player '''        

class AI(object):
    '''
    Artificial opponent class
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.planets = []
        self.orbit = 0
        self.structures = []
        self.units = []
        self.assault_party = []
        self.defense_party = []
        self.minerals = AI_MINERAL_STARTING_AMOUNT
        self.ge_amount = AI_GRAVITY_ENGINE_STARTING_AMOUNT
        self.all_stars = []
        
    def activateRandomStar(self, all_stars):
        self.all_stars = all_stars
        if(self._allStarsActivated(self.all_stars) == False):    
            while(True):
                star = self.all_stars[random.randrange(0, NUMBER_OF_STARS, 1)]
                if not star.activated:
                    star.activateStar(self)
                    orbit = 0
                    task = taskMgr.doMethodLater(AI_ACTIVATE_PLANET_WAIT_TIME - AI_ACCELERATION_TIME*MAX_NUMBER_OF_PLANETS, self._activatePlanetsLoop, 'AIactivatePlanet', extraArgs =[orbit, star], appendTask=True)
                    break
    
    def _activatePlanetsLoop(self, orbit, star, task):
        if(self._allPlanetsActivated(star) == True):
            self.activateRandomStar(self.all_stars)
        else:
            self._activatePlanet(star.getPlanetAt(orbit))   
            orbit = orbit + 1
            task = taskMgr.doMethodLater(AI_ACTIVATE_PLANET_WAIT_TIME - AI_ACCELERATION_TIME*orbit, self._activatePlanetsLoop, 'AIactivatePlanet', extraArgs =[orbit, star], appendTask=True)
        
    def _activatePlanet(self, planet):
        if(planet.activated == False):
            planet.activatePlanet(self)
            self._startConstruction(planet, None)
            
    def _startConstruction(self, planet, task):
        if(planet.player == self):
            structureType = random.randrange(1, 5, 1)
            if(planet.hasStructure("forge")==False and planet.task_structure_timer==None):
                ''' Build Forge at all times '''
                planet.task_structure_timer = taskMgr.doMethodLater(FORGE_BUILD_TIME, self._constructForge, 'AIbuildForge', extraArgs =[planet], appendTask=True)
            if(structureType == 1 and planet.hasStructure("nexus")==False and planet.task_structure_timer==None):
                planet.task_structure_timer = taskMgr.doMethodLater(NEXUS_BUILD_TIME, self._constructNexus, 'AIbuildNexus', extraArgs =[planet], appendTask=True)
            elif(structureType == 2 and planet.hasStructure("extractor")==False and planet.hasStructure("phylon")==False and planet.hasStructure("generatorCore")==False and planet.task_structure_timer==None):
                planet.task_structure_timer = taskMgr.doMethodLater(EXTRACTOR_BUILD_TIME, self._constructExtractor, 'AIbuildExtractor', extraArgs =[planet], appendTask=True)
            elif(structureType == 3 and planet.hasStructure("phylon")==False and planet.hasStructure("generatorCore")==False and planet.task_structure_timer==None):
                planet.task_structure_timer = taskMgr.doMethodLater(PHYLON_BUILD_TIME, self._constructPhylon, 'AIbuildPhylon', extraArgs =[planet], appendTask=True)
            elif(structureType == 4 and planet.hasStructure("generatorCore")==False and planet.task_structure_timer==None):
                planet.task_structure_timer = taskMgr.doMethodLater(GENERATOR_CORE_BUILD_TIME, self._constructGeneratorCore, 'AIbuildGeneratorCore', extraArgs =[planet], appendTask=True)
            if(planet.hasStructure("forge")==True):
                unit_type = random.randrange(0, 100, 1)
                if(0 <= unit_type and unit_type < 60):
                    ''' 60% chance of constructing units of tier I '''
                    self._constructUnitTierI(planet, None)
                elif(60 <= unit_type and unit_type < 90):
                    ''' 30% chance of constructing units of tier II '''
                    self._constructUnitTierII(planet, None)
                elif(90 <= unit_type and unit_type < 100):
                    ''' 10% chance of constructing units of tier III '''
                    self._constructUnitTierIII(planet, None)
                if(planet.getNumberOfStructures() >= 2):
                    return task.done
            else:
                new_task = taskMgr.doMethodLater(1, self._startConstruction, 'AIstartConstruction', extraArgs =[planet], appendTask=True)

    def _constructForge(self, planet, task):
        forge = Forge(planet)
        self.structures.append(forge)
        planet.task_structure_timer=None
        return task.done
        
    def _constructNexus(self, planet, task):
        nexus = Nexus(planet)
        self.structures.append(nexus)
        planet.task_structure_timer=None
        return task.done
        
    def _constructExtractor(self, planet, task):
        extractor = Extractor(planet)
        self.structures.append(extractor)
        planet.task_structure_timer=None
        return task.done
    
    def _constructPhylon(self, planet, task):
        phylon = Phylon(planet)
        self.structures.append(phylon)
        planet.task_structure_timer=None
        return task.done
    
    def _constructGeneratorCore(self, planet, task):
        generatorCore = GeneratorCore(planet)
        self.structures.append(generatorCore)
        planet.task_structure_timer=None
        return task.done
    
    def _constructUnitTierI(self, planet, task):
        unit_type = random.randrange(0, 3, 1)
        if(unit_type == 0 and planet.task_unit_timer == None):
            planet.task_unit_timer =  taskMgr.doMethodLater(SWARM_BUILD_TIME, self._constructSwarm, 'AIbuildSwarm', extraArgs =[planet], appendTask=True)
        elif(unit_type == 1 and planet.task_unit_timer == None):
            planet.task_unit_timer =  taskMgr.doMethodLater(GLOBE_BUILD_TIME, self._constructSphere, 'AIbuildGlobe', extraArgs =[planet], appendTask=True)
        elif(unit_type == 2 and planet.task_unit_timer == None):
            planet.task_unit_timer =  taskMgr.doMethodLater(ANALYZER_BUILD_TIME, self._constructSphere, 'AIbuildGlobe', extraArgs =[planet], appendTask=True)  
        if(planet.getNumberOfUnits() >= AI_MAX_NUMBER_OF_UNITS):
            return task.done
        else:
            new_task = taskMgr.doMethodLater(1, self._constructUnitTierI, 'AIconstructUnitTierI', extraArgs =[planet], appendTask=True)
            
    def _constructUnitTierII(self, planet, task):
        unit_type = random.randrange(0, 3, 1)
        if(unit_type == 0):
            planet.task_unit_timer = taskMgr.doMethodLater(HORDE_BUILD_TIME, self._constructHorde, 'AIbuildHorde', extraArgs =[planet], appendTask=True)
        elif(unit_type == 1):
            planet.task_unit_timer =  taskMgr.doMethodLater(SPHERE_BUILD_TIME, self._constructSphere, 'AIbuildSphere', extraArgs =[planet], appendTask=True)
        elif(unit_type == 2):
            '''since TierII contains 2 units, an additional swarm is added here '''
            planet.task_unit_timer =  taskMgr.doMethodLater(SWARM_BUILD_TIME, self._constructSwarm, 'AIbuildSwarm', extraArgs =[planet], appendTask=True) 
        if(planet.getNumberOfUnits() >= AI_MAX_NUMBER_OF_UNITS-1):
            return task.done
        else:
            new_task = taskMgr.doMethodLater(1, self._constructUnitTierII, 'AIconstructUnitTierII', extraArgs =[planet], appendTask=True)
            
    def _constructUnitTierIII(self, planet, task):
        unit_type = random.randrange(0, 3, 1)
        if(unit_type == 0):
            planet.task_unit_timer =  taskMgr.doMethodLater(HIVE_BUILD_TIME, self._constructHive, 'AIbuildHive', extraArgs =[planet], appendTask=True)
        elif(unit_type == 1):
            planet.task_unit_timer =  taskMgr.doMethodLater(PLANETARIUM_BUILD_TIME, self._constructPlanetarium, 'AIbuildPlanetarium', extraArgs =[planet], appendTask=True)
        elif(unit_type == 2):
            planet.task_unit_timer =  taskMgr.doMethodLater(MATHEMATICA_BUILD_TIME, self._constructMathematica, 'AIbuildMathematica', extraArgs =[planet], appendTask=True)  
        if(planet.getNumberOfUnits() >= AI_MAX_NUMBER_OF_UNITS-2):
            return task.done
        else:
            new_task = taskMgr.doMethodLater(1, self._constructUnitTierIII, 'AIconstructUnitTierIII', extraArgs =[planet], appendTask=True)

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
    
    def _constructGlobe(self, planet, task):
        globe = Globe(planet, self)
        globe.startOrbit()
        self.units.append(globe)
        planet.task_unit_timer = None
        return task.done
    
    def _constructSphere(self, planet, task):
        sphere = Sphere(planet, self)
        sphere.startOrbit()
        self.units.append(sphere)
        planet.task_unit_timer = None
        return task.done
        
    def _constructPlanetarium(self, planet, task):
        planetarium = Planetarium(planet, self)
        planetarium.startOrbit()
        self.units.append(planetarium)
        planet.task_unit_timer = None
        return task.done
    
    def _constructAnalyzer(self, planet, task):
        analyzer = Analyzer(planet, self)
        analyzer.startOrbit()
        self.units.append(analyzer)
        planet.task_unit_timer = None
        return task.done   
            
    def _constructMathematica(self, planet, task):
        mathematica = Mathematica(planet, self)
        mathematica.startOrbit()
        self.units.append(mathematica)
        planet.task_unit_timer = None
        return task.done
        
    def _constructBlackHoleGenerator(self, planet, task):
        blackHoleGenerator = BlackHoleGenerator(planet, self)
        blackHoleGenerator.startOrbit()
        self.units.append(blackHoleGenerator)
        planet.task_unit_timer = None
        return task.done
   
    def _allStarsActivated(self, all_star):
        for star in all_star:
            if(star.activated == False):
                return False
        return True
    
    def _allPlanetsActivated(self, star):
        for planet in star.planets():
            if(planet.activated == False):
                return False
        return True
    