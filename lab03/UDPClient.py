# -*- coding: utf-8 -*-

from socket import* #import the socket
serverName = 'localhost' #address to where the server is hosted
serverPort = 12000 #port that the server uses to communicate
clientSocket = socket(AF_INET, SOCK_DGRAM) #this is client's socket it created, it contains what the network is using like IPv4 and the last part is that it is UDP.
question = raw_input('1 for romersk matte eller 2 for stor og små bokstav?')
if question == '2':
    message = raw_input('Input lowercase sentence:') #you can type in a word in lowercaase
    utfmessage=message.decode('utf-8')
    clientSocket.sendto(utfmessage.encode('utf-8'),(serverName, serverPort)) #where the clienSocket sends it data to, it contains the messages, servers address and the serverport that it use to comunicate
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #packets data is put in to the variable modifiedMessage, the port and servername is stored in the serverAddress. the last part clientSocket.recvfrom is where the data recives from the clientSocket
    print modifiedMessage #print out a modified message, istead of lowercase it is now uppercase
    clientSocket.close() #The process terminates
else:
    message = raw_input('Skriv romertallene:')
    clientSocket.sendto('rm' + message,(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print modifiedMessage
    clientSocket.close()

