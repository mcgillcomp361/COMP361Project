'''
Created on Feb 21, 2012

@author: Bazibaz
'''
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from researchTree import ResearchTree
from gameModel.solar import Planet

class GamePanel(): 
    
    def __init__(self, player): 
        self.mainFrame = DirectFrame(frameColor= (0,0,0,1),
            scale=0.05,
            pos=(0, 0,-0.7),
            sortOrder=2,        
        )   
        self._loadSounds()
        self.player = player
        self.planet = None

        self.researchTree = ResearchTree(self.player)
        
        self.ub1 = None
        self.ub2 = None
        self.ub3 = None
        self.ub4 = None
        self.ub5 = None
        self.ub6 = None
        self.ub7 = None
        self.ub8 = None
        self.ub9 = None
        self.ubGravity = None
        self.fub1 = None
        self.fub2 = None
        self.fub3 = None
        self.fub4 = None
        self.fub5 = None
        self.fub6 = None
        self.fub7 = None
        self.fub8 = None
        self.fub9 = None
        self.fubGravity = None
        self.phylon = None
        self.gc = None
        self.pd2 = None
        self.pd3 = None
        self.pd4 = None
        
        
        #StructurePanel buttons
        self.spb1 = None
        self.spb2 = None
        self.spb3 = None
        self.spb4 = None
        
        self.loadUnits()
        self.loadResources()
        self.loadResearchTree()
