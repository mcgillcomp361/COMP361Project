'''
Created on Feb 21, 2012

@author: Bazibaz
'''
from direct.gui.DirectGui import *
from pandac.PandaModules import *

class GamePanel(): 
    def __init__(self, player): 
        self.mainFrame = DirectFrame(frameColor= (0,0,0,1),
            scale=0.05,
            pos=(0, 0,-0.7),
            sortOrder=2,        
        )   
        geom=OnscreenImage(parent=render2d, image="./models/gui/guiBarV2.png", scale = (1, 1, 0.3), pos = (0,0,-0.7))
        geom.setTransparency(True)  
        self.player = player
        self.loadResources()
        self.loadMiniMap()
        self.playerResources()
        self.loadAbilities()
        self.loadUnits()
        self.loadResearchTree()
        
    def loadResources(self):
        b1 = DirectButton(image = "./models/gui/structures/structure1.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-29.6,0,0.85),borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectForge)
        b2 = DirectButton(image = "./models/gui/structures/structure2.png",frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-28.1,0,0.85), borderWidth = (0.005, 0.005),  text_align = TextNode.ALeft,
                          relief=2, command=self.selectNexus)
        b3 = DirectButton(image = "./models/gui/structures/structure3.png",frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-26.6,0, 0.85), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectExtractor)
        b4 = DirectButton(image = "./models/gui/structures/structure4.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-25.1,0, 0.85), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectPD1)
        b5 = DirectButton(image = "./models/gui/structures/structure5.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-29.6,0, -0.75), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectPhylon)
        b6 = DirectButton(image = "./models/gui/structures/structure6.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-28.1,0, -0.75), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectPD2)
        b7 = DirectButton(image = "./models/gui/structures/structure7.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-29.6,0, -2.3), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectGC)
        b8 = DirectButton(image = "./models/gui/structures/structure8.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-28.1,0, -2.3), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectPD3)
        b9 = DirectButton(image = "./models/gui/structures/structure9.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-29.6,0, -3.90), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectPD4)    
        b1.reparentTo(self.mainFrame)
        b2.reparentTo(self.mainFrame)
        b3.reparentTo(self.mainFrame)
        b4.reparentTo(self.mainFrame)
        b5.reparentTo(self.mainFrame)
        b6.reparentTo(self.mainFrame)
        b7.reparentTo(self.mainFrame)
        b8.reparentTo(self.mainFrame)
        b9.reparentTo(self.mainFrame)
        
    def loadUnits(self):
        b1 = DirectButton(image = "./models/gui/units/unit1.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-21,0,0.85),borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectSwarm)
        b2 = DirectButton(image = "./models/gui/units/unit2.png",frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-19.5,0,0.85), borderWidth = (0.005, 0.005),  text_align = TextNode.ALeft,
                          relief=2, command=self.selectGlobe)
        b3 = DirectButton(image = "./models/gui/units/unit3.png",frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-18,0, 0.85), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectAnalyzer)
        b4 = DirectButton(image = "./models/gui/units/unit4.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-21,0, -0.75), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectSphere)
        b5 = DirectButton(image = "./models/gui/units/unit5.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-19.5,0, -0.75), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectHive)
        b6 = DirectButton(image = "./models/gui/units/unit6.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-21,0, -2.3), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectPlanetarium)
        b7 = DirectButton(image = "./models/gui/units/unit7.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-19.5,0, -2.3), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectMathematica)
        b8 = DirectButton(image = "./models/gui/units/unit8.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-18,0, -2.3), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectBHG)
        b9 = DirectButton(image = "./models/gui/units/unit9.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.65, 1, 0.65), pos=(-21,0, -3.9), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectSwarm) #TODO: reusing swarm here...         
        b1.reparentTo(self.mainFrame)
        b2.reparentTo(self.mainFrame)
        b3.reparentTo(self.mainFrame)
        b4.reparentTo(self.mainFrame)
        b5.reparentTo(self.mainFrame)
        b6.reparentTo(self.mainFrame)
        b7.reparentTo(self.mainFrame)
        b8.reparentTo(self.mainFrame)
        b9.reparentTo(self.mainFrame)
     
    
    def loadAbilities(self):
        #TODO: Julie
        message = "Ability list"   
         
    def playerResources(self):
        resources = OnscreenText(text = 'Resources: ', pos = (1.4, 0.4), scale = 0.7, fg = (1, 1, 1, 1))
        amount = OnscreenText(text = str(self.player.minerals), pos = (7, 0.4), scale = 0.7, fg = (1, 1, 1, 1))
        gEngine = OnscreenText(text = 'Gravity Engines: ', pos = (2, -0.7), scale = 0.7, fg = (1, 1, 1, 1))
        ge_amount = OnscreenText(text = str(self.player.ge_amount), pos = (7, -0.7), scale = 0.7, fg = (1, 1, 1, 1))
        resources.reparentTo(self.mainFrame)
        gEngine.reparentTo(self.mainFrame)
        amount.reparentTo(self.mainFrame)
        ge_amount.reparentTo(self.mainFrame)
      
    def loadResearchTree(self):
        b1 = DirectButton(text = ("Research Tree", "click!", "roll"), pos = (0, 0, -2.4),
                          frameColor=(0, 0,0, 0.2),text_fg=(0,0,0,1), text_scale=0.8, borderWidth = (0.01, 0.01), 
                          text_align = TextNode.ALeft, relief=2, command = self.loadTree)
        b1.reparentTo(self.mainFrame)
    
    def loadTree(self):
        #create a new window for the resource tree
        wp = WindowProperties()
        wp.setSize(400, 300)
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
 
        bk_text = "Research Tree" 
        self.textObject = OnscreenText(parent = aspect2d, text = bk_text, pos = (0.0,0.5), 
                                       scale = 0.17,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1) 
#        window = base.openWindow()

    def loadMiniMap(self):
        #TODO: JULIE
        pass
        
    ## CONSTRUCTION SELECTION
    def selectForge(self):
        self.player.addStructure("forge")
        
    def selectNexus(self):
        print 'selected Nexus'
        
    def selectExtractor(self): 
        print 'selectedExtractor'
        
    def selectPD1(self):
        print 'selected pd1'
        
    def selectPhylon(self):
        print 'selected phylon'
    
    def selectPD2(self):
        print 'selected PD2'
        
    def selectGC(self):
        print 'selected GC'
        
    def selectPD3(self):
        print 'selected PD3'
        
    def selectPD4(self):
        print 'selected PD4'
        
    ## UNIT SELECTION        
    def selectSwarm(self):
        from gameEngine.gameEngine import addUnit
        print 'selected swarm'
        addUnit()
        
    def selectGlobe(self):
        print 'selected globe'
        
    def selectAnalyzer(self):
        print 'selected analyzer'
        
    def selectHorde(self):
        print 'selected horde'
        
    def selectSphere(self):
        print 'selected sphere'
        
    def selectHive(self):
        print 'selected hive'
        
    def selectPlanetarium(self):
        print 'selected planetarium'
        
    def selectMathematica(self):
        print 'selected mathematica'

    def selectBHG(self):
        print 'selected black hole generator'