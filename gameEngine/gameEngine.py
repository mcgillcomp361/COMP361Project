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

from gameModel.player import *
from gameModel.solar import Star, Planet
from graphicEngine.environement import Environement
from graphicEngine.solar import StarDraw, PlanetDraw
from graphicEngine.camera import Camera
from gameModel.constants import MAX_DEAD_STAR_RADIUS, NUMBER_OF_STARS, \
    MAX_DEAD_PLANET_RADIUS, MIN_PLANET_VELOCITY, MAX_PLANET_VELOCITY, MAX_NUMBER_OF_PLANETS, DEEP_SPACE_DISTANCE, \
    UNIVERSE_SCALE, DISTANCE_BETWEEN_PLANETS
from panda3d.core import Point3

from mouseEvents import MouseEvents

class GameEngine(DirectObject.DirectObject):
    '''
    This class acts as the connection between the game model and the graphic engine.
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.mouse_events = MouseEvents()
        
        self.all_players = []
        self.all_stars = []
        self.all_planets = []
        self.prepareGame(NUMBER_OF_STARS, MAX_NUMBER_OF_PLANETS, self.all_stars, self.all_planets)
        
        self.startGame(self.all_players)
        
    
    def prepareGame(self, number_of_stars, number_of_planets, stars, planets):
        '''
        Sets up the environment of the game
        @param number_of_stars : int, the desired number of stars 
        @precondition: number_of_stars > 0
        @param number_of_stars : int, the desired number of planets orbiting each star
        @precondition number_of_planets > 0
        @param stars : Star, list of the stars
        '''
        #Initialize graphics
        self.env_graphics = Environement()
        
        while(len(stars)<number_of_stars):
            rand = random.random()*10
            if (len(stars)==0):
                x_random = 0
                y_random = 0
            elif (rand<2.5):
                x_random = -random.random()*UNIVERSE_SCALE/(1.3)
                y_random = -random.random()*UNIVERSE_SCALE/(1.3)
            elif (rand>=2.5 and rand<5):
                x_random = random.random()*UNIVERSE_SCALE/(1.3)
                y_random = -random.random()*UNIVERSE_SCALE/(1.3)
            elif (rand>=5 and rand<7.5):
                x_random = -random.random()*UNIVERSE_SCALE/(1.3)
                y_random = random.random()*UNIVERSE_SCALE/(1.3)
            else:
                x_random = random.random()*UNIVERSE_SCALE/(1.3)
                y_random = random.random()*UNIVERSE_SCALE/(1.3)
                
            add = True
            
            for star in stars:
                if(DEEP_SPACE_DISTANCE>abs(x_random-star[0].position.x) or \
                   DEEP_SPACE_DISTANCE>abs(y_random-star[0].position.y)):
                    add = False
            
            if(add):
                star = Star(position=Point3(x_random,y_random,0), radius = MAX_DEAD_STAR_RADIUS)
                dstar = StarDraw(star)
                #Add observer to star model
                star.attachObserver(dstar);
                stars.append((star,dstar))
                i=1
                prev_p = None
                while(i<=number_of_planets):
                    '''DO NOT CHANGE THESE FORMULAS'''
                    alpha = math.pi*2*random.random()
                    pxcord = math.cos(alpha)*DISTANCE_BETWEEN_PLANETS*i + star.position.x
                    pycord = math.sin(alpha)*DISTANCE_BETWEEN_PLANETS*i + star.position.y
                    planet = Planet(position=Point3(pxcord*0.001,\
                                                    pycord*0.001, 0), \
                                    radius = MAX_DEAD_PLANET_RADIUS)
                    
                    planet.parent_star = star
                    planet.prev_planet = prev_p
                    prev_p = planet
                    planet.orbital_velocity = MAX_PLANET_VELOCITY/(number_of_planets-i+1) + (MIN_PLANET_VELOCITY*math.pow(i+2,3))
                    planet.spin_velocity = 70
                    dplanet = PlanetDraw(planet, dstar.point_path)
                    planet.attachObserver(dplanet);
                    star.addPlanet(planet)
                    planets.append((planet,dplanet))
                    i = i + 1
            
        
            
    def startGame(self, players):
        '''
        Start a prepared game, executes the codes that are common to both modes of the game and then enters
        either the single player mode or the multiplayer mode based on the players choice.
        @param players: the list of the players ready to play
        '''
        music = base.loader.loadSfx("sound/music/music1.mp3")
        music.setLoop(True)
        music.play()
        
        #randomly set the camera on one of the stars for the player
        rand = random.randrange(0,NUMBER_OF_STARS,1)
        ''' TODO : camera is not set on the correct position, why ? '''
        self.game_camera = Camera(self.all_stars[rand])
        
        '''TODO : choose between single player or multiplayer '''
        self.singlePlayer()
        #multiPlayer(players)
            
    def singlePlayer(self):
        '''
        Run a single player game with an AI player
        @players : the player
        '''
        self.player = Player("player")
        self.AI = Player("AI")
        
        
        