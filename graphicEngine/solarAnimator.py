'''
Created on 13 mars 2012

@author: num3ric
'''
from direct.showbase import DirectObject 

class SolarAnimator(DirectObject.DirectObject):
    
    def __init__(self, dstars, dplanets):
        self._dstars = dstars
        self._dplanets = dplanets
        taskMgr.add(self.stepAnimation, 'SolarAnimation')
    
    def stepAnimation(self, task):
#        self.orbitPlanets()
        self.drawConnections()
        return task.cont
        
    def orbitPlanets(self):
        for dplanet in self._dplanets:
            dplanet.orbit()
            
    def drawConnections(self):
        nb = 10
        point_list = []
        for i in xrange(nb):
            first_dplanet = self._dplanets[i]
            second_dplanet = None
            for j in xrange(i, nb):
                second_dplanet = self._dplanets[j]
                point_list.append((first_dplanet.point_path.getPos(), second_dplanet.point_path.getPos()))
            first_dplanet.drawConnections(second_dplanet, point_list)
            del point_list[:]
                
        