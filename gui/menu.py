import sys
from direct.gui.OnscreenText import OnscreenText 
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from gameEngine.gameEngine import GameEngine
 

class Menu(): 
    def __init__(self): 
        self.b=OnscreenImage(parent=render2d, image="./models/gui/mainMenu.png") 
        b1 = DirectButton(text = ("Single Player", "click!", "start_roll", "disabled"), frameColor=(1, 1, 1, 0), text_fg=(1, 1, 1, 1),
                     text_scale=0.1, text_align = TextNode.ALeft, pos=(0.3, 0, 0.4),
                     relief=2, command = self.startGame)
            
        b2 = DirectButton(text = ("Multiplayer", "click!", "start_roll", "disabled"), frameColor=(1, 1, 1, 0), text_fg=(1, 1, 1, 1),
                      text_scale=0.1,  text_align = TextNode.ALeft,pos=(1, 0, 0.15),
                      relief=2, command = self.startGame)
        b3 = DirectButton(text = ("Tutorial", "click!", "tutorial_roll", "disabled"), frameColor=(1, 1, 1, 0), text_fg=(1, 1, 1, 1),
                      text_scale=0.1, text_align = TextNode.ALeft,pos=(-1.2, 0, 0.1),
                      relief=2, command = self.tutorial)
        b4 = DirectButton(text = ("Settings", "click!", "settings_roll", "disabled"), frameColor=(1, 1, 1, 0), text_fg=(1, 1, 1, 1),
                              text_scale=0.1, text_align = TextNode.ALeft,pos=(0.35, 0, -0.15),
                              relief=2, command = self.settings)
        b5 = DirectButton(text = ("Exit", "click!", "exit", "disabled"), frameColor=(1, 1, 1, 0), text_fg=(1, 1, 1, 1),
                              text_scale=0.1, text_align = TextNode.ALeft,pos=(-1.55, 0, -0.35),
                              relief=2, command = sys.exit)
            
        self.mainFrame = DirectFrame(pos=(0,0,0))
        b1.reparentTo(self.mainFrame)
        b2.reparentTo(self.mainFrame)
        b3.reparentTo(self.mainFrame)
        b4.reparentTo(self.mainFrame)
        b5.reparentTo(self.mainFrame)
       
       
    def startGame(self):
        print 'starting game'
        self.mainFrame.destroy()
        self.b.destroy()
        self.ge = GameEngine()

    def mainMenu(self):
        self.mainFrame.destroy()

        b1 = DirectButton(text = ("Single Player", "click!", "start_roll", "disabled"), frameColor=(1, 1, 1, 0), text_fg=(1, 1, 1, 1),
                     text_scale=0.1, text_align = TextNode.ALeft, pos=(0.3, 0, 0.4),
                     relief=2, command = self.startGame)
            
        b2 = DirectButton(text = ("Multiplayer", "click!", "start_roll", "disabled"), frameColor=(1, 1, 1, 0), text_fg=(1, 1, 1, 1),
                      text_scale=0.1,  text_align = TextNode.ALeft,pos=(1, 0, 0.15),
                      relief=2, command = self.startGame)
        b3 = DirectButton(text = ("Tutorial", "click!", "tutorial_roll", "disabled"), frameColor=(1, 1, 1, 0), text_fg=(1, 1, 1, 1),
                      text_scale=0.1, text_align = TextNode.ALeft,pos=(-1.2, 0, 0.1),
                      relief=2, command = self.tutorial)
        b4 = DirectButton(text = ("Settings", "click!", "settings_roll", "disabled"), frameColor=(1, 1, 1, 0), text_fg=(1, 1, 1, 1),
                              text_scale=0.1, text_align = TextNode.ALeft,pos=(0.35, 0, -0.15),
                              relief=2, command = self.settings)
        b5 = DirectButton(text = ("Exit", "click!", "exit", "disabled"), frameColor=(1, 1, 1, 0), text_fg=(1, 1, 1, 1),
                              text_scale=0.1, text_align = TextNode.ALeft,pos=(-1.55, 0, -0.35),
                              relief=2, command = sys.exit)
            
        self.mainFrame = DirectFrame(pos=(0,0,0) )
        b1.reparentTo(self.mainFrame)
        b2.reparentTo(self.mainFrame)
        b3.reparentTo(self.mainFrame)
        b4.reparentTo(self.mainFrame)
        b5.reparentTo(self.mainFrame)
       
        
    def tutorial(self):
        initial_menu = 1
        self.mainFrame.destroy()
        screenText = OnscreenText(text = 'TUTORIAL', pos = (0.2, 0.6), scale = 0.1, fg = (1, 1, 1, 1))
        b1 = DirectButton(text = ("Back to Main Menu", "click!", "main menu roll", "disabled"), frameColor=(1, 1, 1, 0), text_fg=(1, 1, 1, 1),
                  text_scale=0.1, text_align = TextNode.ALeft, pos=(0.2, 0, -0.5),
                  relief=2, command = self.mainMenu)
        self.mainFrame = DirectFrame(pos=(0,0,0))       
        screenText.reparentTo(self.mainFrame)
        b1.reparentTo(self.mainFrame)
    
    def settings(self):
        self.mainFrame.destroy()
        screenText = OnscreenText(text = 'Audio Settings', pos = (0.2, 0.6), scale = .1, fg = (1, 1, 1, 1))
        volumeText = OnscreenText(text = 'Set Volume:', pos = (0.1, 0.5), scale = 0.05, fg = (1, 1, 1, 1))
        b1 = DirectButton(text = ("Back to Main Menu", "click!", "main menu roll", "disabled"), frameColor=(1, 1, 1, 0), text_fg=(1, 1, 1, 1),
                  text_scale=0.1, text_align = TextNode.ALeft, pos=(0.2, 0, -0.5),
                  relief=2, command = self.mainMenu)
 
        self.mainFrame = DirectFrame(pos=(0,0,0) )
        screenText.reparentTo(self.mainFrame)
        volumeText.reparentTo(self.mainFrame)
        b1.reparentTo(self.mainFrame)