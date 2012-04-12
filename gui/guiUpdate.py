'''
Created on Mar 12, 2012

@author: Julie
'''

from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.gui.OnscreenImage import OnscreenImage
from gamePanel import GamePanel

class guiUpdate(): 
    def __init__(self, value):

        self.value = value
        self._loadSounds()
        
#        self.screenText = OnscreenText(text='Time: ', pos=(0.8, 0.95), scale=0.05, fg=(1, 1, 1, 1))
#        self.timeValue = OnscreenText(text='  ', pos=(1.0, 0.95), scale=0.05, fg=(1, 1, 1, 1))
        self.image = OnscreenImage(image=("./models/gui/gravsymbol.png"), scale = 0.027, pos=(0.2, 0, -0.735))
        self.image.setTransparency(True)
        self.image = OnscreenImage(image=("./models/gui/Mineral.png"), scale = 0.03, pos=(0.2, 0, -0.655))
        self.image.setTransparency(True)
        self.geAmount = OnscreenText(text=' ', pos=(0.6, -0.75), scale=0.05, fg=(1, 1, 1, 1))
        self.resourceValue = OnscreenText(text='  ', pos=(0.6, -0.67), scale=0.05, fg=(1, 1, 1, 1))
        self.mainFrame = DirectFrame(frameColor= (0,0,0,1),
            scale=0.05,
            pos=(0, 0,-0.7), parent=aspect2d      
        )   
    
    def _loadSounds(self):
        '''
        Method to load sounds.
        '''
        self.mouse_hover = base.loader.loadSfx("sound/effects/mouse_hover/unit_building_hover.wav")
        self.mouse_hover.setLoop(False)
        self.mouse_hover.setVolume(0.2)
        
        self.mouse_click = base.loader.loadSfx("sound/effects/menu/mouse_click.wav")
        self.mouse_click.setVolume(0.2)
            
    def update(self, event):
#        if (event == "updateTime"):          
#            from gameEngine.gameEngine import player
#            if(player.selected_star != None):
#                self.refreshTime() 
#                self.value = player.selected_star.lifetime
#                self.printTime()
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
        if (event == "updateUnits"):
            self.refreshUnits
        if (event == "updateConstructions"):
            self.updateConstructions
            
    def start(self):
#        self.printTime()
        self.printResources()
        self.printGE()
        
#    def refreshTime(self):
#        self.timeValue.remove()

#    def printTime(self):
#        self.timeValue = OnscreenText(text=str(self.value), pos=(1.0, 0.95), scale=0.05, fg=(1, 1, 1, 1))
        
    def refreshResources(self):
        self.resourceValue.remove();  
        
    def printResources(self):      
        self.resourceValue = OnscreenText(text=str(self.value), pos=(0.6, -0.67), scale=0.05, fg=(1, 1, 1, 1))
        
    def refreshGE(self):
        self.geAmount.remove()
        
    def printGE(self):
        self.geAmount = OnscreenText(text=str(self.value), pos=(0.6, -0.75), scale=0.05, fg=(1, 1, 1, 1))

    def refreshUnitsAndConstructions(self, planet):
        #g = None
        
        from gameEngine.gameEngine import gamePanel
        if not planet.activated:
            return
        elif(planet.hasStructure("forge")):
            gamePanel.resetGamePanel()
            gamePanel.hasForge()
            if(planet.player.research.getLevel()>=2):
                gamePanel.unlockTier2Units()
                gamePanel.unlockTier2Structures()
            if(planet.player.research.getLevel()>=3):
                gamePanel.unlockTier3Units()
                gamePanel.unlockTier3Structures()
            if(planet.player.research.getLevel()==4):
                gamePanel.unlockTier4Units()
                gamePanel.unlockTier4Structures()
        else:
            if(planet.player.research.getLevel()>=2):
                gamePanel.unlockTier2Structures()
            if(planet.player.research.getLevel()>=3):
                gamePanel.unlockTier3Structures()
            if(planet.player.research.getLevel()==4):
                gamePanel.unlockTier4Structures()