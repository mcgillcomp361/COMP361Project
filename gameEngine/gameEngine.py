'''
Created on Jan 23, 2012

@author: Bazibaz
'''
import random
from random import uniform
import math

from direct.showbase import DirectObject 

import sys
sys.path.append("..")

from gameModel.units import Unit
from gameModel.player import *
from gameModel.ai import *
from gameModel.solar import Star, Planet
from graphicEngine.environement import Environement
#from graphicEngine.solarAnimator import SolarAnimator
from graphicEngine.camera import Camera
from gameModel.constants import UNIVERSE_SCALE, DEEP_SPACE_DISTANCE, \
MAX_DEAD_STAR_RADIUS, NUMBER_OF_STARS, MIN_DISTANCE_BETWEEN_PLANETS, \
MIN_PLANET_VELOCITY, MAX_SOLAR_SYSTEM_RADIUS, MAX_DEAD_PLANET_RADIUS, \
MAX_NUMBER_OF_PLANETS, MAX_PLANET_VELOCITY, AI_INITIATION_TIME
from panda3d.core import Point3, Vec3
from direct.task import Task
from mouseEvents import MouseEvents
from gui.gamePanel import GamePanel
from gui.guiUpdate import guiUpdate
from gui.minimap import Minimap

mouse_events = None
env_graphics = None
player = None
ai = None
ai_task = None
all_players = []
all_stars = []
all_planets = []

music = None

_game_camera = None
            
    #Keyboard events
gamePanel = None
updateGUI = None

def initialize():
    global mouse_events, env_graphics, all_players, gamePanel, updateGUI
    mouse_events = MouseEvents()
    env_graphics = Environement()
    gamePanel = None
    updateGUI = guiUpdate(0)
    _prepareGame()
    setupMinimap()
    _startGame(all_players)

def _prepareGame():
    '''
        Sets up the environment of the game
    '''
    global all_stars, all_planets, gamePanel, updateGUI
    #Initialize graphics
    max_loop = 0
    while(len(all_stars)< NUMBER_OF_STARS):
        new_star_pos = Point3()
        if (len(all_stars)==0):
            new_star_pos = Point3(0,0,0)
        else:
            new_star_pos= Point3((random.random()-0.5)*UNIVERSE_SCALE,
                                 (random.random()-0.5)*UNIVERSE_SCALE, 0)
        # Given that the star is separated enough from its neighboring stars
        # we can add it to the solar system  
        if _isSeparated(all_stars, new_star_pos, DEEP_SPACE_DISTANCE):
            star = Star(position = new_star_pos, radius = MAX_DEAD_STAR_RADIUS)
            #Add observer to star model
            star.attachObserver(updateGUI)
            all_stars.append(star)
            # Add planets to star
            prev_p = None
            radius = MAX_SOLAR_SYSTEM_RADIUS/MAX_NUMBER_OF_PLANETS
            while(star.getNumberOfPlanets() < MAX_NUMBER_OF_PLANETS):
                i = star.getNumberOfPlanets()
                angle = math.pi*2*random.random()
                radius += MIN_DISTANCE_BETWEEN_PLANETS + 3*random.random()
                planet = Planet(radius, angle, MAX_DEAD_PLANET_RADIUS, star)
                planet.parent_star = star
                planet.prev_planet = prev_p
                prev_p = planet
                planet.max_orbital_velocity = math.pow(MAX_PLANET_VELOCITY - (float(i)/MAX_NUMBER_OF_PLANETS) * (MAX_PLANET_VELOCITY - MIN_PLANET_VELOCITY), 2)
                planet.spin_velocity = 70
                star.addPlanet(planet)
                all_planets.append(planet)
            
            for i, planet in enumerate(star.planets()):
                if i==0:
                    continue
                planet.prev_planet.next_planet = planet
                
                
        #Safety check so that we don't loop forever without knowing why
        max_loop = max_loop + 1
        if max_loop > 10*NUMBER_OF_STARS:
            raise Exception("Cannot add all stars based on the current parameters.")
        
