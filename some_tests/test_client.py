#!/usr/bin/env python

import direct.directbase.DirectStart

from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import * 
from direct.task import Task 
from direct.distributed.PyDatagram import PyDatagram 
from direct.distributed.PyDatagramIterator import PyDatagramIterator 
from Client import *

class World(DirectObject):
    def __init__(self):
        # Connect to our server
        self.client = Client("127.0.0.1", 9099, compress=True)
        
        # Create a task to print and send data
        taskMgr.doMethodLater(2.0, self.printTask, "printData")
        
    def printTask(self, task):
        # Print results
        print "Received: " + str(self.client.getData())
        print "Connected: " + str(self.client.getConnected())
        
        # Setup data to send to the server
        data = {}
        data["test"] = "test"
        
        # Send data to the server
        self.client.sendData(data)
        
        return Task.again
            
w = World()
run()