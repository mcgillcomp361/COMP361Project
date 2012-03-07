'''
Created on Mar 2, 2012

@author: Eran-Tasker
'''
from pandac.PandaModules import * 
import direct.directbase.DirectStart 
from direct.distributed.PyDatagram import PyDatagram 
from direct.distributed.PyDatagramIterator import PyDatagramIterator 
from pandac.PandaModules import QueuedConnectionManager
from pandac.PandaModules import QueuedConnectionReader
from pandac.PandaModules import ConnectionWriter

cManager = QueuedConnectionManager()
cReader = QueuedConnectionReader(cManager, 0)
cWriter = ConnectionWriter(cManager,0)


port_address=9099  # same for client and server
 
 # a valid server URL. You can also use a DNS name
 # if the server has one, such as "localhost" or "panda3d.org"
ip_address="192.168.0.50"
 
 # how long until we give up trying to reach the server?
timeout_in_miliseconds=3000  # 3 seconds
 
myConnection=cManager.openTCPClientConnection(ip_address,port_address,timeout_in_miliseconds)
if myConnection:
  cReader.addConnection(myConnection)  # receive messages from server
  
# Developer-defined constants, telling the server what to do.
# Your style of how to store this information may differ; this is
# only one way to tackle the problem
PRINT_MESSAGE = 1
 
def myNewPyDatagram(self):
  # Send a test message
  myPyDatagram = PyDatagram()
  myPyDatagram.addUint8(PRINT_MESSAGE)
  myPyDatagram.addString("Hello, world!")
  return myPyDatagram

cWriter.send(myNewPyDatagram(), aConnection)


cManager.closeConnection(myConnection)

