'''
Created on Mar 31, 2012

@author: Benjamin
'''
import unittest
from gameModel.player import Player
from gameModel.solar import Planet
from gameModel.solar import Star


class Test(unittest.TestCase):


    def setUp(self):
        self.player = Player("Ben")
        self.player.selected_planet = 
        
    def test_param(self):
        self.assertEquals(self.player.name, "Ben")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()