'''
Created on Mar 31, 2012

@author: Bazibaz
'''

from direct.gui.OnscreenImage import OnscreenImage 
from direct.gui.DirectGui import * 
from direct.showbase.DirectObject import DirectObject 
from pandac.PandaModules import *
from pandac.PandaModules import PNMImage

class Minimap():
    image = None   
    texture = None  
    map = None     
    onscreen = None
    
    def __init__(self):
     #   taskMgr.add(self.step,"MinimapTask") 
        pos = Vec3(1.3, 0, -0.55)
        self.scale = (350)
        cpos = Vec3(0,0,0)      #center
        mapImage = "models/gui/minimap.png"
        self.mapRadius = 64
        self.spin = False
        self.distanceScale = (18.75*self.mapRadius/self.scale)
        
        self.map = aspect2d.attachNewNode('Map')
        
        props = base.win.getProperties()
        self.Height = float(props.getYSize())
        self.Hscale = (1/self.Height)
        
        self.map.setScale(self.Hscale)  
        self.map.setPos(pos)
        self.pointer = render.attachNewNode('pointer')
        self.pointer.setPos(cpos)
        self.pivot = []
        self.pivot.append([])
        self.dots = []
        self.dots.append([])
        self.targets = []
        self.targets.append([])
        self.teamImage = []
        #self.teamImage.append("models/gui/dot.png")
        image = OnscreenImage(image = mapImage, scale = self.scale, parent = self.map)
        image.setTransparency(True)
        self.totaltargets = 0
      