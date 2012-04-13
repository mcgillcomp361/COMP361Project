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
        pos = Vec3(1.4, 0, -0.64)
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
        self.dotPlayer = OnscreenImage(image = "models/gui/minimap/Player.png", scale = 3,pos = (base.camera.getX()/self.constant,0,base.camera.getY()/self.constant), parent = self.map)
        self.planetTargets = None
        self.starTargets = None

        image = OnscreenImage(image = mapImage, scale = self.scale, parent = self.map)
        image.setTransparency(True)

        
    def setTargets(self, planetTargets=None,starTargets=None):
        self.planetTargets = planetTargets
        if planetTargets is None: pass
        for i in range(len(self.planetTargets)):
            star = self.planetTargets[i].parent_star.point_path
            x = (self.planetTargets[i].point_path.getX() + star.getX())/self.constant
            y = (self.planetTargets[i].point_path.getY() + star.getY())/self.constant
            z = (self.planetTargets[i].point_path.getZ() + star.getZ())/self.constant
            self.dots.append(OnscreenImage(image = "models/gui/minimap/whiteDot.png", scale = 3,pos = (x,0,y), parent = self.map))
        if starTargets is None: pass   
        for i in range(len(starTargets)):
            x = starTargets[i].point_path.getX()/self.constant
            y = starTargets[i].point_path.getY()/self.constant
            z = starTargets[i].point_path.getZ()/self.constant
            self.dots.append(OnscreenImage(image = "models/gui/minimap/redDot.png", scale = 6,pos = (x,0,y), parent = self.map))
    
    def step(self, task):
        self.dotPlayer.destroy()
        x = base.camera.getX()
        y = base.camera.getY()
        if (x < -3251): x = -3251
        if (x > 3000): x= 3000
        if (y < -6200): y = -6200
        if (y > 6258): y = 6258

        self.dotPlayer = OnscreenImage(image = "models/gui/minimap/Player.png", scale = 5,pos = (-1*x/self.constant,0,y/(-2*self.constant)), parent = self.map)        
        self.dotPlayer.setTransparency(1)
        return Task.cont
      