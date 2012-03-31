'''
Created on Dec 30, 2011

@author: Eran-Tasker
'''
from gameModel.abilities import Ability
import unittest
import random

class Test(unittest.TestCase):
    
    #Abilities test cases
    def setUp(self):
        self.ability1 = Ability(100)
        self.ability2 = Ability(random.random())
        self.ability3 = Ability(100)
    
    def test_param(self):
        self.assertEqual(self.ability1.cool_down, self.ability3.cool_down)
        self.assertNotEqual(self.ability2.cool_down, self.ability1.cool_down)
        self.assertNotEqual(self.ability2.cool_down, self.ability3.cool_down)
        
    def test_use(self):
        self.assertFalse(self.ability1.used)
        self.ability1.use(123)
        self.assertTrue(self.ability1.used)
        self.assertNotEqual(self.ability1.position, None)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()