'''
Created on Jan 23, 2012

@author: Bazibaz
'''
import random

from direct.showbase import DirectObject 

import sys
sys.path.append("..")

from gameModel.solar import *
from graphicEngine.environement import Environement
from graphicEngine.solar import StarDraw, PlanetDraw
from graphicEngine.camera import Camera
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
        #initialize graphics
        self.env_graphics = Environement()
        self.game_camera = Camera()
        self.mouse_events = MouseEvents()
        
        music = base.loader.loadSfx("models/music1.mp3")
        music.play()

        self.star1 = Star(position=Point3(random.random()*20,0,0), radius=1)
        self.dstar1 = StarDraw(self.star1)
        #Add observer to star model
        self.star1.attach(self.dstar1);
        
        self.system_planets = []
        for i in xrange(random.random()*20):
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
            
        self.star2 = Star(position=Point3(50,random.random()*(-30),0), radius=1)
        self.dstar2 = StarDraw(self.star2)
        #Add observer to star model
        self.star2.attach(self.dstar2);
        
        for i in xrange(random.random()*20):
            r = random.random()
            planet = Planet(position=Point3((random.random()-0.5) * 20, \
                                            (random.random()-0.5) * 20, 0), \
                            radius=r*0.2+0.20)
            planet.orbital_velocity = r*50+20
            planet.spin_velocity = 60
            dplanet = PlanetDraw(planet, self.dstar2.point_path)
            dplanet.startSpin()
            dplanet.startOrbit()
            planet.attach(dplanet);
            self.system_planets.append((planet, dplanet))
            
        self.star3 = Star(position=Point3(-50,random.random()*50,0), radius=1)
        self.dstar3 = StarDraw(self.star3)
        #Add observer to star model
        self.star3.attach(self.dstar3);
        
        for i in xrange(random.random()*20):
            r = random.random()
            planet = Planet(position=Point3((random.random()-0.5) * 20, \
                                            (random.random()-0.5) * 20, 0), \
                            radius=r*0.2+0.20)
            planet.orbital_velocity = r*50+20
            planet.spin_velocity = 60
            dplanet = PlanetDraw(planet, self.dstar3.point_path)
            dplanet.startSpin()
            dplanet.startOrbit()
            planet.attach(dplanet);
            self.system_planets.append((planet, dplanet))

