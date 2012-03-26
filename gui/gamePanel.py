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
  
        self.image = OnscreenImage(parent=render2d, image="./models/gui/research_tree.png", scale = (1, 1, 1), pos = (0,0,0))

        #add buttons Tier 1        
        #Add units
        b1 = DirectButton(image = "./models/gui/units/unit1.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(-0.72,0,0.44),borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectSwarm)
        b2 = DirectButton(image = "./models/gui/units/unit2.png",frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(-0.52,0,0.44), borderWidth = (0.005, 0.005),  text_align = TextNode.ALeft,
                          relief=2, command=self.selectGlobe)
        b3 = DirectButton(image = "./models/gui/units/unit3.png",frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(-0.32,0, 0.44), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectAnalyzer)
        #Add abilities      
        #Add constructions
        b4 = DirectButton(image = "./models/gui/structures/structure1.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(0,0,0.44),borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectForge)
        b5 = DirectButton(image = "./models/gui/structures/structure2.png",frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(0.2,0,0.44), borderWidth = (0.005, 0.005),  text_align = TextNode.ALeft,
                          relief=2, command=self.selectNexus)
        b6 = DirectButton(image = "./models/gui/structures/structure3.png",frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(0.4,0, 0.44), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectExtractor)
        b7 = DirectButton(image = "./models/gui/structures/structure4.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(0.6,0, 0.44), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectPD1)
        
        #Tier 2 
        
        #Add Units
        b8 = DirectButton(image = "./models/gui/units/unit4.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(-0.72,0, 0.05), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectSphere)
        b9 = DirectButton(image = "./models/gui/units/unit5.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(-0.52,0, 0.05), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectHive)
        
        #Add Abilities
        
        #Add Constructions
        b10 = DirectButton(image = "./models/gui/structures/structure5.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(0,0, 0.05), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectPhylon)
        b11 = DirectButton(image = "./models/gui/structures/structure6.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(0.2,0, 0.05), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectPD2)
        
        #Tier 3
        
        #Add Units
        b12 = DirectButton(image = "./models/gui/units/unit6.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(-0.72,0, -0.3), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectPlanetarium)
        b13 = DirectButton(image = "./models/gui/units/unit7.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(-0.52,0, -0.3), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectMathematica)
        b14 = DirectButton(image = "./models/gui/units/unit8.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(-0.32,0, -0.3), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectBHG)
        
        #Add Abilities
        #Add Constructions
        b15 = DirectButton(image = "./models/gui/structures/structure7.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(0,0, -0.3), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectGC)
        b16 = DirectButton(image = "./models/gui/structures/structure8.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(0.2,0, -0.3), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectPD3)
        
        #Tier 4
        
        #Add Units
        b17 = DirectButton(image = "./models/gui/units/unit9.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(-0.72,0, -0.7), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectSwarm) #TODO: reusing swarm here...   
        
        #Add Abilities
        #Add Constructions
        b18 = DirectButton(image = "./models/gui/structures/structure9.png", frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          image_scale = (0.08, 1, 0.08), pos=(0,0, -0.7), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectPD4) 
        
        b1.reparentTo(self.image)
        b2.reparentTo(self.image)
        b3.reparentTo(self.image)        
        b4.reparentTo(self.image)
        b5.reparentTo(self.image)
        b6.reparentTo(self.image)
        b7.reparentTo(self.image)
        b8.reparentTo(self.image)
        b9.reparentTo(self.image)
        b10.reparentTo(self.image)
        b11.reparentTo(self.image)
        
        b12.reparentTo(self.image)
        b13.reparentTo(self.image)
        b14.reparentTo(self.image)
        b15.reparentTo(self.image)
        b16.reparentTo(self.image)
        
        b17.reparentTo(self.image)
        b18.reparentTo(self.image)
        
    def loadMiniMap(self):
        #TODO: JULIE
        pass
        
    ## CONSTRUCTION SELECTION
    def selectForge(self):
        self.player.addStructure("forge")
        
    def selectNexus(self):
        self.player.addStructure("nexus")
        
    def selectExtractor(self): 
        self.player.addStructure("extractor")
        
    def selectPhylon(self):
        self.player.addStructure("phylon")
        
    def selectGC(self):
        self.player.addStructure("generatorCore")
        
    def selectPD1(self):
        print 'selected pd1'
    
    def selectPD2(self):
        print 'selected PD2'
        
    def selectPD3(self):
        print 'selected PD3'
        
    def selectPD4(self):
        print 'selected PD4'
        
    ## UNIT SELECTION        
    def selectSwarm(self):
        self.player.addUnit("swarm")
        
    def selectGlobe(self):
        self.player.addUnit("globe")
        
    def selectAnalyzer(self):
        self.player.addUnit("analyzer")
        
    def selectHorde(self):
        self.player.addUnit("horde")
        
    def selectSphere(self):
        self.player.addUnit("sphere")
        
    def selectHive(self):
        self.player.addUnit("hive")
        
    def selectPlanetarium(self):
        self.player.addUnit("planetarium")
        
    def selectMathematica(self):
        self.player.addUnit("mathematica")

    def selectBHG(self):
        self.player.addUnit("blackHoleGenerator")