def _startGame(players):
    '''
    Start a prepared game, executes the codes that are common to both modes of the game and then enters
    either the single player mode or the multiplayer mode based on the players choice.
    @param players: the list of the players ready to play
    '''
    global _game_camera, music
    ''' TODO : music should be played here '''
#    musicMgr = base.audioManager()
    music = base.loader.loadSfx("sound/music/orbitals.mp3")
    music.setLoop(True)
    music.setVolume(0.15)
    music.play()
    
    #randomly set the camera on one of the stars for the player
    rand = random.randrange(0,NUMBER_OF_STARS,1)
    ''' TODO : camera is not set on the correct position, why ? '''
    _game_camera = Camera(all_stars[rand])
    
    '''TODO : choose between single player or multiplayer '''
    _singlePlayer()
    #multiPlayer(players)
        
def _singlePlayer():
    '''
    Run a single player game with an AI player
    @players : the player
    '''
    global player, mouse_events, ai, all_stars, _game_camera, gamePanel
    player = Player("player")
    gamePanel = GamePanel(player)
    updateGUI.refreshResources()
    updateGUI.value = player.minerals
    updateGUI.printResources()
    updateGUI.refreshGE()
    updateGUI.value = player.ge_amount
    updateGUI.printGE()
    task_track_minerals = taskMgr.doMethodLater(1, player.trackMinerals, 'trackPlayerMinerals')
    mouse_events.setPlayer(player)
    mouse_events.setCamera(_game_camera)
    ai = AI("Alien", all_stars)
    _runAI()
    task_track_units_and_structures = taskMgr.doMethodLater(1, _trackUnitsAndStructures, 'trackUnitsAndStructures')
       
def _isSeparated(neighbors, test_position, mindist):
    '''
     Check if we can add the star by verifying that it has no
     close neighbours
     @param neighbors: Neighboring bodies (ex. stars)
     @param test_position: Current position being tested
     @param mindist: Minimum distance between the position and any neighboring body
    '''
    for neighbor in neighbors:
            distance = Vec3(neighbor.position - test_position).length()
            if distance < mindist:
                return False
    return True

'''
The AI section which the game engine manages
'''
def _runAI():
    global ai_task
    ai_task = taskMgr.doMethodLater(AI_INITIATION_TIME, _initiateAI, 'initiateAI') 
    
def _initiateAI(task):
    global all_stars, ai, ai_task 
    ai.activateRandomStar()
    ai_task = None
    return task.done

def setupMinimap():
    planetTargets = []
    starTargets = []
    for planet in all_planets:
        planetTargets.append(planet)
    for star in starTargets:
        starTargets.append(star)
    map = Minimap()
    map.setTargets(planetTargets, starTargets)

'''
The Auto management of observing and removing units and structures from the game world
'''
def _trackUnitsAndStructures(task):
    global ai, player, all_stars
    #print len(player.selected_units)
    if(ai != None):
        for unit in ai.units:
            if(unit.energy <= 0):
                unit.host_planet.removeOrbitingUnit(unit)
                ai.units.remove(unit)
                unit.removeFromGame()
                unit = None

    for unit in player.units:
        if(unit.energy <= 0):
            unit.host_planet.removeOrbitingUnit(unit)
            for selected_unit in player.selected_units:
                if(unit == selected_unit):
                    player.selected_units.remove(unit)
            player.units.remove(unit)
            unit.removeFromGame()
            unit = None
            
    has_no_stars = True
    for star in all_stars:
        if(star.player == player and star.lifetime > 0):
            has_no_stars = False
            print

    ''' Loosing Condition ''',
    if(len(player.planets) == 0 and player.ge_amount == 0 and has_no_stars and player.hasCaptureTypeUnit()==False):
        print 'You Lost, Noob !'
        base.userExit()
#        base.framework.set_exit_flag()
        
    has_no_stars = True
    for star in all_stars:
        if(star.player == ai):
            has_no_stars = False

    ''' Winning Condition '''
    if(len(ai.planets) == 0 and len(ai.units) == 0 and has_no_stars and ai.isDead):
        print 'You Win, Pro!'
        base.userExit()
            
    return task.again
