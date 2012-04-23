'''
Created on Mar 30, 2012

@author: Benjamin
'''
from direct.showbase.DirectObject import DirectObject    

from pandac.PandaModules import ConfigVariableString 
ConfigVariableString("window-type", "none").setValue("none") 
import direct.directbase.DirectStart 
from direct.task import Task 
from pandac.PandaModules import QueuedConnectionManager, QueuedConnectionReader, ConnectionWriter, QueuedConnectionListener 
from direct.distributed.PyDatagram import PyDatagram 
from direct.distributed.PyDatagramIterator import PyDatagramIterator 

class Client(DirectObject): 
    def __init__( self ): 
        print "Initializing client test" 
        
        self.port = 9099
        self.ip_address = "192.168.1.110" 
        self.timeout = 3000             # 3 seconds to timeout 
        
        self.cManager = QueuedConnectionManager() 
        self.cListener = QueuedConnectionListener(self.cManager, 0) 
        self.cReader = QueuedConnectionReader(self.cManager, 0) 
        self.cWriter = ConnectionWriter(self.cManager,0) 
        
        self.Connection = self.cManager.openTCPClientConnection(self.ip_address, self.port, self.timeout) 
        if self.Connection: 
            taskMgr.add(self.tskReaderPolling,"read the connection listener",-40) 
            # this tells the client to listen for datagrams sent by the server 
            
            print "Connected to Server" 
            self.cReader.addConnection(self.Connection) 
            PRINT_MESSAGE = 1 
            myPyDatagram = PyDatagram() 
            myPyDatagram.addUint8(100) 
            # adds an unsigned integer to your datagram 
            myPyDatagram.addString("first string of text") 
            # adds a string to your datagram 
            myPyDatagram.addString("second string of text") 
            # adds a second string to your datagram 
            self.cWriter.send(myPyDatagram, self.Connection) 
            # fires it off to the server 
            
            #self.cManager.closeConnection(self.Connection) 
            #print "Disconnected from Server" 
            # uncomment the above 2 lines if you want the client to 
            # automatically disconnect.  Or you can just 
            # hit CTRL-C twice when it's running to kill it 
            # in windows, I don't know how to kill it in linux 
        else: 
            print "Not connected to Server" 
        
    def tskReaderPolling(self, task): 
        if self.cReader.dataAvailable(): 
            datagram=PyDatagram()  
            if self.cReader.getData(datagram): 
                self.processServerMessage(datagram) 
        return Task.cont        
    
    def processServerMessage(self, netDatagram): 
        myIterator = PyDatagramIterator(netDatagram) 
        #print myIterator.getString()
        print myIterator.getClassType() 
        
Client = Client() 
run() 