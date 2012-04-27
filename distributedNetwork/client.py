'''
Created on 2012-04-23

@author: Eran-Tasker
'''
from direct.directbase.DirectStart import *
from direct.distributed.ClientRepository import ClientRepository
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import *

from distributedStar import DistributedStar

import sys
import random

class MyClientRepository(ClientRepository):
    def __init__(self):
        dcFileNames = ['direct.dc', 'net.dc']
        
        ClientRepository.__init__(self, dcFileNames = dcFileNames)
        
class Client(DirectObject):
    def __init__(self):
        DirectObject.__init__(self)
        
        #No player yet
        self.player = None
        self.stars = []
        
        tcpPort = base.config.GetInt('server-port', 4400)
        hostname = base.config.GetString('server-host', '192.168.137.1')
        self.url = URLSpec('http://%s:%s' % (hostname, tcpPort))
        
        self.cr = MyClientRepository()
        self.cr.connect([self.url], successCallback = self.connectSuccess, failureCallback = self.connectFailure)
        self.waitingText = OnscreenText(
            'Connecting to %s.\n.' % (self.url),
            scale = 0.1, fg = (1, 1, 1, 1), shadow = (0, 0, 0, 1))
    
    def connectFailure(self, statusCode, statusString):
        self.waitingText.destroy()
        self.failureText = OnscreenText(
            'Failed to connect to %s: %s.' % (self.url, statusString),
            scale = 0.15, fg = (1, 0, 0, 1), shadow = (0, 0, 0, 1))
        
    def connectSuccess(self):
        """ Successfully connected.  But we still can't really do
        anything until we've got the doID range. """
        self.waitingText.destroy()
        self.waitingText = OnscreenText('Waiting for server.',scale = 0.1, fg = (1, 1, 1, 1), shadow = (0, 0, 0, 1))
        self.acceptOnce('createReady', self.createReady)
        
    def createReady(self):
        """ Now we're ready to go! """
        self.waitingText.destroy()
        
        # Manifest an avatar for ourselves.
        #self.av = self.cr.createDistributedObject(className = 'DistributedPlayer')

        # Update the local avatar's position every frame.
        #self.moveTask = taskMgr.add(self.moveAvatar, 'moveAvatar')

        # Send position updates only several times a second, instead
        # of every frame, or we will flood the network.
        #self.lastBroadcastTransform = self.av.getTransform()
        #self.updateTask = taskMgr.doMethodLater(0.2, self.updateAvatar, 'updateAvatar')
        
    def addStars(self, positions):
        for position in positions:
            star = DistributedStar(self.cr)
            star.setInitialPos(position)
            self.cr.createDistributedObject(distObj = star)
            self.stars.append(star)
            
    def clearStars(self):
        for p in self.stars:
            self.cr.sendDeleteMsg(p.doId)