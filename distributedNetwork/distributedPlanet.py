'''
Created on 2012-04-26

@author: Eran-Tasker
'''
from direct.distributed.DistributedObject import DistributedObject
from pandac.PandaModules import *

from gameModel.solar import Planet

import os

class DistributedPlanet(DistributedObject):
    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self.initialPos = (0,0,0)
        
    def setInitialPos(self, position):
        self.initialPos(position.getX(), position.getY(), position.getZ())
        
    def getInitialPos(self):
        return self.initialPos
    
    def announceGenerate(self):
        DistributedObject.announceGenerate(self)
        x, y, z = self.initialPos
        
    def disable(self):
        DistributedObject.disable(self)
        