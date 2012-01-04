'''
Created on Jan 2, 2012

@author: JulieL
'''

import direct.directbase.DirectStart
from direct.showbase import DirectObject
from panda3d.core import TextNode, Vec3, Vec4
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
from Camera import Camera
from Planet import Planet
from Star import Star
import sys

class Game(DirectObject):
  #Macro-like function used to reduce the amount to code needed to create the
  #on screen instructions
  def genLabelText(self, text, i):
    return OnscreenText(text = text, pos = (-1.3, .95-.05*i), fg=(1,1,1,1),
                       align = TextNode.ALeft, scale = .05, mayChange = 1)

  def __init__(self):

    #The standard camera position and background initialization
    base.setBackgroundColor(0, 0, 0)
    base.disableMouse()
    
    c = Camera()
    s = Star(4, 1, 1)
    p = Planet(20, 1, 1, 1) 
    
    self.title = OnscreenText(text="Bazibaz",
                              style=1, fg=(1,1,1,1),
                              pos=(0.9,0.9), scale = .1)
    self.text = self.genLabelText(
      "Zoom in and out using a mouse", 0)
    self.text = self.genLabelText("Move mouse side to side", 1)
    self.text = self.genLabelText("Rotate view by pressing on the right mouse key", 2)
                                   #state of the global simulation
    self.loadBackground()
    self.accept("escape", sys.exit)    #Exit the program when escape is pressed


  def loadBackground(self):
    self.sky = loader.loadModel("../models/solar_sky_sphere")
    self.sky_tex = loader.loadTexture("../models/stars_1k_tex.jpg")
    self.sky.setTexture(self.sky_tex, 1)
    self.sky.reparentTo(render)
    self.sky.setScale(40)
      
g = Game()

run()

