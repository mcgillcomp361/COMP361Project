'''
Created on 25 janv. 2012

@author: Bazibaz
'''
from direct.showbase import DirectObject 
from pandac.PandaModules import AntialiasAttrib, DirectionalLight, AmbientLight, Fog
from panda3d.core import VBase4, Vec4
from gameModel.constants import UNIVERSE_SCALE

class Environement(DirectObject.DirectObject):
    '''
    Host the different graphical environement elements
    '''
    def __init__(self):
        
        base.setBackgroundColor(0, 0, 0)
        render.setAntialias(AntialiasAttrib.MMultisample, 1)

        #Lighting
#        dirLight = DirectionalLight("directional")
#        dirLight.setColor(Vec4(1.0, 1.0, 1.0, 1.0))
#        dirNode = render.attachNewNode(dirLight)
#        dirNode.setHpr(60, 0, 90)
#        render.setLight(dirNode)
        
        alight = AmbientLight('alight')
        alight.setColor(VBase4(0.5, 0.5, 0.75, 1))
        alnp = render.attachNewNode(alight)
        render.setLight(alnp)
        render.setShaderAuto()
    
        self.sky = loader.loadModel("models/environment/solar_sky_sphere")
        self.sky_tex = loader.loadTexture("models/environment/universe.png")
        self.sky.setTexture(self.sky_tex, 1)
        self.sky.reparentTo(render)
        self.sky.setScale(UNIVERSE_SCALE*5)
