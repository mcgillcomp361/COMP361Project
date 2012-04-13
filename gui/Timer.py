'''
Created on Mar 12, 2012

@author: Julie
'''
from direct.gui.DirectGui import *
from pandac.PandaModules import *

class Timer(): 
    def __init__(self, star): 
        self.star = star;
#        x = self.star.position.getX()
#        y = self.star.position.getY()
#        self.screenText = OnscreenText(text='Time: ', pos=(0.8, 0.95), scale=0.05, fg=(1, 1, 1, 1))
 #       self.timeValue = OnscreenText(text='  ', pos=(1.0, 0.95), scale=0.05, fg=(1, 1, 1, 1))
        
    def refresh(self):
        self.timeValue.remove()

    def printTime(self):
#        x = self.star.position.getX()
#        y = self.star.position.getY()
        self.timeValue = OnscreenText(text=str(self.star.lifetime), pos=(1.0, 0.95), scale=0.05, fg=(1, 1, 1, 1))