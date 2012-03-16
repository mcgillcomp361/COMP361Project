'''
Created on Mar 2, 2012

@author: Eran-Tasker
'''

from server_and_client import Client

attempts = 5

Client = Client()
while Client.connectToServer() == False:
    attempts = attempts - 1
    if attempts == 0:
        exit()

while True:
    Client.recieveMessage()

Client.disconnectServer()
run()