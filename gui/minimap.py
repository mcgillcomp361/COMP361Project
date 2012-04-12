'''
Created on Mar 31, 2012

@author: Bazibaz
'''

from direct.gui.OnscreenImage import OnscreenImage 
from direct.gui.DirectGui import * 
from direct.showbase.DirectObject import DirectObject 
from pandac.PandaModules import *
from direct.task import Task

class Minimap():
    image = None   
    texture = None  
    map = None     
    onscreen = None
    
    def __init__(self):
        taskMgr.add(self.step,"MinimapTask") 
        x = base.win.getXSize()*0.0016
        pos = Vec3(x, 0, -0.65)
        self.scale = (180)
        self.constant = 22
        cpos = Vec3(0,0,0)      #center
        mapImage = "models/gui/minimap/minimap.png"
        self.mapRadius = 75
        self.distanceScale = (20*self.mapRadius/self.scale)
        self.map = aspect2d.attachNewNode('Map')
        
        props = base.win.getProperties()
        self.Height = float(props.getYSize())
        self.Hscale = (1/self.Height)
        
        self.map.setScale(self.Hscale)  
        self.map.setPos(pos)

        self.dots = []
        self.dots.append([])
        self.planetTargets = []
        self.planetTargets.append([])
        self.starTargets = []
        self.starTargets.append([])

        image = OnscreenImage(image = mapImage, scale = self.scale, parent = self.map)
        image.setTransparency(True)
        self.totaltargets = 0
        
    def setTargets(self, playerTargets=None,starTargets=None):
       
        if starTargets is None: pass   
        for i in range(len(starTargets)):
            x = starTargets[i].point_path.getX()/self.constant
            y = starTargets[i].point_path.getY()/self.constant
            z = starTargets[i].point_path.getZ()/self.constant
            self.dots.append(OnscreenImage(image = "models/gui/minimap/redDot.png", scale = 5,pos = (x,0,y), parent = self.map))
        if playerTargets is None: pass
        for i in range(len(playerTargets)):
            star = playerTargets[i].parent_star.point_path
            x = (playerTargets[i].point_path.getX() + star.getX())/self.constant
            y = (playerTargets[i].point_path.getY() + star.getY())/self.constant
            z = (playerTargets[i].point_path.getZ() + star.getZ())/self.constant
            self.dots.append(OnscreenImage(image = "models/gui/minimap/whiteDot.png", scale = 3,pos = (x,0,y), parent = self.map))
    
    def step(self, task):
        return Task.cont
      