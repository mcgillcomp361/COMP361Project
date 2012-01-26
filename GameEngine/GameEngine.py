'''
Created on Jan 23, 2012

@author: Eran-Tasker
'''
import random

from direct.showbase import DirectObject 

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

        self.sun = Star(position=Point3(0,0,0), radius=1)
        self.dsun = StarDraw(self.sun)
        #Add observer to sun model
        self.sun.attach(self.dsun);
        
        self.system_planets = []
        for i in xrange(10):
            r = random.random()
            planet = Planet(position=Point3((random.random()-0.5) * 20, \
                                            (random.random()-0.5) * 20, 0), \
                            radius=r*0.2+0.20)
            planet.orbital_velocity = r*50+20
            planet.spin_velocity = 60
            dplanet = PlanetDraw(planet, self.dsun.point_path)
            dplanet.startSpin()
            dplanet.startOrbit()
            planet.attach(dplanet);
            self.system_planets.append((planet, dplanet))

