'''
Created on Mar 30, 2012

@author: Benjamin
'''
from direct.showbase.DirectObject import DirectObject  
from direct.task import Task 
from pandac.PandaModules import ConfigVariableString 
ConfigVariableString("window-type", "none").setValue("none") 
import direct.directbase.DirectStart 
# These are the  Panda libraries needed for everything else 
# to function properly.  The configvariable bit disables the 
# standard window that opens, as the server doesn't need to continually 
# re-draw a window - it just needs to to output to the command prompt 

from panda3d.core import * 

from pandac.PandaModules import QueuedConnectionManager, QueuedConnectionReader, ConnectionWriter, QueuedConnectionListener, NetAddress 
from direct.distributed.PyDatagram import PyDatagram 
from direct.distributed.PyDatagramIterator import PyDatagramIterator 
# panda's built-in networking code for TCP networking 

class Server(DirectObject): 
    def __init__( self ): 
        self.port = 50114
        self.portStatus = "Closed" 
        self.host = "localhost" 
        self.backlog = 1000 
        self.Connections = {} 
        # basic configuration variables that are used by most of the 
        # other functions in this class 

        self.StartConnectionManager() 
        # manages the connection manager 
        
        self.DisplayServerStatus() 
        # output a status box to the console which tells you the port 
        # and any connections currently connected to your server 
        
    def DisplayServerStatusTASK(self, task): 
        # all this does is periodically load the status function below 
        # add a task to display it every 30 seconds while you are doing 
        # any new coding 
        self.DisplayServerStatus() 
        return Task.again 
    
    def DisplayServerStatus(self): 
        print "\n----------------------------------------------------------------------------\n" 
        print "SERVER STATUS:\n\n" 
        print "Connection Manager Port: " + str(self.port)  + " [" + str(self.portStatus) + "]" 
        for k, v in self.Connections.iteritems(): 
            print "Connection " + k 

    ################################################################## 
    #              TCP Networking Functions and Tasks 
    ################################################################## 
        
    def StartConnectionManager(self): 
        # this function creates a connection manager, and then 
        # creates a bunch of tasks to handle connections 
        # that connect to the server 
        self.cManager = QueuedConnectionManager() 
        self.cListener = QueuedConnectionListener(self.cManager, 0) 
        self.cReader = QueuedConnectionReader(self.cManager, 0) 
        self.cWriter = ConnectionWriter(self.cManager,0) 
        self.tcpSocket = self.cManager.openTCPServerRendezvous(self.port,self.backlog)
        self.cListener.addConnection(self.tcpSocket) 
        self.portStatus = "Open" 
        taskMgr.add(self.ConnectionManagerTASK_Listen_For_Connections,"Listening for Connections",-39) 
        # This task listens for new connections 
        taskMgr.add(self.ConnectionManagerTASK_Listen_For_Datagrams,"Listening for Datagrams",-40) 
        # This task listens for new datagrams 
        taskMgr.add(self.ConnectionManagerTASK_Check_For_Dropped_Connections,"Listening for Disconnections",-41) 
        # This task listens for disconnections 
        
    def ConnectionManagerTASK_Listen_For_Connections(self, task): 
        if(self.portStatus == "Open"): 
        # This exists in case you want to add a feature to disable your 
        # login server for some reason.  You can just put code in somewhere 
        # to set portStatus = 'closed' and your server will not 
        # accept any new connections 
            if self.cListener.newConnectionAvailable(): 
                print "CONNECTION" 
                rendezvous = PointerToConnection() 
                netAddress = NetAddress() 
                newConnection = PointerToConnection() 
                if self.cListener.getNewConnection(rendezvous,netAddress,newConnection): 
                    newConnection = newConnection.p() 
                    self.Connections[str(newConnection.this)] = rendezvous 
                    # all connections are stored in the self.Connections 
                    # dictionary, which you can use as a way to assign 
                    # unique identifiers to each connection, making 
                    # it easy to send messages out 
                    self.cReader.addConnection(newConnection)    
                    print "\nSOMEBODY CONNECTED" 
                    print "IP Address: " + str(newConnection.getAddress()) 
                    print "Connection ID: " + str(newConnection.this) 
                    print "\n" 
                    # you can delete this, I've left it in for debugging 
                    # purposes 
                    self.DisplayServerStatus()                
                    # this fucntion just outputs the port and 
                    # current connections, useful for debugging purposes 
        return Task.cont  

    def ConnectionManagerTASK_Listen_For_Datagrams(self, task): 
        if self.cReader.dataAvailable(): 
            datagram=NetDatagram()  
            if self.cReader.getData(datagram): 
                print "\nDatagram received, sending response" 
                myResponse = PyDatagram() 
                myResponse.addString("GOT YER MESSAGE") 
                self.cWriter.send(myResponse, datagram.getConnection()) 
                # this was just testing some code, but the server will 
                # automatically return a 'GOT YER MESSAGE' datagram 
                # to any connection that sends a datagram to it 
                # this is where you add a processing function here 
                #myProcessDataFunction(datagram) 
        return Task.cont 

    def ConnectionManagerTASK_Check_For_Dropped_Connections(self, task): 
        # if a connection has disappeared, this just does some house 
        # keeping to officially close the connection on the server, 
        # if you don't have this task the server will lose track 
        # of how many people are actually connected to you 
        if(self.cManager.resetConnectionAvailable()): 
            connectionPointer = PointerToConnection() 
            self.cManager.getResetConnection(connectionPointer) 
            lostConnection = connectionPointer.p() 
            # the above pulls information on the connection that was lost 
            print "\nSOMEBODY DISCONNECTED" 
            print "IP Address: " + str(lostConnection.getAddress()) 
            print "ConnectionID: " + str(lostConnection.this) 
            print "\n" 
            del self.Connections[str(lostConnection.this)] 
            # remove the connection from the dictionary 
            self.cManager.closeConnection(lostConnection) 
            # kills the connection on the server 
            self.DisplayServerStatus() 
        return Task.cont 
  

Server = Server() 
run() 