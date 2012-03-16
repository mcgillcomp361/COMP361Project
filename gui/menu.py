import sys
from direct.gui.OnscreenText import OnscreenText 
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from gameEngine.gameEngine import GameEngine
 

class Menu(): 
    def __init__(self): 
        self.b=OnscreenImage(parent=render2d, image="./models/gui/mainMenu.png") 
        self.screenImages=loader.loadModel('./models/gui/singleplayer.egg')
        b1 = DirectButton(geom=(self.screenImages.find('**/singleplayer'), 
                        self.screenImages.find('**/singleplayer_over'), 
                        self.screenImages.find('**/singleplayer_over'), 
                        self.screenImages.find('**/singleplayer')), frameColor=(1, 1, 1, 0), text_fg=(1, 1, 1, 1),
                      pos=(0.6, 0, 0.4),
                     relief=2, command = self.startGame)
        b1.setScale(0.6,1,0.16)
        self.screenImages=loader.loadModel('./models/gui/multiplayer.egg')
        b2 = DirectButton(geom=(self.screenImages.find('**/multiplayer'), 
                        self.screenImages.find('**/multiplayer_over'), 
                        self.screenImages.find('**/multiplayer_over'), 
                        self.screenImages.find('**/multiplayer')), frameColor=(1, 1, 1, 0), text_fg=(1, 1, 1, 1),
                      pos=(1.3, 0, 0.15),
                     relief=2, command = self.startGame)
        b2.setScale(0.6,1,0.16)
        self.screenImages=loader.loadModel('./models/gui/tutorial.egg')
        b3 = DirectButton(geom=(self.screenImages.find('**/tutorial'), 
                        self.screenImages.find('**/tutorial_over'), 
                        self.screenImages.find('**/tutorial_over'), 
                        self.screenImages.find('**/tutorial')), frameColor=(1, 1, 1, 0), text_fg=(1, 1, 1, 1),
                      pos=(-1.1, 0, 0.1),
                     relief=2, command = self.tutorial)
        b3.setScale(0.6,1,0.16)
        self.screenImages=loader.loadModel('./models/gui/settings.egg')
        b4 = DirectButton(geom=(self.screenImages.find('**/settings'), 
                        self.screenImages.find('**/settings_over'), 
                        self.screenImages.find('**/settings_over'), 
                        self.screenImages.find('**/settings')), frameColor=(1, 1, 1, 0), text_fg=(1, 1, 1, 1),
                     pos=(0.45, 0, -0.1),
                     relief=2, command = self.settings)
        b4.setScale(0.6,1,0.16) 
        self.screenImages=loader.loadModel('./models/gui/exit.egg')
        b5 = DirectButton(geom=(self.screenImages.find('**/exit'), 
                        self.screenImages.find('**/exit_over'), 
                        self.screenImages.find('**/exit_over'), 
                        self.screenImages.find('**/exit')), frameColor=(1, 1, 1, 0), text_fg=(1, 1, 1, 1),
                     pos=(-1.55, 0, -0.35),
                     relief=2, command = sys.exit)
        b5.setScale(0.6,1,0.16) 
            
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