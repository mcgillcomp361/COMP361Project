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
            pos=(0, 0,-0.8),
            sortOrder=2,
            geom=loader.loadModel("./models/gui/guiBar.egg"),        
            geom_scale = (65,5,8),
            geom_pos = (0,0,0)
        )   
        self.player = player
        self.loadResources()
        self.loadMiniMap()
        self.playerResources()
        self.loadAbilities()
        self.loadUnits()
        self.loadResearchTree()
        
    def loadResources(self):
        b1 = DirectButton(text = ("Forge", "click!", "roll"), frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                  text_scale=0.4, pos=(-30,0,0.5),borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                  relief=2, command=self.selectForge)
        b2 = DirectButton(text = ("Nexus", "click!", "roll"),frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                  text_scale=0.4, pos=(-28.5,0,0.5), borderWidth = (0.005, 0.005),  text_align = TextNode.ALeft,
                  relief=2, command=self.selectNexus)
        b3 = DirectButton(text = ("Extractor", "click!", "roll"),frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                  text_scale=0.3, pos=(-27,0, 0.5), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                  relief=2, command=self.selectExtractor)
        b4 = DirectButton(text = ("PD 1", "click!", "roll"), frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          text_scale=0.4, pos=(-25.5,0, 0.5), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectPD1)
        b5 = DirectButton(text = ("Phylon", "click!", "roll"), frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          text_scale=0.4, pos=(-30,0, -0.5), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectPhylon)
        b6 = DirectButton(text = ("PD II", "click!", "roll"), frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          text_scale=0.4, pos=(-28.5,0, -0.5), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectPD2)
        b7 = DirectButton(text = ("GC", "click!", "roll"), frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          text_scale=0.4, pos=(-30,0, -1.5), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectGC)
        b8 = DirectButton(text = ("PD III", "click!", "roll"), frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          text_scale=0.4, pos=(-28.5,0, -1.5), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                          relief=2, command=self.selectPD3)
        b9 = DirectButton(text = ("PD IV", "click!", "roll"), frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                          text_scale=0.4, pos=(-30,0, -2.5), borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
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
         b1 = DirectButton(text = ("Swarm", "click!", "roll"), frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                  text_scale=0.4, pos=(-22,0,0.5),borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                  relief=2, command=self.selectSwarm)
         b2 = DirectButton(text = ("Globe", "click!", "roll"), frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                  text_scale=0.4, pos=(-20.5,0,0.5),borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                  relief=2, command=self.selectGlobe)
         b3 = DirectButton(text = ("Analyzer", "click!", "roll"), frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                  text_scale=0.4, pos=(-19,0,0.5),borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                  relief=2, command=self.selectAnalyzer)
         b4 = DirectButton(text = ("Horde", "click!", "roll"), frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                  text_scale=0.4, pos=(-22,0,-0.5),borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                  relief=2, command=self.selectHorde)
         b5 = DirectButton(text = ("Sphere", "click!", "roll"), frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                  text_scale=0.4, pos=(-20.5,0,-0.5),borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                  relief=2, command=self.selectSphere)
         b6 = DirectButton(text = ("Hive", "click!", "roll"), frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                  text_scale=0.4, pos=(-22,0,-1.5),borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                  relief=2, command=self.selectHive)
         b7 = DirectButton(text = ("Planetarium", "click!", "roll"), frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                  text_scale=0.4, pos=(-20.5,0,-1.5),borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                  relief=2, command=self.selectPlanetarium)
         b8 = DirectButton(text = ("Mathematica", "click!", "roll"), frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                  text_scale=0.4, pos=(-19,0,-1.5),borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                  relief=2, command=self.selectMathematica)
         b9 = DirectButton(text = ("BHG", "click!", "roll"), frameColor=(0, 0,0, 0),text_fg=(1,1,1,1),
                  text_scale=0.4, pos=(-22,0,-2.5),borderWidth = (0.005, 0.005), text_align = TextNode.ALeft,
                  relief=2, command=self.selectBHG)        
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
        resources = OnscreenText(text = 'Resources: ', pos = (1.3, 0.3), scale = 0.7, fg = (1, 1, 1, 1))
        amt = str(self.player.minerals)
        amount = OnscreenText(text = amt, pos = (5, 0.3), scale = 0.7, fg = (1, 1, 1, 1))
        gEngine = OnscreenText(text = 'Gravity Engines: ', pos = (2, -0.7), scale = 0.7, fg = (1, 1, 1, 1))
        resources.reparentTo(self.mainFrame)
        gEngine.reparentTo(self.mainFrame)
        amount.reparentTo(self.mainFrame)
      
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
       # window = base.openWindow()

    def loadMiniMap(self):
        #TODO: JULIE
        minimap =  DirectFrame(pos=(1,-1,-1), frameSize=(0.3, 0.5, 0.0, 0.35), frameColor = (0, 0, 0, 1) )
        
    ## CONSTRUCTION SELECTION
    def selectForge(self):
        print 'selected Forge'
        
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
        print 'selected swarm'
        
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
