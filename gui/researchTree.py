'''
Created on Mar 30, 2012

@author: Julie
'''

from direct.gui.DirectGui import *
from pandac.PandaModules import *

class ResearchTree():
    
    def __init__(self):
        pass
     
    def loadTree(self):            
        
        wp = WindowProperties()
        wp.setSize(300, 500)
        wp.setOrigin(879, 200)
        controlwin = base.openWindow(props = wp, aspectRatio = 1.33)
        
        # Setup a render2d and aspect2d for the new window. 
        render2d = NodePath('render2d') 
        render2d.setDepthTest(0) 
        render2d.setDepthWrite(0) 
        camera2d = base.makeCamera2d(controlwin) 
        camera2d.reparentTo(render2d) 
        aspectRatio = 1.33
        aspect2d = render2d.attachNewNode(PGTop("aspect2d")) 
        aspect2d.setScale(1.0 / aspectRatio, 1.0, 1.0) 
        
        self.image = OnscreenImage(parent=render2d, image="./models/gui/research_tree.png", scale = (1, 1, 1), pos = (0,0,0))
        
        #title
        b1 = DirectButton(text = ("Research Tree", "click!", "roll"), pos = (-0.4, 0, 0.8),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, text_align = TextNode.ALeft, relief=2)
        
        #Tier 1 abilities
        b2 = DirectButton(text = ("Capture", "click!", "roll"), pos = (-0.6, 0, 0.4),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, text_align = TextNode.ALeft, relief=2)
        b3 = DirectButton(text = ("Cloak", "click!", "roll"), pos = (-0.1, 0, 0.4),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, text_align = TextNode.ALeft, relief=2)
        b4 = DirectButton(text = ("Vision", "click!", "roll"), pos = (0.4, 0, 0.4),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, text_align = TextNode.ALeft, relief=2)
        
        #Tier 2 abilities
        
        b5 = DirectButton(text = ("Burrow", "click!", "roll"), pos = (-0.6, 0, 0),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, text_align = TextNode.ALeft, relief=2)
        b6 = DirectButton(text = ("Healing Aura", "click!", "roll"), pos = (-0.1, 0, 0),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, text_align = TextNode.ALeft, relief=2)
        
        #Tier 3 abilities
        b7 = DirectButton(text = ("Harvest", "click!", "roll"), pos = (-0.6, 0, -0.4),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, text_align = TextNode.ALeft, relief=2)
        b8 = DirectButton(text = ("Ring of Fire", "click!", "roll"), pos = (-0.1, 0, -0.4),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, text_align = TextNode.ALeft, relief=2)
        b9 = DirectButton(text = ("Control Wave", "click!", "roll"), pos = (0.4, 0, -0.4),
                          frameColor=(0,0,0,0),text_fg=(1,1,1,1), text_scale=0.08, text_align = TextNode.ALeft, relief=2)
        
        #Tier 4 abilities
        
        
        b1.reparentTo(self.image)
        b2.reparentTo(self.image)
        b3.reparentTo(self.image)
        b4.reparentTo(self.image)
        b5.reparentTo(self.image)
        b6.reparentTo(self.image)   
        b7.reparentTo(self.image)
        b8.reparentTo(self.image)
        b9.reparentTo(self.image)
            
        #Add tier buttons
        
        #Add abilities buttons
        
        #Tier 1 
        