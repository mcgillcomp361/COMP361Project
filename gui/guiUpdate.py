'''
Created on Mar 12, 2012

@author: Julie
'''
from direct.gui.DirectGui import *
from pandac.PandaModules import *

class guiUpdate(): 
    def __init__(self, value):

        self.value = value;
        self.screenText = OnscreenText(text='Time: ', pos=(0.8, 0.95), scale=0.05, fg=(1, 1, 1, 1))
        self.timeValue = OnscreenText(text='  ', pos=(1.0, 0.95), scale=0.05, fg=(1, 1, 1, 1))
        self.resources = OnscreenText(text='Minerals: ', pos=(0.1, -0.67), scale=0.05, fg=(1, 1, 1, 1))
        self.resourceValue = OnscreenText(text='  ', pos=(0.4, -0.67), scale=0.05, fg=(1, 1, 1, 1))
        self.ge = OnscreenText(text='Gravity Engines: ', pos=(0.12, -0.75), scale=0.05, fg=(1, 1, 1, 1))
        self.geAmount = OnscreenText(text=' ', pos=(0.4, -0.75), scale=0.05, fg=(1, 1, 1, 1))
        
    def update(self, event):
        if (event == "updateTime"):
            self.refreshTime()            
            from gameEngine.gameEngine import player
            self.value = player.selected_star.lifetime
            self.printTime()
        if (event == "updateMinerals"):
            self.refreshResources()
            from gameEngine.gameEngine import player
            self.value = player.minerals
            self.printResources()
        if (event == "updateGE"):
            self.refreshGE()
            from gameEngine.gameEngine import player
            self.value = player.ge_amount
            self.printGE()
            
    def start(self):
        self.printTime()
        self.printResources()
        self.printGE()
        
    def refreshTime(self):
        self.timeValue.remove()

    def printTime(self):
        self.timeValue = OnscreenText(text=str(self.value), pos=(1.0, 0.95), scale=0.05, fg=(1, 1, 1, 1))
        
    def refreshResources(self):
        self.resourceValue.remove();  
        
    def printResources(self):      
        self.resourceValue = OnscreenText(text=str(self.value), pos=(0.4, -0.67), scale=0.05, fg=(1, 1, 1, 1))
        
    def refreshGE(self):
        self.geAmount.remove()
        
    def printGE(self):
        self.geAmount = OnscreenText(text=str(self.value), pos=(0.4, -0.75), scale=0.05, fg=(1, 1, 1, 1))