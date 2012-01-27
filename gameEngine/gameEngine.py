'''
Created on Jan 23, 2012

@author: Bazibaz
'''
import random

from direct.showbase import DirectObject 

import sys
sys.path.append("..")

from gameModel.solar import Star, Planet
from graphicEngine.environement import Environement
from graphicEngine.solar import StarDraw, PlanetDraw
from graphicEngine.camera import Camera
from gameModel.constants import MAX_DEAD_STAR_RADIUS, NUMBER_OF_STARS
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
        
        self.stars = []
        self.prepareGame(NUMBER_OF_STARS, self.stars)
        
        self.startGame()
        
        ''''
        self.system_planets = []
        for i in xrange(int(random.random()*20)):
            r = random.random()
            planet = Planet(position=Point3((random.random()-0.5) * 20, \
                                            (random.random()-0.5) * 20, 0), \
                            radius=r*0.2+0.20)
            planet.orbital_velocity = r*50+20
            planet.spin_velocity = 60
            dplanet = PlanetDraw(planet, self.dstar1.point_path)
            dplanet.startSpin()
            dplanet.startOrbit()
            planet.attach(dplanet);
            self.system_planets.append((planet, dplanet))
        '''
    
    def prepareGame(self, number_of_stars, stars):
        '''
        Sets up the environment of the game
        @param number_of_stars : int, the desired number of stars 
        @param stars : Star, list of the stars
        '''
        #initialize graphics and camera
        self.env_graphics = Environement()
        self.game_camera = Camera()
        
        for i in xrange(number_of_stars):
            # @todo : make sure the distance between stars are correct
            self.star = Star(position=Point3(random.random()*20,0,0), radius = MAX_DEAD_STAR_RADIUS)
            self.dstar = StarDraw(self.star)
            #Add observer to star model
            self.star.attach(self.dstar);
            stars.append((self.star,self.dstar))
        
    def startGame(self):
        '''
        Start a prepared game
        '''
        music = base.loader.loadSfx("models/music1.mp3")
        music.play()

