'''
Created on Feb 16, 2012

@author: Eran-Tasker
'''
from server_and_client import Server

time = 5000
Server = Server()
while True:
    if Server.activeConnections[0] and time != 0:
        Server.broadCast(Server.activeConnections[0])
        time = time - 1

Server.terminateAllConnection()    
run()