'''
Created on Jan 12, 2012
@author: Bazibaz
'''

''' Environment '''
#Smaller for easier testing -> instead of searching forever
UNIVERSE_SCALE = 6000
MAX_CAMERA_DISTANCE = 15000
''' Stars '''
STAR_BUILD_TIME = 0
#I think these should be independent from the universe scale
MAX_DEAD_STAR_RADIUS = 6
MAX_STAR_RADIUS = 8
MAX_SOLAR_SYSTEM_RADIUS = 100 #could be variable instead
#make sure the number is satisfactory for UNIVERSE_SCALE
NUMBER_OF_STARS = 10
LIFETIME = 180.0 
''' should be divisible by 6 '''

''' Planets '''
PLANET_BUILD_TIME = 0
MAX_NUMBER_OF_PLANETS = 10
MAX_DEAD_PLANET_RADIUS = MAX_DEAD_STAR_RADIUS/3.6
MAX_PLANET_RADIUS = MAX_DEAD_PLANET_RADIUS*1.8
MIN_DISTANCE_BETWEEN_PLANETS = MAX_PLANET_RADIUS*5
MIN_PLANET_VELOCITY = 0.006
MAX_PLANET_VELOCITY = 0.08
PLANET_SPIN_VELOCITY = 5

''' Deep Space a.k.a. min distance between stars'''
DEEP_SPACE_DISTANCE = UNIVERSE_SCALE*MAX_NUMBER_OF_PLANETS/50

''' Resources '''
MINERAL_STARTING_AMOUNT = 0
GRAVITY_ENGINE_STARTING_AMOUNT = 1

''' AI '''
AI_INITIATION_TIME = 9
AI_ACTIVATE_PLANET_WAIT_TIME = 60
AI_ACCELERATION_TIME = 5
AI_START_CONSTRUCTION_WAIT_TIME = 10
AI_UNIT_CONSTRUCTION_WAIT_TIME = 3
AI_MAX_NUMBER_OF_UNITS = 3 #per planet
AI_ESCAPE_WAIT_TIME = 2

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
GENERATOR_CORE_MAX_ENERGY = 600
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
HORDE_MINERAL_COST = 150
HIVE_DESCRIPTION = "Evolved from the Horde, this unit compromises of millions of combat bio-drones  equipped with para-dimensional sight, dark energy engines, excavation tech and deadly harvesting tools. The hive is much stronger and larger than the horde but relatively slower"
HIVE_MAX_ENERGY = 500
HIVE_DAMAGE = 12
HIVE_VELOCITY = 1
HIVE_BUILD_TIME = 60
HIVE_MINERAL_COST = 250
GLOBE_DESCRIPTION = "This basic synthetic machine built from the remains of the ancient technology is used as a major combat unit. It is much more effective than the swarm but it costs more minerals to be built"
GLOBE_MAX_ENERGY = 160
GLOBE_DAMAGE = 6
GLOBE_VELOCITY = 1
GLOBE_BUILD_TIME = 25
GLOBE_MINERAL_COST = 100
SPHERE_DESCRIPTION = "A synthetic machine based on the Globe design but much more effective in combat and can also repair any units close by. Although, it requires more minerals to be built and is slower"
SPHERE_MAX_ENERGY = 270
SPHERE_DAMAGE = 8
SPHERE_VELOCITY = 1
SPHERE_BUILD_TIME = 45
SPHERE_MINERAL_COST = 250
PLANETARIUM_DESCRIPTION = "A massive synthetic machine based on the Sphere design with devastating power which can also repair any units close by. Although, it requires more minerals to be built and is much slower"
PLANETARIUM_MAX_ENERGY = 600
PLANETARIUM_DAMAGE = 13
PLANETARIUM_VELOCITY = 1
PLANETARIUM_BUILD_TIME = 70
PLANETARIUM_MINERAL_COST = 500
ANALYZER_DESCRIPTION = "A living supercomputer made out of thousands of artificial brains is used to monitor every activity in a galaxy. Very weak and has no combat capabilities but it can detect cloaked units"
ANALYZER_MAX_ENERGY = 130
ANALYZER_DAMAGE = 0
ANALYZER_VELOCITY = 1
ANALYZER_BUILD_TIME = 20
ANALYZER_MINERAL_COST = 80
MATHEMATICA_DESCRIPTION = "The ultimate form of Artificial Intelligence, a supercomputer god made out of millions of artificial brains is used to monitor every activity in the universe. Much stronger than analyzer but  has no combat capabilities. It can detect cloaked units"
MATHEMATICA_MAX_ENERGY = 300
MATHEMATICA_DAMAGE = 0
MATHEMATICA_VELOCITY = 1
MATHEMATICA_BUILD_TIME = 50
MATHEMATICA_MINERAL_COST = 210
BLACK_HOLE_GENERATOR_DESCRIPTION = "The ultimate Weapon. Creates a black hole in a star. It is very slow"
BLACK_HOLE_GENERATOR_MAX_ENERGY = 400
BLACK_HOLE_GENERATOR_DAMAGE = 0
BLACK_HOLE_GENERATOR_VELOCITY = 1
BLACK_HOLE_GENERATOR_BUILD_TIME = 90
BLACK_HOLE_GENERATOR_MINERAL_COST = 1000

''' Abilities '''

''' Evolution Tree '''