'''
Created on Mar 15, 2012

@author: Benjamin
'''
from direct.task.TaskNew import TaskManager
#Network imports
from pandac.PandaModules import QueuedConnectionManager
from pandac.PandaModules import QueuedConnectionListener
from pandac.PandaModules import QueuedConnectionReader
from pandac.PandaModules import ConnectionWriter

class Server():
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
 
        self.cListener.addConnection(tcpSocket)
        
    def tskListenerPolling(self,taskdata):
        if self.cListener.newConnectionAvailable():
            rendezvous = PointerToConnection()
            netAddress = NetAddress()
            newConnection = PointerToConnection()
            
            if self.cListener.getNewConnection(rendezvous,netAddress,newConnection):
                newConnection = newConnection.p()
                self.activeConnections.append(newConnection) # Remember connection
                self.cReader.addConnection(newConnection)     # Begin reading connection
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
        taskMgr.add(tskListenerPolling,"Poll the connection listener",-39)
        taskMgr.add(tskReaderPolling,"Poll the connection reader",-40)
        
    '''
    Terminate all connections.
    '''
    def terminateConnection(self):
        for aClient in self.activeConnections:
            self.cReader.removeConnections(aClient)
        self.activeConnections = []
        #Close our listener
        self.cManager.closeConnection(self.tcpSocket)
        
    '''
    Terminate a connection.
    '''
    def terminateConnection(self, aClient):
        for aClient in self.activeConnections:
            self.cReader.removeConnections(aClient)
        self.activeConnections = []
        #Close our listener
        self.cManager.closeConnection(self.tcpSocket)
        
class Client():
    def __init__(self):
        self.cManager = QueuedConnectionManager()
        self.cReader = QueuedConnectionReader(self.cManager, 0)
        self.cWriter = ConnectionWriter(self.cManager,0)