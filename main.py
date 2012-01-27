'''
Created on 13 jan. 2012

@author: Bazibaz
'''
import random, math, sys

#ANTIALIASING PREREQUISITE. Has to be loaded before anything else.
from pandac.PandaModules import loadPrcFileData 
loadPrcFileData('', 'framebuffer-multisample 1' ) 
loadPrcFileData('', 'multisamples 8')

from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import *

from gui.menu import Menu
from gameEngine.gameEngine import GameEngine
    
class Application(ShowBase):
    def __init__(self):
        '''TODO: An option should be added to graphics submenu that allows the user to adjust resolution'''
        loadPrcFileData('', 'fullscreen 1')
        loadPrcFileData('', 'win-size 1280 800')
        ShowBase.__init__(self)
        
        self.menu = Menu()
        
        self.ge = GameEngine()
        
        #GUI stuff
        self.title = OnscreenText(text="Bazibaz", style=1, fg=(1,1,1,1), pos=(0.9,0.9), scale = .1)
        self.text = self.genLabelText("Orbits Alpha Ver.0.1", 0)
        self.text = self.genLabelText(
            "Zoom in and out using a mouse", 1)
        self.text = self.genLabelText("Move mouse side to side", 2)
        self.text = self.genLabelText("Rotate view by pressing on the right mouse key", 3)
        
        #Exit the program when escape is pressed
        self.accept("escape", sys.exit)

    def genLabelText(self, text, i):
        return OnscreenText(text = text, pos = (-1.3, .95-.05*i), fg=(1,1,1,1), \
                            align = TextNode.ALeft, scale = .05, mayChange = 1)
        


app = Application()
# TODO: maybe we want to manage the game loop ourselves? Using taskMgr.step().
#       See http://www.panda3d.org/manual/index.php/Main_Loop
app.run()
