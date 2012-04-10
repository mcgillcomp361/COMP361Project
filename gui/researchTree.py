'''
Created on Mar 30, 2012

@author: Julie
'''

from direct.gui.DirectGui import *
from pandac.PandaModules import *
from gameModel.constants import TIER_II_RESEARCH_TIME, TIER_III_RESEARCH_TIME, TIER_IV_RESEARCH_TIME

class ResearchTree():
    
    def __init__(self, player):
        self.player = player
        self.research_task = None
     
    def loadTree(self):            
               
        wp = WindowProperties()
        wp.setSize(300, 500)
        wp.setOrigin(879, 200)
        win = base.openWindow(props = wp, aspectRatio = 1.33)
        
        # Setup a render2d and aspect2d for the new window. 
        myRender = NodePath('myRender') 
        base.camList[-1].reparentTo(myRender)
        
        # Set up a 2-d scene for GUI objects in this window. 
        myRender2d = NodePath('myRender2d') 
        myCamera2d = base.makeCamera2d(win) 
        myCamera2d.reparentTo(myRender2d)
        
        # Turn off certain rendering attributes that are inappropriate for 2-d 
        # objects. 
        myRender2d.setDepthWrite(0) 
        myRender2d.setMaterialOff(1) 
        myRender2d.setTwoSided(1)
       
        # Force the window to be open now. 
        base.graphicsEngine.openWindows() 
         
        # Set up an aspect2d node on this new window, which serves as the root 
        # of all DirectGui items.  
        mk = base.dataRoot.attachNewNode(MouseAndKeyboard(win, 0, 'myWindowMouse')) 
        mw = mk.attachNewNode(MouseWatcher('mw')) 
        myAspect2d = myRender2d.attachNewNode(PGTop('myAspect2d')) 
        myAspect2d.node().setMouseWatcher(mw.node()) 
        
        self.image = OnscreenImage(parent=myRender2d, image="./models/gui/researchTree/research_tree.png", scale = (1, 1, 1), pos = (0,0,0))
        
        self.tier1 = OnscreenImage(parent = myRender2d, image = ("./models/gui/researchTree/tier1.png"), pos = (0, 0, 0.7), scale = (0.4, 1, 0.05))
        self.tier2 = DirectButton(parent = myAspect2d, image = ("./models/gui/researchTree/tier2.png"), pos = (0, 0, 0.3),
                          frameColor=(0, 0,0, 0),image_scale = (0.4, 1, 0.05), command = self.selectTier2)
        self.tier3 = DirectButton(parent = myAspect2d, image = ("./models/gui/researchTree/tier3.png"), pos = (0, 0, -0.15),
                          frameColor=(0, 0,0, 0),image_scale = (0.4, 1, 0.05), command = self.selectTier3)
        self.tier4 = DirectButton(parent = myAspect2d, image = ("./models/gui/researchTree/tier4.png"), pos = (0, 0, -0.55),
                          frameColor=(0, 0,0, 0),image_scale = (0.4, 1, 0.05), command = self.selectTier4)        

        #Tier 1 abilities
        self.b1 = DirectButton(parent = myAspect2d, text = ("Capture", "click!", "roll"), pos = (-0.6, 0, 0.4),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, relief=2, command=self.selectCapture)   
        self.b2 = DirectButton(parent = myAspect2d, text = ("Cloak", "click!", "roll"), pos = (-0.1, 0, 0.4),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, relief=2, command=self.selectCloak)
        self.b3 = DirectButton(parent = myAspect2d, text = ("Vision", "click!", "roll"), pos = (0.4, 0, 0.4),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, relief=2, command=self.selectVision)
        
        #Tier 2 abilities
        
        self.b4 = DirectButton(parent = myAspect2d, text = ("Burrow", "click!", "roll"), pos = (-0.6, 0, 0),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, relief=2, command=self.selectBurrow)
        self.b5 = DirectButton(parent = myAspect2d, text = ("Healing Aura", "click!", "roll"), pos = (-0.1, 0, 0),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, relief=2, command=self.selectHealingAura)
        
        #Tier 3 abilities
        self.b6 = DirectButton(parent = myAspect2d, text = ("Harvest", "click!", "roll"), pos = (-0.6, 0, -0.4),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, relief=2, command=self.selectHarvest)
        self.b7 = DirectButton(parent = myAspect2d, text = ("Ring of Fire", "click!", "roll"), pos = (-0.1, 0, -0.4),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, relief=2, command=self.selectRingOfFire)
        self.b8 = DirectButton(parent = myAspect2d, text = ("Control Wave", "click!", "roll"), pos = (0.4, 0, -0.4),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, relief=2, command=self.selectControlWave)
        
        #Tier 4 abilities
        self.b9 = DirectButton(parent = myAspect2d, text = ("Generate Black Hole", "click!", "roll"), pos = (-0.2, 0, -0.8),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, relief=2, command=self.selectGBH)

    def selectTier2(self):
        print self.player.research.getLevel()
        if(self.player.research.getLevel() == 1 and self.research_task == None):
            self.research_task = taskMgr.doMethodLater(TIER_II_RESEARCH_TIME, self.player.research.incrementLevel, 'researchTireII')
            print 'tier 2'
    
    def selectTier3(self):
        if(self.player.research.getLevel() == 2 and self.research_task == None):
            self.research_task = taskMgr.doMethodLater(TIER_III_RESEARCH_TIME, self.player.research.incrementLevel, 'researchTireIII')
            print 'tier 3'
        
    def selectTier4(self):
        if(self.player.research.getLevel() == 3 and self.research_task == None):
            self.research_task = taskMgr.doMethodLater(TIER_IV_RESEARCH_TIME, self.player.research.incrementLevel, 'researchTireIV')
            print 'tier 4'
            
    def selectCapture(self): 
        pass
    
    def selectCloak(self): 
        pass
    
    def selectVision(self): 
        pass
    
    def selectBurrow(self): 
        pass
    
    def selectHealingAura(self): 
        pass
    
    def selectHarvest(self): 
        pass
    
    def selectRingOfFire(self): 
        pass
    
    def selectControlWave(self): 
        pass 

    def selectGBH(self): 
        pass     