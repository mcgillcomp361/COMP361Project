'''
Created on Feb 21, 2012

@author: Bazibaz
'''
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from researchTree import ResearchTree
from minimap import Minimap
from gameModel.solar import Planet

class GamePanel(): 
    def __init__(self, player): 
        self.mainFrame = DirectFrame(frameColor= (0,0,0,1),
            scale=0.05,
            pos=(0, 0,-0.7),
            sortOrder=2,        
        )   
        self.planets = []
        self._loadSounds()
        self.player = player
        self.researchTree = ResearchTree()
        self.loadUnits()
        self.loadResources()
        self.loadMiniMap()
        self.loadResearchTree()
        geom=OnscreenImage(parent=render2d, image="./models/gui/guiBar.png", scale = (1, 1, 0.3), pos = (0,0,-0.7))
        geom.setTransparency(True)  
        
    def _loadSounds(self):
        '''
        Method to load sounds.
        '''
        self.mouse_hover = base.loader.loadSfx("sound/effects/mouse_hover/unit_building_hover.wav")
        self.mouse_hover.setLoop(False)
        self.mouse_hover.setVolume(0.2)
        
        self.mouse_click = base.loader.loadSfx("sound/effects/menu/mouse_click.wav")
        self.mouse_click.setVolume(0.2)
    
    def loadResources(self):
        
        b1 = DirectButton(image = ("./models/gui/structures/forge.png", "./models/gui/structures/forge.png", 
                                   "./models/gui/structures/forge_hover.png"), frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-29.6,0,0.85), command=self.selectForge, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        b1.stateNodePath[2].setTransparency(1)
        b1.stateNodePath[2].setScale(15, 1, 5)
        b1.stateNodePath[2].setPos(9, 0, 2)
                    
        b2 = DirectButton(image = ("./models/gui/structures/nexus.png", "./models/gui/structures/nexus.png",
                          "./models/gui/structures/nexus_hover.png"), frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-28.1,0,0.85), command=self.selectNexus, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        b2.stateNodePath[2].setTransparency(1)
        b2.stateNodePath[2].setScale(15, 1, 5)
        b2.stateNodePath[2].setPos(9, 0, 2)
        
        b3 = DirectButton(image = ("./models/gui/structures/extractor.png","./models/gui/structures/extractor.png",
                                   "./models/gui/structures/extractor_hover.png"),frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-26.6,0, 0.85), command=self.selectExtractor, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        b3.stateNodePath[2].setTransparency(1)
        b3.stateNodePath[2].setScale(15, 1, 5)
        b3.stateNodePath[2].setPos(9, 0, 1)
        
        b4 = DirectButton(image = ("./models/gui/structures/pd1.png", "./models/gui/structures/pd1.png",
                                   "./models/gui/structures/pd1_hover.png"),frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-25.1,0, 0.85), command=self.selectPD1, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        b4.stateNodePath[2].setTransparency(1)
        b4.stateNodePath[2].setScale(15, 1, 5)
        b4.stateNodePath[2].setPos(9, 0, 1)
        
        b5 = DirectButton(image = ("./models/gui/structures/phylon.png","./models/gui/structures/phylon.png",
                                    "./models/gui/structures/phylon_hover.png"), frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-29.6,0, -0.75), command=self.selectPhylon, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        b5.stateNodePath[2].setTransparency(1)
        b5.stateNodePath[2].setScale(15, 1, 5)
        b5.stateNodePath[2].setPos(9, 0, 1)
        
        b6 = DirectButton(image = ("./models/gui/structures/pd2.png", "./models/gui/structures/pd2.png",
                                   "./models/gui/structures/pd2_hover.png"),frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-28.1,0, -0.75), command=self.selectPD2, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        b6.stateNodePath[2].setTransparency(1)
        b6.stateNodePath[2].setScale(15, 1, 5)
        b6.stateNodePath[2].setPos(9, 0, 1)             
        
        b7 = DirectButton(image = ("./models/gui/structures/gc.png", "./models/gui/structures/gc.png",
                                   "./models/gui/structures/gc_hover.png"), frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-29.6,0, -2.3), command=self.selectGC, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        b7.stateNodePath[2].setTransparency(1)
        b7.stateNodePath[2].setScale(15, 1, 5)
        b7.stateNodePath[2].setPos(10, 0, 1)
        
        b8 = DirectButton(image = ("./models/gui/structures/pd3.png", "./models/gui/structures/pd3.png",
                                   "./models/gui/structures/pd3_hover.png"),frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-28.1,0, -2.3), command=self.selectPD3, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        b8.stateNodePath[2].setTransparency(1)
        b8.stateNodePath[2].setScale(15, 1, 5)
        b8.stateNodePath[2].setPos(10, 0, 1)
        
        b9 = DirectButton(image = ("./models/gui/structures/pd4.png", "./models/gui/structures/pd4.png",
                                   "./models/gui/structures/pd4_hover.png"), frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-29.6,0, -3.90), command=self.selectPD4, clickSound=self.mouse_click, rolloverSound=self.mouse_hover) 
        b9.stateNodePath[2].setTransparency(1)
        b9.stateNodePath[2].setScale(15, 1, 5)
        b9.stateNodePath[2].setPos(10, 0, 1)
           
        b4.reparentTo(self.mainFrame)
        b3.reparentTo(self.mainFrame)
        b2.reparentTo(self.mainFrame)
        b1.reparentTo(self.mainFrame)
        b6.reparentTo(self.mainFrame)
        b5.reparentTo(self.mainFrame)
        b8.reparentTo(self.mainFrame)
        b7.reparentTo(self.mainFrame)
        b9.reparentTo(self.mainFrame)
        
    def loadUnits(self):
        b1 = DirectButton(image = ("./models/gui/units/swarm.png", "./models/gui/units/swarm.png","./models/gui/units/swarm_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-21,0,0.85), command=self.selectSwarm, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        b1.stateNodePath[2].setTransparency(1)
        b1.stateNodePath[2].setScale(15, 1, 5)
        b1.stateNodePath[2].setPos(10, 0, 2)
        
        b2 = DirectButton(image = ("./models/gui/units/globe.png", "./models/gui/units/globe.png", "./models/gui/units/globe_hover.png"), 
                          frameColor=(0, 0,0, 0),image_scale = (0.65, 1, 0.65), pos=(-19.5,0,0.85), command=self.selectGlobe, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        b2.stateNodePath[2].setTransparency(1)
        b2.stateNodePath[2].setScale(15, 1, 5)
        b2.stateNodePath[2].setPos(10, 0, 2)
        
        b3 = DirectButton(image = ("./models/gui/units/analyzer.png", "./models/gui/units/analyzer.png", "./models/gui/units/analyzer_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-18,0, 0.85), command=self.selectAnalyzer, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        b3.stateNodePath[2].setTransparency(1)
        b3.stateNodePath[2].setScale(15, 1, 5)
        b3.stateNodePath[2].setPos(10, 0, 2)
        
        b4 = DirectButton(image = ("./models/gui/units/horde.png", "./models/gui/units/horde.png", "./models/gui/units/horde_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-21,0, -0.75), command=self.selectHorde, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        b4.stateNodePath[2].setTransparency(1)
        b4.stateNodePath[2].setScale(15, 1, 5)
        b4.stateNodePath[2].setPos(10, 0, 3)
        
        b5 = DirectButton(image = ("./models/gui/units/sphere.png", "./models/gui/units/sphere.png", "./models/gui/units/sphere_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-19.5,0, -0.75), command=self.selectSphere, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        b5.stateNodePath[2].setTransparency(1)
        b5.stateNodePath[2].setScale(15, 1, 5)
        b5.stateNodePath[2].setPos(10, 0, 3)
        
        bGravity = DirectButton(image = ("./models/gui/units/gravityEngine.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-18,0, -0.75), relief=2, command=self.selectGravityEngine, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        bGravity.setTransparency(1)
        
        b6 = DirectButton(image = ("./models/gui/units/hive.png", "./models/gui/units/hive.png","./models/gui/units/hive_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-21,0, -2.3),command=self.selectHive, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        b6.stateNodePath[2].setTransparency(1)
        b6.stateNodePath[2].setScale(15, 1, 5)
        b6.stateNodePath[2].setPos(10, 0, 3)
        
        b7 = DirectButton(image = ("./models/gui/units/planetarium.png", "./models/gui/units/planetarium.png","./models/gui/units/planetarium_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-19.5,0, -2.3), command=self.selectPlanetarium, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        b7.stateNodePath[2].setTransparency(1)
        b7.stateNodePath[2].setScale(15, 1, 5)
        b7.stateNodePath[2].setPos(10, 0, 3)        
        
        b8 = DirectButton(image = ("./models/gui/units/mathematica.png","./models/gui/units/mathematica.png","./models/gui/units/mathematica_hover.png"), 
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-18,0, -2.3), command=self.selectMathematica, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        b8.stateNodePath[2].setTransparency(1)
        b8.stateNodePath[2].setScale(15, 1, 5)
        b8.stateNodePath[2].setPos(10, 0, 3) 
        
        b9 = DirectButton(image = ("./models/gui/units/bhg.png","./models/gui/units/bhg.png","./models/gui/units/bhg_hover.png"), 
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-21,0, -3.9), command=self.selectBHG, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)         
        b9.stateNodePath[2].setTransparency(1)
        b9.stateNodePath[2].setScale(15, 1, 5)
        b9.stateNodePath[2].setPos(10, 0, 2) 
        #Rendering order matters
        b3.reparentTo(self.mainFrame)
        b2.reparentTo(self.mainFrame)
        b1.reparentTo(self.mainFrame)
        b5.reparentTo(self.mainFrame)
        b4.reparentTo(self.mainFrame)
        b8.reparentTo(self.mainFrame)
        b7.reparentTo(self.mainFrame)
        b6.reparentTo(self.mainFrame)
        b9.reparentTo(self.mainFrame)
        bGravity.reparentTo(self.mainFrame)
      
    def loadResearchTree(self):
        b1 = DirectButton(image = ("./models/gui/ResearchButton.png"), pos = (7, 0, -3),
                          frameColor=(0, 0,0, 0),image_scale = (4, 1, 1.5), command = self.researchTree.loadTree)
        b1.stateNodePath[0].setTransparency(1)
        b1.stateNodePath[1].setTransparency(1)
        b1.stateNodePath[2].setTransparency(1)
        b1.reparentTo(self.mainFrame)
            
    def loadMiniMap(self):
        #TODO: Finish Minimap
        self.targets = []
 #       for planets in self.player.planets:
 #           self.targets.append(self.planets.planet)
        self.map = Minimap()
       
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
    
    def selectGravityEngine(self):
        self.player.addUnit("gravityEngine")
