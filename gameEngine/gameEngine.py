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
from graphicEngine.solarAnimator import SolarAnimator
from graphicEngine.solar import StarDraw, PlanetDraw, UnitDraw
from graphicEngine.camera import Camera
from gui.gamePanel import GamePanel
from gameModel.constants import UNIVERSE_SCALE, DEEP_SPACE_DISTANCE, \
MAX_DEAD_STAR_RADIUS, NUMBER_OF_STARS, MIN_DISTANCE_BETWEEN_PLANETS, \
MIN_PLANET_VELOCITY, MAX_SOLAR_SYSTEM_RADIUS, MAX_DEAD_PLANET_RADIUS, \
MAX_NUMBER_OF_PLANETS, MAX_PLANET_VELOCITY
from panda3d.core import Point3, Vec3
from direct.task import Task

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
        
        self.player = None
        self.AI = None
        
        self.all_players = []
        self.all_stars = []
        self.all_planets = []
        self.prepareGame(NUMBER_OF_STARS, MAX_NUMBER_OF_PLANETS, self.all_stars, self.all_planets)
        self.solarAnimator = SolarAnimator([s[1] for s in self.all_stars], [p[1] for p in self.all_planets])
        
        self.startGame(self.all_players)
        #Keyboard events
        self.accept('u', self._addUnit) #temporary function for testing units
    
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
        max_loop = 0
        while(len(stars)< number_of_stars):
            new_star_pos = Point3()
            if (len(stars)==0):
                new_star_pos = Point3(0,0,0)
            else:
                new_star_pos= Point3((random.random()-0.5)*UNIVERSE_SCALE,
                                     (random.random()-0.5)*UNIVERSE_SCALE, 0)
            # Given that the star is separated enough from its neighboring stars
            # we can add it to the solar system  
            if _isSeparated([s[0] for s in stars], new_star_pos, DEEP_SPACE_DISTANCE):
                star = Star(position = new_star_pos, radius = MAX_DEAD_STAR_RADIUS)
                dstar = StarDraw(star)
                #Add observer to star model
                star.attachObserver(dstar);
                self.all_stars.append((star,dstar))
                # Add planets to star
                prev_p = None
                radius = MAX_SOLAR_SYSTEM_RADIUS/number_of_planets
                while(star.getNumberOfPlanets() < number_of_planets):
                    i = star.getNumberOfPlanets()
                    angle = math.pi*2*random.random()
                    radius += MIN_DISTANCE_BETWEEN_PLANETS + 3*random.random()
                    planet = Planet(radius, angle, MAX_DEAD_PLANET_RADIUS)
                    planet.parent_star = star
                    planet.prev_planet = prev_p
                    prev_p = planet
                    planet.orbital_velocity = math.pow(MAX_PLANET_VELOCITY - (float(i)/number_of_planets) * (MAX_PLANET_VELOCITY - MIN_PLANET_VELOCITY), 2)
                    planet.spin_velocity = 70
                    dplanet = PlanetDraw(planet, dstar.point_path)
                    planet.attachObserver(dplanet);
                    star.addPlanet(planet)
                    self.all_planets.append((planet,dplanet))
                
                for i, planet in enumerate(star.planets()):
                    if i==0:
                        continue
                    planet.prev_planet.next_planet = planet
                    
                    
            #Safety check so that we don't loop forever without knowing why
            max_loop = max_loop + 1
            if max_loop > 10*number_of_stars:
                raise Exception("Cannot add all stars based on the current parameters.")
            
    def startGame(self, players):
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
        self.game_camera = Camera(self.all_stars[rand][0])
        
        '''TODO : choose between single player or multiplayer '''
        self.singlePlayer()
        #multiPlayer(players)
            
    def singlePlayer(self):
        '''
        Run a single player game with an AI player
        @players : the player
        '''
        self.player = Player("player")
        self.gP = GamePanel(self.player)
        self.AI = Player("AI")
    
    #Temporary function for adding & testing units
    def _addUnit(self):
        if self.mouse_events.selected_planet_pair != None:
            host_planet = self.mouse_events.selected_planet_pair[0]
            self.unit = Unit(host_planet, 1,1,1)
            host_planet.addOrbitingUnit(self.unit)
            self.dunit = UnitDraw(self.unit, self.mouse_events.selected_planet_pair[1])
            self.dunit.startOrbit()
#            taskMgr.add(self.all_planets[3][1].drawConnections, 'Accumulator', extraArgs=[self.all_planets[4][1]], appendTask=True)
#            self.all_planets[3][1].connections.create()
#            self.all_planets[3][1].drawConnections(self.all_planets[4][1])

       
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
