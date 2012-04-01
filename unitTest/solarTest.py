'''
Created on Mar 31, 2012

@author: Benjamin
'''
import unittest
from gameModel.player import Player
from gameModel.solar import SphericalBody
from gameModel.solar import Star
from gameModel.solar import Planet
from gameModel.constants import *
from direct.showbase import DirectObject

window = DirectObject() 

class Test(unittest.TestCase):


    def setUp(self):
        #self.sphere1 = SphericalBody(123,80,False, Player("Bazibaz"))
        #self.sphere2 = SphericalBody(123,80,True, Player("Bazibaz"))
        
        self.star = Star(123,34)
        
        self.planet1 = Planet(60,45,12,self.star)
        self.planet2 = Planet(60,45,12,self.star,self.planet1,Player("Bazibaz"))
        
    def test_addPlnt(self):
        self.star.addPlanet(self.planet1)
        self.assertEqual(self.star._planets[0], self.planet1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()