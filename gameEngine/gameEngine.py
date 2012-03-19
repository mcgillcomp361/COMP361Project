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
from gameModel.solar import Star, Planet
from graphicEngine.environement import Environement
#from graphicEngine.solarAnimator import SolarAnimator
from graphicEngine.camera import Camera
from gameModel.constants import UNIVERSE_SCALE, DEEP_SPACE_DISTANCE, \
MAX_DEAD_STAR_RADIUS, NUMBER_OF_STARS, MIN_DISTANCE_BETWEEN_PLANETS, \
MIN_PLANET_VELOCITY, MAX_SOLAR_SYSTEM_RADIUS, MAX_DEAD_PLANET_RADIUS, \
MAX_NUMBER_OF_PLANETS, MAX_PLANET_VELOCITY
from panda3d.core import Point3, Vec3
from direct.task import Task
from mouseEvents import MouseEvents
from gui.gamePanel import GamePanel
from gui.guiUpdate import guiUpdate

mouse_events = None
env_graphics = None
player = None
AI = None
all_players = []
all_stars = []
all_planets = []

_game_camera = None
            
    #Keyboard events
gamePanel = None
updateGUI = None

def initialize():
    global mouse_events, env_graphics, all_players, gamePanel, updateGUI
    mouse_events = MouseEvents()
    env_graphics = Environement()
    gamePanel = GamePanel(player)
    updateGUI = guiUpdate(0)
    _prepareGame()
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
                planet.orbital_velocity = math.pow(MAX_PLANET_VELOCITY - (float(i)/MAX_NUMBER_OF_PLANETS) * (MAX_PLANET_VELOCITY - MIN_PLANET_VELOCITY), 2)
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
    
    ''' TODO : music should be self.music so it can be changed later on '''
    music = base.loader.loadSfx("sound/music/music1.mp3")
    music.setLoop(True)
    music.play()
    
    #randomly set the camera on one of the stars for the player
    rand = random.randrange(0,NUMBER_OF_STARS,1)
    ''' TODO : camera is not set on the correct position, why ? '''
    game_camera = Camera(all_stars[rand])
    
    '''TODO : choose between single player or multiplayer '''
    _singlePlayer()
    #multiPlayer(players)
        
def _singlePlayer():
    '''
    Run a single player game with an AI player
    @players : the player
    '''
    global player, mouse_events, AI
    player = Player("player")
    mouse_events.setPlayer(player)
    AI = Player("AI")
    
def moveUnitsPrev():
    global player
    planet = player.selected_planet
    if planet != None and planet.next_planet != None:
        for unit in planet.units():
            unit.move(planet.next_planet)
            break

def moveUnitsNext():
    global player
    planet = player.selected_planet
    if planet != None and planet.prev_planet != None:
        for unit in planet.units():
            unit.move(planet.prev_planet)
            break
       
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