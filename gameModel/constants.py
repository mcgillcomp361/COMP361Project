'''
Created on Jan 12, 2012
@author: Bazibaz
'''
import math

''' Environment '''
UNIVERSE_SCALE = 12000

''' Stars '''
STAR_BUILD_TIME = 0
MAX_DEAD_STAR_RADIUS = UNIVERSE_SCALE/2000
MAX_STAR_RADIUS = UNIVERSE_SCALE/1500
#make sure the number is satisfactory for UNIVERSE_SCALE
NUMBER_OF_STARS = 10
LIFETIME = 1800000

''' Planets '''
PLANET_BUILD_TIME = 0
MAX_NUMBER_OF_PLANETS = 10
MAX_DEAD_PLANET_RADIUS = MAX_DEAD_STAR_RADIUS/3.6
MAX_PLANET_RADIUS = MAX_DEAD_PLANET_RADIUS*1.8
DISTANCE_BETWEEN_PLANETS = MAX_PLANET_RADIUS*7000#do not change this at any cost
MIN_PLANET_VELOCITY = 1
MAX_PLANET_VELOCITY = 100

''' Deep Space '''
DEEP_SPACE_DISTANCE = UNIVERSE_SCALE*MAX_NUMBER_OF_PLANETS/100

''' Resources '''
MINERAL_STARTING_AMOUNT = 0
GRAVITY_ENGINE_STARTING_AMOUNT = 1

''' Structures '''
STRUCTURE_TYPE = ["Forge","Nexus","Extractor","Phylon","GeneratorCore","PlanetaryDefenseI",
                  "PlanetaryDefenseII","PlanetaryDefenseIII","PlanetaryDefenseIV","GravityEngine"]
MAX_NUMBER_OF_STRUCTURE = 4
FORGE_DESCRIPTION = "These are complex production facilities that cover entire continents. It allows construction of all the unlocked units on that specific planet"
FORGE_MAX_ENERGY = 1200
FORGE_BUILD_TIME = 30
NEXUS_DESCRIPTION = "This massive complex is used to research the ancient technology and speed up evolution"
NEXUS_MAX_ENERGY = 1000
NEXUS_BUILD_TIME = 50
NEXUS_RESEARCH_INCREASE_RATE = 1.1
EXTRACTOR_DESCRIPTION = "The basic mineral gathering complex"
EXTRACTOR_MAX_ENERGY = 200
EXTRACTOR_BUILD_TIME = 15
EXTRACTOR_RESOURCE_GENERATION_RATE = 1
PHYLON_DESCRIPTION = "A fast mineral gathering complex equipped with advanced excavating machines"
PHYLON_MAX_ENERGY = 400
PHYLON_BUILD_TIME = 30
PHYLON_RESOURCE_GENERATION_RATE = 2
GENERATOR_CORE_DESCRIPTION = "Massive mineral gathering complex equipped with ancient technology of cracking planet's cores"
GENERATOR_CORE_ENERGY = 600
GENERATOR_CORE_BUILD_TIME = 60
GENERATOR_CORE_RESOURCE_GENERATION_RATE = 3
PLANETARY_DEFENSE_I_DESCRIPTION = "Basic turrets constructed in the orbit of the planet"
PLANETARY_DEFENSE_I_MAX_ENERGY = 100
PLANETARY_DEFENSE_I_BUILD_TIME = 20
PLANETARY_DEFENSE_I_DAMAGE = 3
PLANETARY_DEFENSE_II_DESCRIPTION = "Medium size turrets constructed in the orbit of the planet"
PLANETARY_DEFENSE_II_MAX_ENERGY = 200
PLANETARY_DEFENSE_II_BUILD_TIME = 30
PLANETARY_DEFENSE_II_DAMAGE = 5
PLANETARY_DEFENSE_III_DESCRIPTION = "Advanced turrets constructed in the orbit of the planet"
PLANETARY_DEFENSE_III_MAX_ENERGY = 300
PLANETARY_DEFENSE_III_BUILD_TIME = 40
PLANETARY_DEFENSE_III_DAMAGE = 7
PLANETARY_DEFENSE_IV_DESCRIPTION = "Heavy turrets and defensive space stations constructed in the orbit of the planet"
PLANETARY_DEFENSE_IV_MAX_ENERGY = 400
PLANETARY_DEFENSE_IV_BUILD_TIME = 50
PLANETARY_DEFENSE_IV_DAMAGE = 9

''' Units '''
UNIT_TYPE = ["Swarm","Horde","Hive","Globe","Sphere","Planetarium",
             "Analyzer","Mathematica","BlackHoleGenerator"]
MAX_NUMBER_OF_UNITS = 30
MIN_UNIT_VELOCITY = 0
MAX_UNIT_VELOCITY = 2
SWARM_DESCRIPTION = "The basic combat unit which compromises of hundreds of combat bio-drones equipped with para-dimensional sight and dark energy engines. The swarm is fast but very weak"
SWARM_MAX_ENERGY = 100
SWARM_DAMAGE = 4
SWARM_VELOCITY = 1
SWARM_BUILD_TIME = 15
SWARM_MINERAL_COST = 50
HORDE_DESCRIPTION = "Evolved from the swarm, this unit compromises of thousands of combat bio-drones  equipped with para-dimensional sight, dark energy engines and excavation tech. The horde is much stronger and larger than the swarm but relatively slower"
HORDE_MAX_ENERGY = 250
HORDE_DAMAGE = 8
HORDE_VELOCITY = 1
HORDE_BUILD_TIME = 30
HORDE_MINERAL_COST = 120
HIVE_DESCRIPTION = "Evolved from the Horde, this unit compromises of millions of combat bio-drones  equipped with para-dimensional sight, dark energy engines, excavation tech and deadly harvesting tools. The hive is much stronger and larger than the horde but relatively slower"
HIVE_MAX_ENERGY = 500
HIVE_DAMAGE = 12
HIVE_VELOCITY = 1
HIVE_BUILD_TIME = 60
HIVE_MINERAL_COST = 230

''' Abilities '''

''' Evolution Tree '''

