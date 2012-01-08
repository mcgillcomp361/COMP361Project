'''
Created on 7 janv. 2012

@author: num3ric
'''

class StarRender(object):
    pass
#
#
#    def __init__(self):
#        '''
#        Constructor
#        '''
#        pass
##        self.sun = loader.loadModel("../models/planet_sphere")
##        self.sun_tex = loader.loadTexture("../models/sun_1k_tex.jpg")
##        self.sun.setTexture(self.sun_tex, 1)
##        self.sun.reparentTo(render)
##        self.sun.setScale(2 * self._radius)


class PlanetRender(object):
    pass
#    
#    def __init__(self):
#        self._orbital_velocity = 0
#        self.orbit_radius = 0
#        
#    
#    def loadPlanet(self):
#        self.orbit_root_mercury = render.attachNewNode('orbit_root_mercury')
#
#    
#        self.mercury = loader.loadModel("../models/planet_sphere")
#        self.mercury_tex = loader.loadTexture("../models/mercury_1k_tex.jpg")
#        self.mercury.setTexture(self.mercury_tex, 1)
#        self.mercury.reparentTo(self.orbit_root_mercury)
#        self.mercury.setPos( 0.38 * self.orbitscale, 0, 0)
#        self.mercury.setScale(0.385 * self._radius)
#    
#    def rotatePlanet(self):
#        self.orbit_period_mercury = self.orbit_root_mercury.hprInterval(
#          (0.241 * self._orbital_velocity), Vec3(360, 0, 0))
#        self.day_period_mercury = self.mercury.hprInterval(
#          (59 * self._orbitingUnits), Vec3(360, 0, 0))
#    
#        self.orbit_period_mercury.loop()
#        self.day_period_mercury.loop()