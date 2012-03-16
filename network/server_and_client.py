'''
Created on Mar 15, 2012

@author: Benjamin
'''
from panda3d.core import *
from direct.task import Task
import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
#For transmitting information between the server and client
from direct.distributed.PyDatagram import PyDatagram 
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from pandac.PandaModules import NetDatagram
#Network imports
from pandac.PandaModules import QueuedConnectionManager
from pandac.PandaModules import QueuedConnectionListener
from pandac.PandaModules import QueuedConnectionReader
from pandac.PandaModules import ConnectionWriter

PRINT_MESSAGE = 1 #1=TRUE print the message

class Server(DirectObject):
    def __init__(self):
        self.cManager = QueuedConnectionManager()
        self.cListener = QueuedConnectionListener(self.cManager, 0)
        self.cReader = QueuedConnectionReader(self.cManager, 0)
        self.cWriter = ConnectionWriter(self.cManager,0)
 
        self.activeConnections = [] # Keeps tracks of active connections
        
        #Set up the connection
        port_address=9099 #No-other TCP/IP services are using this port
        backlog=1000 #If we ignore 1,000 connection attempts, something is wrong!
        self.tcpSocket = self.cManager.openTCPServerRendezvous(port_address,backlog)
 
        self.cListener.addConnection(self.tcpSocket)
        self.setTaskManagers() #Set the Managers
        
    def tskListenerPolling(self,taskdata):
        if self.cListener.newConnectionAvailable():
            rendezvous = PointerToConnection()
            netAddress = NetAddress()
            newConnection = PointerToConnection()
            
            if self.cListener.getNewConnection(rendezvous,netAddress,newConnection):
                newConnection = newConnection.p()
                self.activeConnections.append(newConnection) # Remember connection
                self.cReader.addConnection(newConnection)     # Begin reading connection
                self.broadCast(newConnection) #Broadcasts the Server Message
        return Task.cont
    
    def tskReaderPolling(self,taskdata):
        if self.cReader.dataAvailable():
            datagram = NetDatagram()  # catch the incoming data in this instance
            # Check the return value; if we were threaded, someone else could have
            # snagged this data before we did
            if self.cReader.getData(datagram):
                myProcessDataFunction(datagram)
        return Task.cont
    
    def setTaskManagers(self):
        taskMgr.add(self.tskListenerPolling,"Poll the connection listener",-39)
        taskMgr.add(self.tskReaderPolling,"Poll the connection reader",-40)
        
    '''
    Terminate all connections.
    '''
    def terminateAllConnection(self):
        for aClient in self.activeConnections:
            self.cReader.removeConnections(aClient)
        self.activeConnections = []
        #Close our listener
        self.cManager.closeConnection(self.tcpSocket)
        
    '''
    Terminate a connection.
    '''
    def terminateConnection(self, aClient):
        self.cReader.removeConnections(aClient)
        
    '''
    PyDatagram for messages
    Arguments: message must be a string
    '''
    def messageData(self, message):
        messDat = PyDatagram()
        messDat.addUint8(PRINT_MESSAGE)
        messDat.addString(message)
        return messDat
    
    '''
    Broadcast Server Message
    '''
    def broadCast(self, aClient):
        message = self.messageData("Welcome to BaziBaz's Server\nConnection has been estabilished\n")
        self.cWriter.send(message, aClient)

class Client(DirectObject):
    def __init__(self):
        self.cManager = QueuedConnectionManager()
        self.cReader = QueuedConnectionReader(self.cManager, 0)
        self.cWriter = ConnectionWriter(self.cManager,0)
        self.connection = None #Connection with the server
        
    def connectToServer(self, ip_address="192.168.1.110", port_address=9099):
        #How long to wait until we give up connecting
        timeout = 3000 # 3 seconds
        self.connection = self.cManager.openTCPClientConnection(ip_address,port_address,timeout)
        if self.connection:
            self.cReader.addConnection(self.connection) #Retrieve message from Server
            return True #We connected
        return False #We couldn't succeed
    
    def processMsgData(self, dataGram):
        iterator = PyDatagramIterator(dataGram)
        msgID = iterator.getUint8()
        if msgID == PRINT_MESSAGE:
            msg = iterator.getString()
            print msg
    
    def recieveMessage(self):
        datagram = NetDatagram() #Needed to store the message or data recieved
        if self.cReader.getData(datagram):
            self.processMsgData(datagram)
            
    
    '''
    Closes the connection with the server
    '''
    def disconnectServer(self):
        self.cManager.closeConnection(self.connection)