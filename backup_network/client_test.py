'''
Created on Mar 2, 2012

@author: Eran-Tasker
'''
#These two lines allow the server and client to run without the window
#from pandac.PandaModules import ConfigVariableString 
#ConfigVariableString("window-type", "none").setValue("none")
from server_and_client import Client

attempts = 5

Client = Client()
while Client.connectToServer() == False:
    attempts = attempts - 1
    if attempts == 0:
        exit()

#while True:
#    Client.recieveMessage()

#Client.disconnectServer()
run()