'''
Created on 7 janv. 2012

@author: num3ric
'''

from panda3d.core import Vec3

class StarRender(object):


    def __init__(self, Star):
        '''
        Constructor
        '''
        self.star = loader.loadModel("models/planet_sphere")
        if Star.activated:
            self.star_tex = loader.loadTexture("models/star_1k_tex.jpg")
        else:
            self.star_tex = loader.loadTexture("models/star_dead_tex.jpg")
        self.star.setTexture(self.star_tex, 1)
        self.star.reparentTo(render)
        self.star.setPos(Star.position)
        self.star.setScale(2 * Star.radius)
        self.star.setTag('starTag', '1');


class PlanetRender(object):

    def __init__(self, Planet):
        self._orbital_velocity = Planet.orbital_velocity
        self.orbit_radius = Planet.radius
        self.orbit_root_planet = render.attachNewNode('orbit_root_planet')

    
        self.planet = loader.loadModel("models/planet_sphere")
        self.planet_tex = loader.loadTexture("models/mars_1k_tex.jpg")
        self.planet.setTexture(self.planet_tex, 1)
        self.planet.reparentTo(self.orbit_root_planet)
        self.planet.setPos(Planet.position)
        self.planet.setScale(0.385 * Planet.radius)
        self._orbital_velocity = Planet.orbital_velocity
        self._orbitingUnits = Planet._orbiting_units
        
        self.rotatePlanet()
    
    def rotatePlanet(self):
        self.orbit_period_planet = self.orbit_root_planet.hprInterval(
          (0.241 * self._orbital_velocity), Vec3(360, 0, 0))
        self.rotate_period_planet = self.planet.hprInterval(
          (59 * .82), Vec3(360, 0, 0))
    
        self.orbit_period_planet.loop()
        self.rotate_period_planet.loop()