'''
Created on Feb 16, 2012

@author: Eran-Tasker
'''
#These two lines allow the server and client to run without the window
#from pandac.PandaModules import ConfigVariableString 
#ConfigVariableString("window-type", "none").setValue("none")
from server_and_client import Server

Server = Server()
'''
while True:
    if Server.activeConnections and time != 0:
        Server.broadCast(Server.activeConnections[0])

Server.terminateAllConnection()
'''
run()