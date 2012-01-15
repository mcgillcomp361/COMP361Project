'''
Created on Jan 2, 2012

@author: JulieL
'''

import direct.directbase.DirectStart
from direct.showbase import DirectObject
from panda3d.core import TextNode, Point3
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
import sys

from GameModel.solar import Star, Planet
from GameModel.Player import Player
from GraphicEngine.camera import Camera
from GraphicEngine.solar_render import StarRender, PlanetRender
from GameEngine.MouseEvents import MouseEvents

class Game(DirectObject):
    #Macro-like function used to reduce the amount to code needed to create the
    #on screen instructions
    def genLabelText(self, text, i):
        return OnscreenText(text = text, pos = (-1.3, .95-.05*i), fg=(1,1,1,1), \
                            align = TextNode.ALeft, scale = .05, mayChange = 1)

    def __init__(self):

        #The standard camera position and background initialization
        base.setBackgroundColor(0, 0, 0)
        base.disableMouse()
        c = Camera()
        m = MouseEvents()
        p = Player(name="Player 1", research_tree="research Tree")
        
        deadStar = Star(position=Point3(0,0,0), radius=0.5)
        StarRender(deadStar)
        deadPlanet = Planet(position=Point3(5,5,0), radius=1, parent_star=deadStar) 
        deadPlanet.orbital_velocity = 100
        PlanetRender(deadPlanet)
        
 
        
        self.title = OnscreenText(text="Bazibaz", style=1, fg=(1,1,1,1), pos=(0.9,0.9), scale = .1)
        self.text = self.genLabelText(
            "Zoom in and out using a mouse", 0)
        self.text = self.genLabelText("Move mouse side to side", 1)
        self.text = self.genLabelText("Rotate view by pressing on the right mouse key", 2)
        self.loadBackground()
        #Exit the program when escape is pressed
        self.accept("escape", sys.exit)


    def loadBackground(self):
        self.sky = loader.loadModel("models/solar_sky_sphere")
        self.sky_tex = loader.loadTexture("models/stars_1k_tex.jpg")
        self.sky.setTexture(self.sky_tex, 1)
        self.sky.reparentTo(render)
        self.sky.setScale(40)
            
g = Game()

run()
