'''
Created on Feb 16, 2012

@author: Eran-Tasker
'''
from pandac.PandaModules import * 
import direct.directbase.DirectStart 
from direct.distributed.PyDatagram import PyDatagram 
from direct.distributed.PyDatagramIterator import PyDatagramIterator 
from pandac.PandaModules import QueuedConnectionManager
from pandac.PandaModules import QueuedConnectionListener
from pandac.PandaModules import QueuedConnectionReader
from pandac.PandaModules import ConnectionWriter

cManager = QueuedConnectionManager()
cListener = QueuedConnectionListener(cManager, 0)
cReader = QueuedConnectionReader(cManager, 0)
cWriter = ConnectionWriter(cManager,0)

activeConnections=[]

port_adress = 9099
backlog = 1000 #Ignore 1000 connection attempts
tcpSocket = cManager.openTCPServerRendezvous(port_adress, backlog)

cListener.addConnection(tcpSocket)

def tskListenerPolling(taskdata):
    if cListener.newConnectionAvailable():
        rendezvous = PointerToConnection()
        netAddress = NetAddress()
        newConnection = PointerToConnection()
 
    if cListener.getNewConnection(rendezvous,netAddress,newConnection):
        newConnection = newConnection.p()
        activeConnections.append(newConnection) # Remember connection
        cReader.addConnection(newConnection)     # Begin reading connection
    return Task.cont

def tskReaderPolling(taskdata):
    if cReader.dataAvailable():
        datagram=NetDatagram()  # catch the incoming data in this instance
    # Check the return value; if we were threaded, someone else could have
    # snagged this data before we did
    if cReader.getData(datagram):
        myProcessDataFunction(datagram)
    return Task.cont

# Developer-defined constants, telling the server what to do.
# Your style of how to store this information may differ; this is
# only one way to tackle the problem
PRINT_MESSAGE = 1
 
def myNewPyDatagram(self):
    # Send a test message
    myPyDatagram = PyDatagram()
    myPyDatagram.addUint8(PRINT_MESSAGE)
    myPyDatagram.addString("Welcome to Benjamin's server!!")
    return myPyDatagram

# broadcast a message to all clients
myPyDatagram = myNewPyDatagram()  # build a datagram to send
for aClient in activeConnections:
    cWriter.send(myPyDatagram,aClient)
  
# terminate connection to all clients
 
for aClient in activeConnections:
    cReader.removeConnection(aClient)
activeConnections=[]
 
# close down our listener
cManager.closeConnection(tcpSocket)


taskMgr.add(tskListenerPolling,"Poll the connection listener",-39)
taskMgr.add(tskReaderPolling,"Poll the connection reader",-40)

def myProcessDataFunction(netDatagram):
    myIterator = PyDatagramIterator(netDatagram)
    msgID = myIterator.getUint8()
    if msgID == PRINT_MESSAGE:
        messageToPrint = myIterator.getString()
        print messageToPrint

datagram = NetDatagram()
if cReader.getData(datagram):
    myProcessDataFunction(datagram)
  
sourceOfMessage = datagram.getConnection()