#        self.b1 = DirectButton(image = ("./models/gui/structures/forge.png", "./models/gui/structures/forge.png", 
#                                   "./models/gui/structures/forge_hover.png"), frameColor=(0, 0,0, 0),
#                          image_scale = (0.65, 1, 0.65), pos=(-29.6,0,0.85), command=self.selectForge, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        geom=OnscreenImage(parent=render2d, image="./models/gui/guiBar.png", scale = (1, 1, 0.3), pos = (0,0,-0.7))
        geom.setTransparency(True)  
        
    def resetStructurePanel(self):
        if (self.spb1 != None):
            self.spb1.destroy()
        if (self.spb2 != None):
            self.spb2.destroy()
        if (self.spb3 != None):
            self.spb3.destroy()
        if (self.spb4 != None):
            self.spb4.destroy()
            
    def paintStructurePanel(self, planet):
        if planet.hasStructure("forge"):
            self.spb1 = OnscreenImage(image = "./models/gui/structures/forge.png", parent = self.mainFrame,
                          scale = (1.5, 1, 1.5), pos=(-10.5,0,-0.5))
        if (planet.hasStructure("nexus")):
            self.spb2 = OnscreenImage(image = "./models/gui/structures/nexus.png", parent = self.mainFrame,
                          scale = (1.5, 1, 1.5), pos=(-7.25,0,-0.5))
        if (planet.hasStructure("extractor")):
            self.spb3 = OnscreenImage(image = "./models/gui/structures/extractor.png", parent = self.mainFrame,
                          scale = (1.5, 1, 1.5), pos=(-4,0,-0.5))
        if (planet.hasStructure("pd1")):
            self.spb4 = OnscreenImage(image = "./models/gui/structures/pd1.png", parent = self.mainFrame,
                          scale = (1.5, 1, 1.5), pos=(-0.75,0,-0.5))
        if (planet.hasStructure("phylon")):
            self.spb5 = OnscreenImage(image = "./models/gui/structures/phylon.png", parent = self.mainFrame,
                          scale = (1.5, 1, 1.5), pos=(-0.4,0,-0.5))
        if (planet.hasStructure("pd2")):
            self.spb6 = OnscreenImage(image = "./models/gui/structures/pd2.png", parent = self.mainFrame,
                          scale = (1.5, 1, 1.5), pos=(-0.75,0,-0.5))
        if (planet.hasStructure("gc")):
            self.spb7 = OnscreenImage(image = "./models/gui/structures/gc.png", parent = self.mainFrame,
                          scale = (1.5, 1, 1.5), pos=(-0.4,0,-0.5))
        if (planet.hasStructure("pd3")):
            self.spb8 = OnscreenImage(image = "./models/gui/structures/pd3.png", parent = self.mainFrame,
                          scale = (1.5, 1, 1.5), pos=(-0.75,0,-0.5))
        if (planet.hasStructure("pd4")):
            self.spb9 = OnscreenImage(image = "./models/gui/structures/pd4.png", parent = self.mainFrame,
                          scale = (1.5, 1, 1.5), pos=(-0.75,0,-0.5)) 
            
    def resetGamePanel(self):
        if(self.ub1 != None):
            self.ub1.destroy()
        if(self.ub2 != None):
            self.ub2.destroy()
        if(self.ub3 != None):
            self.ub3.destroy()
        if(self.ub4 != None):
            self.ub4.destroy()
        if(self.ub5 != None):
            self.ub5.destroy()
        if(self.ub6 != None):
            self.ub6.destroy()
        if(self.ub7 != None):
            self.ub7.destroy()
        if(self.ub8 != None):
            self.ub8.destroy()
        if(self.ub9 != None):
            self.ub9.destroy()
        if(self.ubGravity != None):
            self.ubGravity.destroy()
        if(self.fub1 != None):
            self.fub1.destroy()
        if(self.fub2 != None):
            self.fub2.destroy()
        if(self.fub3 != None):
            self.fub3.destroy()
        if(self.fub4 != None):
            self.fub4.destroy()
        if(self.fub5 != None):
            self.fub5.destroy()
        if(self.fub6 != None):
            self.fub6.destroy()
        if(self.fub7 != None):
            self.fub7.destroy()
        if(self.fub8 != None):
            self.fub8.destroy()
        if(self.fub9 != None):
            self.fub9.destroy()
        if(self.sb1 != None):
            self.sb1.destroy()
        if(self.sb2 != None):
            self.sb2.destroy()
        if(self.sb3 != None):
            self.sb3.destroy()
        if(self.sb4 != None):
            self.sb4.destroy()
        if(self.sb5 != None):
            self.sb5.destroy()
        if(self.sb6 != None):
            self.sb6.destroy()
        if(self.sb7 != None):
            self.sb7.destroy()
        if(self.sb8 != None):
            self.sb8.destroy()
        if(self.sb9 != None):
            self.sb9.destroy()
        if(self.phylon != None):
            self.phylon.destroy()
        if(self.gc != None):
            self.gc.destroy()
        if(self.pd2 != None):
            self.pd2.destroy()
        if(self.pd3 != None):
            self.pd2.destroy()
        if(self.pd4 != None):
            self.pd2.destroy()
        if(self.fubGravity != None):
            self.fubGravity.destroy()
        self.loadUnits()
        self.loadResources()
        
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
        self.sb1 = DirectButton(image = ("./models/gui/structures/forge_locked.png", "./models/gui/structures/forge_locked.png", 
                                   "./models/gui/structures/forge_hover.png"), frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-29.6,0,0.85), command=self.selectForge, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.sb1.stateNodePath[2].setTransparency(1)
        self.sb1.stateNodePath[2].setScale(15, 1, 5)
        self.sb1.stateNodePath[2].setPos(8, 0, 3.5)
                    
        self.sb2 = DirectButton(image = ("./models/gui/structures/nexus_locked.png", "./models/gui/structures/nexus_locked.png",
                          "./models/gui/structures/nexus_hover.png"), frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-28.1,0,0.85), command=self.selectNexus, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.sb2.stateNodePath[2].setTransparency(1)
        self.sb2.stateNodePath[2].setScale(15, 1, 5)
        self.sb2.stateNodePath[2].setPos(8, 0, 3.5)
        
        self.sb3 = DirectButton(image = ("./models/gui/structures/extractor_locked.png","./models/gui/structures/extractor_locked.png",
                                   "./models/gui/structures/extractor_hover.png"),frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-26.6,0, 0.85), command=self.selectExtractor, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.sb3.stateNodePath[2].setTransparency(1)
        self.sb3.stateNodePath[2].setScale(15, 1, 5)
        self.sb3.stateNodePath[2].setPos(8.5, 0, 2)
        
        self.sb4 = DirectButton(image = ("./models/gui/structures/pd1_locked.png", "./models/gui/structures/pd1_locked.png",
                                   "./models/gui/structures/pd1_hover.png"),frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-25.1,0, 0.85), command=self.selectPD1, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.sb4.stateNodePath[2].setTransparency(1)
        self.sb4.stateNodePath[2].setScale(15, 1, 5)
        self.sb4.stateNodePath[2].setPos(8.5, 0, 2)
        
        self.sb5 = DirectButton(image = ("./models/gui/structures/phylon_locked.png","./models/gui/structures/phylon_locked.png",
                                    "./models/gui/structures/phylon_hover.png"), frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-29.6,0, -0.75), command=self.selectPhylon, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.sb5.stateNodePath[2].setTransparency(1)
        self.sb5.stateNodePath[2].setScale(15, 1, 5)
        self.sb5.stateNodePath[2].setPos(8, 0, 4)
        
        self.sb6 = DirectButton(image = ("./models/gui/structures/pd2_locked.png", "./models/gui/structures/pd2_locked.png",
                                   "./models/gui/structures/pd2_hover.png"),frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-28.1,0, -0.75), command=self.selectPD2, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.sb6.stateNodePath[2].setTransparency(1)
        self.sb6.stateNodePath[2].setScale(15, 1, 5)
        self.sb6.stateNodePath[2].setPos(9, 0, 4)             
        
        self.sb7 = DirectButton(image = ("./models/gui/structures/gc_locked.png", "./models/gui/structures/gc_locked.png",
                                   "./models/gui/structures/gc_hover.png"), frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-29.6,0, -2.3), command=self.selectGC, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.sb7.stateNodePath[2].setTransparency(1)
        self.sb7.stateNodePath[2].setScale(15, 1, 5)
        self.sb7.stateNodePath[2].setPos(9, 0, 6)
        
        self.sb8 = DirectButton(image = ("./models/gui/structures/pd3_locked.png", "./models/gui/structures/pd3_locked.png",
                                   "./models/gui/structures/pd3_hover.png"),frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-28.1,0, -2.3), command=self.selectPD3, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.sb8.stateNodePath[2].setTransparency(1)
        self.sb8.stateNodePath[2].setScale(15, 1, 5)
        self.sb8.stateNodePath[2].setPos(9, 0, 6)
        
        self.sb9 = DirectButton(image = ("./models/gui/structures/pd4_locked.png", "./models/gui/structures/pd4_locked.png",
                                   "./models/gui/structures/pd4_hover.png"), frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-29.6,0, -3.90), command=self.selectPD4, clickSound=self.mouse_click, rolloverSound=self.mouse_hover) 
        self.sb9.stateNodePath[2].setTransparency(1)
        self.sb9.stateNodePath[2].setScale(15, 1, 5)
        self.sb9.stateNodePath[2].setPos(9, 0, 7.5)
           
        self.sb4.reparentTo(self.mainFrame)
        self.sb3.reparentTo(self.mainFrame)
        self.sb2.reparentTo(self.mainFrame)
        self.sb1.reparentTo(self.mainFrame)
        self.sb6.reparentTo(self.mainFrame)
        self.sb5.reparentTo(self.mainFrame)
        self.sb8.reparentTo(self.mainFrame)
        self.sb7.reparentTo(self.mainFrame)
        self.sb9.reparentTo(self.mainFrame)
        
    def loadUnits(self):
        self.ub1 = DirectButton(image = ("./models/gui/units/swarm_locked.png", "./models/gui/units/swarm_locked.png","./models/gui/units/swarm_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-21,0,0.85), command=self.selectSwarm, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.ub1.stateNodePath[2].setTransparency(1)
        self.ub1.stateNodePath[2].setScale(15, 1, 5)
        self.ub1.stateNodePath[2].setPos(9, 0, 3.75)
        
        self.ub2 = DirectButton(image = ("./models/gui/units/globe_locked.png", "./models/gui/units/globe_locked.png", "./models/gui/units/globe_hover.png"), 
                          frameColor=(0, 0,0, 0),image_scale = (0.65, 1, 0.65), pos=(-19.5,0,0.85), command=self.selectGlobe, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.ub2.stateNodePath[2].setTransparency(1)
        self.ub2.stateNodePath[2].setScale(15, 1, 5)
        self.ub2.stateNodePath[2].setPos(9, 0, 3.75)
        
        self.ub3 = DirectButton(image = ("./models/gui/units/analyzer_locked.png", "./models/gui/units/analyzer_locked.png", "./models/gui/units/analyzer_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-18,0, 0.85), command=self.selectAnalyzer, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.ub3.stateNodePath[2].setTransparency(1)
        self.ub3.stateNodePath[2].setScale(15, 1, 5)
        self.ub3.stateNodePath[2].setPos(9, 0, 3.75)
        
        self.ub4 = DirectButton(image = ("./models/gui/units/horde_locked.png", "./models/gui/units/horde_locked.png", "./models/gui/units/horde_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-21,0, -0.75), command=self.selectHorde, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.ub4.stateNodePath[2].setTransparency(1)
        self.ub4.stateNodePath[2].setScale(15, 1, 5)
        self.ub4.stateNodePath[2].setPos(9, 0, 6)
        
        self.ub5 = DirectButton(image = ("./models/gui/units/sphere_locked.png", "./models/gui/units/sphere_locked.png", "./models/gui/units/sphere_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-19.5,0, -0.75), command=self.selectSphere, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.ub5.stateNodePath[2].setTransparency(1)
        self.ub5.stateNodePath[2].setScale(15, 1, 5)
        self.ub5.stateNodePath[2].setPos(9, 0, 5.5)
        
        self.ubGravity = DirectButton(image = ("./models/gui/gravsymbol_locked.png", "./models/gui/gravsymbol_locked.png", "./models/gui/gravsymbol_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-18,0, -0.75), relief=2, command=self.selectGravityEngine, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.ubGravity.setTransparency(1)
        self.ubGravity.stateNodePath[2].setTransparency(1)
        self.ubGravity.stateNodePath[2].setScale(15, 1, 5)
        self.ubGravity.stateNodePath[2].setPos(9, 0, 3.75)
        
        self.ub6 = DirectButton(image = ("./models/gui/units/hive_locked.png", "./models/gui/units/hive_locked.png","./models/gui/units/hive_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-21,0, -2.3),command=self.selectHive, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.ub6.stateNodePath[2].setTransparency(1)
        self.ub6.stateNodePath[2].setScale(15, 1, 5)
        self.ub6.stateNodePath[2].setPos(9, 0, 7.7)
        
        self.ub7 = DirectButton(image = ("./models/gui/units/planetarium_locked.png", "./models/gui/units/planetarium_locked.png","./models/gui/units/planetarium_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-19.5,0, -2.3), command=self.selectPlanetarium, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.ub7.stateNodePath[2].setTransparency(1)
        self.ub7.stateNodePath[2].setScale(15, 1, 5)
        self.ub7.stateNodePath[2].setPos(9, 0, 7.7)        
        
        self.ub8 = DirectButton(image = ("./models/gui/units/mathematica_locked.png","./models/gui/units/mathematica_locked.png","./models/gui/units/mathematica_hover.png"), 
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-18,0, -2.3), command=self.selectMathematica, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.ub8.stateNodePath[2].setTransparency(1)
        self.ub8.stateNodePath[2].setScale(15, 1, 5)
        self.ub8.stateNodePath[2].setPos(9, 0, 7.7) 
        
        self.ub9 = DirectButton(image = ("./models/gui/units/bhg_locked.png","./models/gui/units/bhg_locked.png","./models/gui/units/bhg_hover.png"), 
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-21,0, -3.9), command=self.selectBHG, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)         
        self.ub9.stateNodePath[2].setTransparency(1)
        self.ub9.stateNodePath[2].setScale(15, 1, 5)
        self.ub9.stateNodePath[2].setPos(9, 0, 7.7) 
        #Rendering order matters
        self.ub3.reparentTo(self.mainFrame)
        self.ub2.reparentTo(self.mainFrame)
        self.ub1.reparentTo(self.mainFrame)
        self.ubGravity.reparentTo(self.mainFrame)
        self.ub5.reparentTo(self.mainFrame)
        self.ub4.reparentTo(self.mainFrame)
        self.ub8.reparentTo(self.mainFrame)
        self.ub7.reparentTo(self.mainFrame)
        self.ub6.reparentTo(self.mainFrame)
        self.ub9.reparentTo(self.mainFrame)
    
    def isActivated(self):
        self.sb1.destroy()
        self.sb1 = DirectButton(image = ("./models/gui/structures/forge.png", "./models/gui/structures/forge.png", 
                                   "./models/gui/structures/forge_hover.png"), frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-29.6,0,0.85), command=self.selectForge, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.sb1.stateNodePath[2].setTransparency(1)
        self.sb1.stateNodePath[2].setScale(15, 1, 5)
        self.sb1.stateNodePath[2].setPos(9, 0, 3.5)
        
        self.sb2.destroy()        
        self.sb2 = DirectButton(image = ("./models/gui/structures/nexus.png", "./models/gui/structures/nexus.png",
                          "./models/gui/structures/nexus_hover.png"), frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-28.1,0,0.85), command=self.selectNexus, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.sb2.stateNodePath[2].setTransparency(1)
        self.sb2.stateNodePath[2].setScale(15, 1, 5)
        self.sb2.stateNodePath[2].setPos(8, 0, 3.5)
        
        self.sb3.destroy()
        self.sb3 = DirectButton(image = ("./models/gui/structures/extractor.png","./models/gui/structures/extractor.png",
                                   "./models/gui/structures/extractor_hover.png"),frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-26.6,0, 0.85), command=self.selectExtractor, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.sb3.stateNodePath[2].setTransparency(1)
        self.sb3.stateNodePath[2].setScale(15, 1, 5)
        self.sb3.stateNodePath[2].setPos(8.5, 0, 2)
        
        self.sb4.destroy()
        self.sb4 = DirectButton(image = ("./models/gui/structures/pd1.png", "./models/gui/structures/pd1.png",
                                   "./models/gui/structures/pd1_hover.png"),frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-25.1,0, 0.85), command=self.selectPD1, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.sb4.stateNodePath[2].setTransparency(1)
        self.sb4.stateNodePath[2].setScale(15, 1, 5)
        self.sb4.stateNodePath[2].setPos(8.5, 0, 2)
        
        self.sb4.reparentTo(self.mainFrame)
        self.sb3.reparentTo(self.mainFrame)
        self.sb2.reparentTo(self.mainFrame)
        self.sb1.reparentTo(self.mainFrame)

    #Unlock tier 1 units    
    def hasForge(self):
        self.ub1.destroy()
        self.fub1 = DirectButton(image = ("./models/gui/units/swarm.png", "./models/gui/units/swarm.png","./models/gui/units/swarm_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-21,0,0.85), command=self.selectSwarm, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.fub1.stateNodePath[2].setTransparency(1)
        self.fub1.stateNodePath[2].setScale(15, 1, 5)
        self.fub1.stateNodePath[2].setPos(9, 0, 3.75)
        
        self.ub2.destroy()
        self.fub2 = DirectButton(image = ("./models/gui/units/globe.png", "./models/gui/units/globe.png", "./models/gui/units/globe_hover.png"), 
                          frameColor=(0, 0,0, 0),image_scale = (0.65, 1, 0.65), pos=(-19.5,0,0.85), command=self.selectGlobe, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.fub2.stateNodePath[2].setTransparency(1)
        self.fub2.stateNodePath[2].setScale(15, 1, 5)
        self.fub2.stateNodePath[2].setPos(9, 0, 3.75)
        
        self.ub3.destroy()
        self.fub3 = DirectButton(image = ("./models/gui/units/analyzer.png", "./models/gui/units/analyzer.png", "./models/gui/units/analyzer_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-18,0, 0.85), command=self.selectAnalyzer, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.fub3.stateNodePath[2].setTransparency(1)
        self.fub3.stateNodePath[2].setScale(15, 1, 5)
        self.fub3.stateNodePath[2].setPos(9, 0, 3.75)
        self.fub3.reparentTo(self.mainFrame)
        self.fub2.reparentTo(self.mainFrame)
        self.fub1.reparentTo(self.mainFrame)
    
    #Unlock Tier 2 Units
    def unlockTier2Units(self):
        self.ub4.destroy()
        self.fub4 = DirectButton(image = ("./models/gui/units/horde.png", "./models/gui/units/horde.png", "./models/gui/units/horde_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-21,0, -0.75), command=self.selectHorde, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.fub4.stateNodePath[2].setTransparency(1)
        self.fub4.stateNodePath[2].setScale(15, 1, 5)
        self.fub4.stateNodePath[2].setPos(9, 0, 6)
        
        self.ub5.destroy()
        self.fub5 = DirectButton(image = ("./models/gui/units/sphere.png", "./models/gui/units/sphere.png", "./models/gui/units/sphere_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-19.5,0, -0.75), command=self.selectSphere, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.fub5.stateNodePath[2].setTransparency(1)
        self.fub5.stateNodePath[2].setScale(15, 1, 5)
        self.fub5.stateNodePath[2].setPos(9, 0, 5.5)
        
        self.ubGravity.destroy()
        self.fubGravity = DirectButton(image = ("./models/gui/gravsymbol.png", "./models/gui/gravsymbol.png", "./models/gui/gravsymbol_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-18,0, -0.75), relief=2, command=self.selectGravityEngine, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.fubGravity.setTransparency(1)
        self.fubGravity.stateNodePath[2].setTransparency(1)
        self.fubGravity.stateNodePath[2].setScale(15, 1, 5)
        self.fubGravity.stateNodePath[2].setPos(9, 0, 3.75)
        
        self.fubGravity.reparentTo(self.mainFrame)
        self.fub5.reparentTo(self.mainFrame)
        self.fub4.reparentTo(self.mainFrame)
        
    def unlockTier2Structures(self):
        
        self.sb5.destroy()
        self.phylon = DirectButton(image = ("./models/gui/structures/phylon.png","./models/gui/structures/phylon.png",
                                    "./models/gui/structures/phylon_hover.png"), frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-29.6,0, -0.75), command=self.selectPhylon, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.phylon.stateNodePath[2].setTransparency(1)
        self.phylon.stateNodePath[2].setScale(15, 1, 5)
        self.phylon.stateNodePath[2].setPos(8, 0, 4)
        
        self.sb6.destroy()
        self.pd2 = DirectButton(image = ("./models/gui/structures/pd2.png", "./models/gui/structures/pd2.png",
                                   "./models/gui/structures/pd2_hover.png"),frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-28.1,0, -0.75), command=self.selectPD2, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.pd2.stateNodePath[2].setTransparency(1)
        self.pd2.stateNodePath[2].setScale(15, 1, 5)
        self.pd2.stateNodePath[2].setPos(9, 0, 4)
        self.pd2.reparentTo(self.mainFrame)
        self.phylon.reparentTo(self.mainFrame)
        
    #Unlock Tier 3 
    def unlockTier3Units(self):
        self.fub6 = DirectButton(image = ("./models/gui/units/hive.png", "./models/gui/units/hive.png","./models/gui/units/hive_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-21,0, -2.3),command=self.selectHive, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.fub6.stateNodePath[2].setTransparency(1)
        self.fub6.stateNodePath[2].setScale(15, 1, 5)
        self.fub6.stateNodePath[2].setPos(9, 0, 7.7)
        
        self.fub7 = DirectButton(image = ("./models/gui/units/planetarium.png", "./models/gui/units/planetarium.png","./models/gui/units/planetarium_hover.png"),
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-19.5,0, -2.3), command=self.selectPlanetarium, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.fub7.stateNodePath[2].setTransparency(1)
        self.fub7.stateNodePath[2].setScale(15, 1, 5)
        self.fub7.stateNodePath[2].setPos(9, 0, 7.7)        
        
        self.fub8 = DirectButton(image = ("./models/gui/units/mathematica.png","./models/gui/units/mathematica.png","./models/gui/units/mathematica_hover.png"), 
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-18,0, -2.3), command=self.selectMathematica, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.fub8.stateNodePath[2].setTransparency(1)
        self.fub8.stateNodePath[2].setScale(15, 1, 5)
        self.fub8.stateNodePath[2].setPos(9, 0, 7.7)
        
        self.fub8.reparentTo(self.mainFrame)
        self.fub7.reparentTo(self.mainFrame)
        self.fub6.reparentTo(self.mainFrame)
        
    def unlockTier3Structures(self):
        self.sb7.destroy()
        self.gc = DirectButton(image = ("./models/gui/structures/gc.png", "./models/gui/structures/gc.png",
                                   "./models/gui/structures/gc_hover.png"), frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-29.6,0, -2.3), command=self.selectGC, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.gc.stateNodePath[2].setTransparency(1)
        self.gc.stateNodePath[2].setScale(15, 1, 5)
        self.gc.stateNodePath[2].setPos(9, 0, 6)
        
        self.sb8.destroy()
        self.pd3 = DirectButton(image = ("./models/gui/structures/pd3.png", "./models/gui/structures/pd3.png",
                                   "./models/gui/structures/pd3_hover.png"),frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-28.1,0, -2.3), command=self.selectPD3, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)
        self.pd3.stateNodePath[2].setTransparency(1)
        self.pd3.stateNodePath[2].setScale(15, 1, 5)
        self.pd3.stateNodePath[2].setPos(9, 0, 6)
        self.pd3.reparentTo(self.mainFrame)
        self.gc.reparentTo(self.mainFrame)
        
    #Unlock Tier 4 Units
    def unlockTier4Units(self):
        self.fub9 = DirectButton(image = ("./models/gui/units/bhg.png","./models/gui/units/bhg.png","./models/gui/units/bhg_hover.png"), 
                          frameColor=(0, 0,0, 0), image_scale = (0.65, 1, 0.65), pos=(-21,0, -3.9), command=self.selectBHG, clickSound=self.mouse_click, rolloverSound=self.mouse_hover)         
        self.fub9.stateNodePath[2].setTransparency(1)
        self.fub9.stateNodePath[2].setScale(15, 1, 5)
        self.fub9.stateNodePath[2].setPos(9, 0, 7.7)
        self.fub9.reparentTo(self.mainFrame)
        
    def unlockTier4Structures(self):
        self.sb9.destroy()
        self.pd4 = DirectButton(image = ("./models/gui/structures/pd4.png", "./models/gui/structures/pd4.png",
                                   "./models/gui/structures/pd4_hover.png"), frameColor=(0, 0,0, 0),
                          image_scale = (0.65, 1, 0.65), pos=(-29.6,0, -3.90), command=self.selectPD4, clickSound=self.mouse_click, rolloverSound=self.mouse_hover) 
        self.pd4.stateNodePath[2].setTransparency(1)
        self.pd4.stateNodePath[2].setScale(15, 1, 5)
        self.pd4.stateNodePath[2].setPos(9, 0, 8.25)
        self.pd4.reparentTo(self.mainFrame)

    def loadResearchTree(self):
        b1 = DirectButton(image = ("./models/gui/ResearchButton.png"), pos = (7, 0, -3),
                          frameColor=(0, 0,0, 0),image_scale = (4, 1, 1.5), command = self.researchTree.loadTree, clickSound=self.mouse_click)
        b1.stateNodePath[0].setTransparency(1)
        b1.stateNodePath[1].setTransparency(1)
        b1.stateNodePath[2].setTransparency(1)
        b1.reparentTo(self.mainFrame)
       
    ## CONSTRUCTION SELECTION
    def selectForge(self):
        if(self.player != None):
            self.player.addStructure("forge")
        
    def selectNexus(self):
        if(self.player != None):
            self.player.addStructure("nexus")
        
    def selectExtractor(self):
        if(self.player != None):
            self.player.addStructure("extractor")
        
    def selectPhylon(self):
        if(self.player != None):
            self.player.addStructure("phylon")
        
    def selectGC(self):
        if(self.player != None):
            self.player.addStructure("generatorCore")
        
    def selectPD1(self):
        if self.player != None:
            self.player.addStructure("pd1")
    
    def selectPD2(self):
        if(self.player != None):
            self.player.addStructure("pd2")
        
    def selectPD3(self):
        if(self.player != None):
            self.player.addStructure("pd3")
        
    def selectPD4(self):
        if(self.player != None):
            self.player.addStructure("pd4")
        
    ## UNIT SELECTION        
    def selectSwarm(self):
        if(self.player != None):
            self.player.addUnit("swarm")
        
    def selectGlobe(self):
        if(self.player != None):
            self.player.addUnit("globe")
        
    def selectAnalyzer(self):
        if(self.player != None):
            self.player.addUnit("analyzer")
        
    def selectHorde(self):
        if(self.player != None):
            self.player.addUnit("horde")
        
    def selectSphere(self):
        if(self.player != None):
            self.player.addUnit("sphere")
        
    def selectHive(self):
        if(self.player != None):
            self.player.addUnit("hive")
        
    def selectPlanetarium(self):
        if(self.player != None):
            self.player.addUnit("planetarium")
        
    def selectMathematica(self):
        if(self.player != None):
            self.player.addUnit("mathematica")

    def selectBHG(self):
        if(self.player != None):
            self.player.addUnit("blackHoleGenerator")
    
    def selectGravityEngine(self):
        if(self.player != None):
            self.player.addUnit("gravityEngine")
