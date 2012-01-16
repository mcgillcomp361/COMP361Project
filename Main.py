'''
Created on 13 janv. 2012

@author: num3ric
'''
import random, math, sys

#ANTIALIASING PREREQUISITE. Has to be loaded before anything else.
from pandac.PandaModules import loadPrcFileData 
loadPrcFileData('', 'framebuffer-multisample 1' ) 
loadPrcFileData('', 'multisamples 8')

from pandac.PandaModules import AntialiasAttrib, DirectionalLight, AmbientLight
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import *

from GameModel.solar import *
from GameEngine.MouseEvents import MouseEvents
from GraphicEngine.solar import StarDraw, PlanetDraw
from GraphicEngine.camera import Camera
    
class Application(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0, 0, 0)
#        self.disableMouse() 
        game_camera = Camera()
        mouse_events = MouseEvents()

        sun = Star(position=Point3(0,0,0), radius=1)
        dsun = StarDraw(sun)
        
        system_planets = []
        for i in xrange(10):
            r = random.random()
            planet = Planet(position=Point3((random.random()-0.5) * 20, \
                                            (random.random()-0.5) * 20, 0), \
                            radius=r*0.2+0.20)
            planet.orbital_velocity = r*50+20
            planet.spin_velocity = 60
            dplanet = PlanetDraw(planet, dsun.point_path)
            dplanet.startSpin()
            dplanet.startOrbit()
            system_planets.append((planet, dplanet))
        
#        base.useDrive()
#        base.useTrackball()
        self.camera.setPos(0, -12, 5)
        self.camera.lookAt(0, 0, 0)

        render.setAntialias(AntialiasAttrib.MMultisample, 1) 
        #Lighting
        dirLight = DirectionalLight("directional")
        dirLight.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        dirNode = render.attachNewNode(dirLight)
        dirNode.setHpr(60, 0, 90)
        render.setLight(dirNode)
        alight = AmbientLight('alight')
        alight.setColor(VBase4(0.2, 0.2, 0.4, 1))
        alnp = render.attachNewNode(alight)
        render.setLight(alnp)
        render.setShaderAuto()
        
        self.loadBackground()
        
        self.title = OnscreenText(text="Bazibaz", style=1, fg=(1,1,1,1), pos=(0.9,0.9), scale = .1)
        self.text = self.genLabelText(
            "Zoom in and out using a mouse", 0)
        self.text = self.genLabelText("Move mouse side to side", 1)
        self.text = self.genLabelText("Rotate view by pressing on the right mouse key", 2)
        
        #Exit the program when escape is pressed
        self.accept("escape", sys.exit)
    
    def genLabelText(self, text, i):
        return OnscreenText(text = text, pos = (-1.3, .95-.05*i), fg=(1,1,1,1), \
                            align = TextNode.ALeft, scale = .05, mayChange = 1)
    
    def loadBackground(self):
        #TODO: Lighting should not affect the sky sphere
        self.sky = loader.loadModel("models/solar_sky_sphere")
        self.sky_tex = loader.loadTexture("models/stars_1k_tex.jpg")
        self.sky.setTexture(self.sky_tex, 1)
        self.sky.reparentTo(render)
        self.sky.setScale(40)

app = Application()
app.run()