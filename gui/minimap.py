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
        pos = Vec3(1.3, 0, -0.55)
        self.scale = (350)
        cpos = Vec3(0,0,0)      #center
        mapImage = "models/gui/minimap/minimap.png"
        self.mapRadius = 64
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
        self.playerTargets = []
        self.playerTargets.append([])
        self.opponentTargets = []
        self.opponentTargets.append([])
        self.playerImage = []
        self.playerImage.append("models/gui/minimap/yellowDot.png")
        self.opponentImage = []
        self.opponentImage.append("models/gui/minimap/redDot.png")
        image = OnscreenImage(image = mapImage, scale = self.scale, parent = self.map)
        image.setTransparency(True)
        self.totaltargets = 0
        
    def setTargets(self, playerTargets=None,index=1):
        index = index-1
        if playerTargets is None: pass
        
        for i in range(len(playerTargets)):
            self.playerTargets[index].append(playerTargets([i]))
        for i in range(len(self.playerTargets[index])):
            self.pivot[index].append(self.map.attachNewNode("Player" + str(index)+ "Pivot" + str(i)))
            self.dots[index].append(OnscreenImage(image = self.playerImage[index], scale = 1,pos = (0,0,1), parent = self.pivot[index][i]))
            
    def setPlayerImage(self, index = 1, image = "models/yellowDot.png"): #team must be integer, image must be a path to an image file
        index = index - 1
        self.playerImage[index] = image
        
    def setOpponentImage(self, index = 1, image = "models/redDot.png"): #team must be integer, image must be a path to an image file
        index = index - 1
        self.opponentImage[index] = image
        
    def setScale(self, scale):
        self.scale = scale
        
    def setPos(self,num): #must be a Vec3
        self.pos = num
        
    def setWorldCenter(self, cpos): #must be Vec3
        self.pointer.setPos(cpos)
        
    def appendTarget(self, target = None, team = None): #target must be a nodepath, team must be an integer
        if team is None: team = 1
        team = team - 1
        if target is not None:
            self.targets[team].append(target)
            self.pivot[team].append(self.map.attachNewNode("Team"+str(team)+"Pivot"+str(len(self.targets[team]))))
            x = len(self.targets[team])
            self.dots[team].append(OnscreenImage(image = self.teamImage[team], scale = 1,pos = (0,0,1), parent = self.pivot[team][x]))     
        
    def removeTarget(self, target = None, team = None):
        if team is None: team = 1
        team = team - 1
        
        for i in range(len(self.targets[team])):
            if self.targets[team][i] == target: #This means the object in question is the object to be removed
                self.pivot[team][i].stash() #changed from detachNode()
                self.dots[team][i].stash()
                
    def step(self, task):
        for team in range(len(self.playerTargets)): #will cycle through each team
            for i in range(len(self.playerTargets[team])): #will cycle through each member of the team
                target = self.playerTargets[team][i]
                if target.isEmpty() == False:
                
                    self.pointer.setZ(target.getZ())
                    self.pointer.lookAt(target)
                
                    self.pivot[team][i].setR(-self.pointer.getH())
                    x = self.pointer.getDistance(target)/self.distanceScale  #this scales the real world distance to the scale of the minimap
                    if x != 0:
                        self.pivot[team][i].setScale(x)
                        self.dots[team][i].setScale((1/x)*4)    #the dots representing targets should be 4x4 pixels. (the 1/x) is a necessary hack, don't worry about it.              
        return Task.cont
      