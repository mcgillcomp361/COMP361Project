'''
Created on 13 janv. 2012

@author: num3ric
'''
import random, math

#ANTIALIASING PREREQUISITE. Has to be loaded before anything else.
from pandac.PandaModules import loadPrcFileData 
loadPrcFileData('', 'framebuffer-multisample 1' ) 
loadPrcFileData('', 'multisamples 8')

from pandac.PandaModules import AntialiasAttrib
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *

from solar import *
from GameModel.solar import *

    
class Application(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.disableMouse() 

        sun = Star(100, Point3(0,0,0), 1)
        dsun = StarDraw(sun)
        
        system_planets = []
        for i in xrange(10):
            r = random.random()
            planet = Planet(Point3((random.random()-0.5) * 20, \
                                   (random.random()-0.5) * 20, 0), \
                            r*0.2+0.20, r*50+20)
            dplanet = PlanetDraw(planet, dsun.point_path)
            dplanet.startSpin()
            dplanet.startOrbit()
            system_planets.append((planet, dplanet))
        
        base.useDrive()
        base.useTrackball()
        self.camera.setPos(0, -12, 5)
        self.camera.lookAt(0, 0, 0)
#        render.setColor(0.2, 0.8, 1.0)
        render.setAntialias(AntialiasAttrib.MMultisample, 1) 
        dirLight = DirectionalLight("directional")
        dirLight.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
        dirNode = render.attachNewNode(dirLight)
        dirNode.setHpr(60, 0, 90)
        render.setLight(dirNode)
        render.setShaderAuto()

app = Application()
app.run()