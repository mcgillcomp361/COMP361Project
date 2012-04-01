'''
Created on Mar 31, 2012

@author: Benjamin
'''
import unittest
from gameModel.structures import Structure
from gameModel.structures import Extractor
from gameModel.structures import Forge
from gameModel.structures import GeneratorCore
from gameModel.structures import Nexus
from gameModel.structures import Phylon
from gameModel.structures import PlanetaryDefenseI
from gameModel.solar import Planet, Star
from gameModel.player import Player


class Test(unittest.TestCase):


    def setUp(self):
        self.struct = Structure(100, Planet(13, 45, 26, Star(21, 6, Player("Bazibaz")), None, Player("Bazibaz")))
        self.forge = Forge(Planet(13, 45, 26, Star(21, 6, Player("Bazibaz")), None, Player("Bazibaz")))
        self.extractor = Extractor(Planet(13, 45, 26, Star(21, 6, Player("Bazibaz")), None, Player("Bazibaz")))
        self.gencore = GeneratorCore(Planet(13, 45, 26, Star(21, 6, Player("Bazibaz")), None, Player("Bazibaz")))
        self.nexus = Nexus(Planet(13, 45, 26, Star(21, 6, Player("Bazibaz")), None, Player("Bazibaz")))
        self.phylon = Phylon(Planet(13, 45, 26, Star(21, 6, Player("Bazibaz")), None, Player("Bazibaz")))
        self.defense = PlanetaryDefenseI(Planet(13, 45, 26, Star(21, 6, Player("Bazibaz")), None, Player("Bazibaz")))
        
    def test_consqueue(self):
        self.assertEqual(self.forge._units_in_construction, None)
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()