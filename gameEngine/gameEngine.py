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
from gameModel.constants import MAX_DEAD_STAR_RADIUS, NUMBER_OF_STARS, DEEP_SPACE_DISTANCE, UNIVERSE_SCALE
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
        
        self.startSinglePlayerGame()
        
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
        @precondition: number_of_stars > 0
        @param stars : Star, list of the stars
        '''
        #Initialize graphics and camera
        self.env_graphics = Environement()
        self.game_camera = Camera()
        
        self.star = Star(position=Point3(0,0,0), radius = MAX_DEAD_STAR_RADIUS)
        self.dstar = StarDraw(self.star)
        #Add observer to star model
        self.star.attach(self.dstar);
        stars.append((self.star,self.dstar))
        
        while(len(stars)<number_of_stars):
            rand = random.random()*10
            if (rand<2.5):
                x_random = -random.random()*UNIVERSE_SCALE
                y_random = -random.random()*UNIVERSE_SCALE
            elif (rand>=2.5 and rand<5):
                x_random = random.random()*UNIVERSE_SCALE
                y_random = -random.random()*UNIVERSE_SCALE
            elif (rand>=5 and rand<7.5):
                x_random = -random.random()*UNIVERSE_SCALE
                y_random = random.random()*UNIVERSE_SCALE
            else:
                x_random = random.random()*UNIVERSE_SCALE
                y_random = random.random()*UNIVERSE_SCALE
                
            add = True
            
            for star in stars:
                if(DEEP_SPACE_DISTANCE>abs(x_random-star[0].position.x) and DEEP_SPACE_DISTANCE>abs(y_random-star[0].position.y)):
                    add = False
                    print DEEP_SPACE_DISTANCE
                    print x_random-star[0].position.x
            
            if(add):
                self.star = Star(position=Point3(x_random,y_random,0), radius = MAX_DEAD_STAR_RADIUS)
                self.dstar = StarDraw(self.star)
                #Add observer to star model
                self.star.attach(self.dstar);
                stars.append((self.star,self.dstar))
            
        
            
    def startSinglePlayerGame(self):
        '''
        Start a prepared game
        '''
        music = base.loader.loadSfx("models/music1.mp3")
        music.play()

