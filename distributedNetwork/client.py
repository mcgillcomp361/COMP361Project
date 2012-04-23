'''
Created on 2012-04-23

@author: Eran-Tasker
'''
from direct.directbase.DirectStart import *
from direct.distributed.ClientRepository import ClientRepository
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import *
import sys
import random

class MyClientRepository(ClientRepository):
    def __init__(self):
        dcFileNames = ['direct.dc', 'net.dc']
        
        ClientRepository.__init__(self, dcFileNames = dcFileNames)
        
class Client(DirectObject):
    def __init__(self):
        DirectObject.__init__(self)