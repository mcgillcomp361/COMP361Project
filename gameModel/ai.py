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
                    NUMBER_OF_STARS, MAX_NUMBER_OF_PLANETS, AI_ACTIVATE_PLANET_WAIT_TIME, AI_START_CONSTRUCTION_WAIT_TIME, AI_MAX_NUMBER_OF_UNITS, AI_ACCELERATION_TIME, AI_UNIT_CONSTRUCTION_WAIT_TIME
from structures import *
from units import *
from solar import *
import random

'''TODO : construct different strategy routines for the AI agent : assault, defence, evacuate '''      

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
        if(planet.activated == False and planet != None):
            planet.activatePlanet(self)
            if(planet.player == self):#for extra check
                task_structure_timer = taskMgr.doMethodLater(AI_START_CONSTRUCTION_WAIT_TIME, self._startConstruction, 'AIbuildForge', extraArgs =[planet], appendTask=True)
                planet.task_structure_timers.append(task_structure_timer)

    def _startConstruction(self, planet, task):
        if(planet.player == self and planet.parent_star.lifetime > 0):
            if(planet.hasStructure("forge")==False):
                self._constructForge(planet)
                planet.task_structure_timers.remove(task)

            structureType = random.randrange(1, 5, 1)
            if(structureType == 1 and planet.hasStructure("nexus")==False):
                task_structure_timer = taskMgr.doMethodLater(NEXUS_BUILD_TIME, self._constructNexus, 'AIbuildNexus', extraArgs =[planet], appendTask=True)
            elif(structureType == 2 and planet.hasStructure("extractor")==False and planet.hasStructure("phylon")==False and planet.hasStructure("generatorCore")==False):
                task_structure_timer = taskMgr.doMethodLater(EXTRACTOR_BUILD_TIME, self._constructExtractor, 'AIbuildExtractor', extraArgs =[planet], appendTask=True)
            elif(structureType == 3 and planet.hasStructure("phylon")==False and planet.hasStructure("generatorCore")==False):
                task_structure_timer = taskMgr.doMethodLater(PHYLON_BUILD_TIME, self._constructPhylon, 'AIbuildPhylon', extraArgs =[planet], appendTask=True)
            elif(structureType == 4 and planet.hasStructure("generatorCore")==False):
                task_structure_timer = taskMgr.doMethodLater(GENERATOR_CORE_BUILD_TIME, self._constructGeneratorCore, 'AIbuildGeneratorCore', extraArgs =[planet], appendTask=True)
            planet.task_structure_timers.append(task_structure_timer)
            
            '''TODO : construct defensive structures '''
            
            if(planet.getNumberOfUnits(self) < AI_MAX_NUMBER_OF_UNITS):
                unit_type = random.randrange(0, 100, 1)
                if(0 <= unit_type and unit_type < 60):
                    ''' 60% chance of constructing units of tier I '''
                    self._constructUnitTierI(planet, 0, None)
                elif(60 <= unit_type and unit_type < 90):
                    ''' 30% chance of constructing units of tier II '''
                    self._constructUnitTierII(planet, 0, None)
                elif(90 <= unit_type and unit_type < 100):
                    ''' 10% chance of constructing units of tier III '''
                    self._constructUnitTierIII(planet, 0, None)

            return task.done

    def _constructForge(self, planet):
        forge = Forge(planet)
        self.structures.append(forge)
        
    def _constructNexus(self, planet, task):
        nexus = Nexus(planet)
        self.structures.append(nexus)
        planet.task_structure_timers.remove(task)
        return task.done
        
    def _constructExtractor(self, planet, task):
        extractor = Extractor(planet)
        self.structures.append(extractor)
        planet.task_structure_timers.remove(task)
        return task.done
    
    def _constructPhylon(self, planet, task):
        phylon = Phylon(planet)
        self.structures.append(phylon)
        planet.task_structure_timers.remove(task)
        return task.done
    
    def _constructGeneratorCore(self, planet, task):
        generatorCore = GeneratorCore(planet)
        self.structures.append(generatorCore)
        planet.task_structure_timers.remove(task)
        return task.done
    
    def _constructUnitTierI(self, planet, units_in_construction, task):
        units_in_construction = units_in_construction + 1
        
        if(planet.parent_star.lifetime <= 0):
            return task.done
        
        unit_type = random.randrange(0, 3, 1)
        if(unit_type == 0):
            task_unit_timer =  taskMgr.doMethodLater(SWARM_BUILD_TIME, self._constructSwarm, 'AIbuildSwarm', extraArgs =[planet], appendTask=True)
        elif(unit_type == 1 and planet.task_unit_timer == None):
            task_unit_timer =  taskMgr.doMethodLater(GLOBE_BUILD_TIME, self._constructSphere, 'AIbuildGlobe', extraArgs =[planet], appendTask=True)
        elif(unit_type == 2 and planet.task_unit_timer == None):
            task_unit_timer =  taskMgr.doMethodLater(ANALYZER_BUILD_TIME, self._constructAnalyzer, 'AIbuildGlobe', extraArgs =[planet], appendTask=True)  
        
        planet.task_unit_timers.append(task_unit_timer)
        if(units_in_construction >= AI_MAX_NUMBER_OF_UNITS):
            if(task==None):return
            else:return task.done
        else:
            new_task = taskMgr.doMethodLater(AI_UNIT_CONSTRUCTION_WAIT_TIME, self._constructUnitTierI, 'AIconstructUnitTierI', extraArgs =[planet, units_in_construction], appendTask=True)
            if(task!=None):return task.done
            
    def _constructUnitTierII(self, planet, units_in_construction, task):
        units_in_construction = units_in_construction + 1
        
        if(planet.parent_star.lifetime <= 0):
            return task.done
        
        unit_type = random.randrange(0, 3, 1)
        if(unit_type == 0):
            task_unit_timer = taskMgr.doMethodLater(HORDE_BUILD_TIME, self._constructHorde, 'AIbuildHorde', extraArgs =[planet], appendTask=True)
        elif(unit_type == 1):
            task_unit_timer =  taskMgr.doMethodLater(SPHERE_BUILD_TIME, self._constructSphere, 'AIbuildSphere', extraArgs =[planet], appendTask=True)
        elif(unit_type == 2):
            '''since TierII contains 2 units, an additional swarm is added here '''
            task_unit_timer =  taskMgr.doMethodLater(SWARM_BUILD_TIME, self._constructSwarm, 'AIbuildSwarm', extraArgs =[planet], appendTask=True) 
        
        planet.task_unit_timers.append(task_unit_timer)
        if(units_in_construction >= AI_MAX_NUMBER_OF_UNITS-1):
            if(task==None):return
            else:return task.done
        else:
            new_task = taskMgr.doMethodLater(AI_UNIT_CONSTRUCTION_WAIT_TIME, self._constructUnitTierII, 'AIconstructUnitTierII', extraArgs =[planet, units_in_construction], appendTask=True)
            if(task!=None):return task.done
            
    def _constructUnitTierIII(self, planet, units_in_construction, task):
        units_in_construction = units_in_construction + 1
        
        if(planet.parent_star.lifetime <= 0):
            return task.done
        
        unit_type = random.randrange(0, 3, 1)
        if(unit_type == 0):
            task_unit_timer =  taskMgr.doMethodLater(HIVE_BUILD_TIME, self._constructHive, 'AIbuildHive', extraArgs =[planet], appendTask=True)
        elif(unit_type == 1):
            task_unit_timer =  taskMgr.doMethodLater(PLANETARIUM_BUILD_TIME, self._constructPlanetarium, 'AIbuildPlanetarium', extraArgs =[planet], appendTask=True)
        elif(unit_type == 2):
            task_unit_timer =  taskMgr.doMethodLater(MATHEMATICA_BUILD_TIME, self._constructMathematica, 'AIbuildMathematica', extraArgs =[planet], appendTask=True)  
        
        planet.task_unit_timers.append(task_unit_timer)
        if(units_in_construction >= AI_MAX_NUMBER_OF_UNITS-2):
            if(task==None):return
            else:return task.done
        else:
            new_task = taskMgr.doMethodLater(AI_UNIT_CONSTRUCTION_WAIT_TIME, self._constructUnitTierIII, 'AIconstructUnitTierIII', extraArgs =[planet, units_in_construction], appendTask=True)
            if(task!=None):return task.done

    def _constructSwarm(self, planet, task):
        swarm = Swarm(planet, self)
        swarm.startOrbit()
        self.units.append(swarm)
        planet.task_unit_timers.remove(task)
        return task.done
    
    def _constructHorde(self, planet, task):
        horde = Horde(planet, self)
        horde.startOrbit()
        self.units.append(horde)
        planet.task_unit_timers.remove(task)
        return task.done
        
    def _constructHive(self, planet, task):
        hive = Hive(planet, self)
        hive.startOrbit()
        self.units.append(hive)
        planet.task_unit_timers.remove(task)
        return task.done
    
    def _constructGlobe(self, planet, task):
        globe = Globe(planet, self)
        globe.startOrbit()
        self.units.append(globe)
        planet.task_unit_timers.remove(task)
        return task.done
    
    def _constructSphere(self, planet, task):
        sphere = Sphere(planet, self)
        sphere.startOrbit()
        self.units.append(sphere)
        planet.task_unit_timers.remove(task)
        return task.done
        
    def _constructPlanetarium(self, planet, task):
        planetarium = Planetarium(planet, self)
        planetarium.startOrbit()
        self.units.append(planetarium)
        planet.task_unit_timers.remove(task)
        return task.done
    
    def _constructAnalyzer(self, planet, task):
        analyzer = Analyzer(planet, self)
        analyzer.startOrbit()
        self.units.append(analyzer)
        planet.task_unit_timers.remove(task)
        return task.done   
            
    def _constructMathematica(self, planet, task):
        mathematica = Mathematica(planet, self)
        mathematica.startOrbit()
        self.units.append(mathematica)
        planet.task_unit_timers.remove(task)
        return task.done
        
    def _constructBlackHoleGenerator(self, planet, task):
        blackHoleGenerator = BlackHoleGenerator(planet, self)
        blackHoleGenerator.startOrbit()
        self.units.append(blackHoleGenerator)
        planet.task_unit_timers.remove(task)
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
    