#!/usr/bin/env python

import direct.directbase.DirectStart

from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import * 
from direct.task import Task 
from direct.distributed.PyDatagram import PyDatagram 
from direct.distributed.PyDatagramIterator import PyDatagramIterator 
from Server import *

class World(DirectObject):
    def __init__(self):
        # Start our server up
        self.server = Server(9099, compress=True)
        
        # Create a task to print and send data
        taskMgr.doMethodLater(2.0, self.printTask, "printData")
        
    def printTask(self, task):
        # Print out results
        print "Received: " + str(self.server.getData())
        print "Clients: " + str(self.server.getClients())
        
        # Broadcast data to all clients
        self.server.broadcastData("Server's Data")
        
        return Task.again
            
w = World()
run()