# -*- coding: utf-8 -*-
from lab02 import romantodeci, decitoroman
from flipbit import flipbit
from socket import * #imports the socket module
serverPort = 12000 #what serverport that the socket uses
serverSocket = socket(AF_INET, SOCK_DGRAM)#creates the servers socket, it is in the network part and consist op what version of IP is uses in this case IPv4 and last part is that it is in UDP
serverSocket.bind(('', serverPort))
print "The server is ready to receive" #message when you can use the server
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)#where the message is where the datapackets are put in and clientAddress is where the address and ports to the client is stored. serverSocket.recvfrom is where the data is recived from the socket
    finalmessage = '' 
    if message[:2] =="rm":
        finalmessage = str(romantodeci(message[2:]))
    else:
           
        for letter in message.decode('utf-8'):
            flipped = flipbit(letter.encode('utf-8'))
            if len(flipped) == 2:
                a = flipped[0]
                b = flipped[1]
                unia = chr(int(a.decode("utf-8"),2))
                unib = chr(int(b.decode("utf-8"),2))
                unified = unia + unib
                finalmessage += unified
            else:
                finalmessage += chr(int(str(flipped),2)) #

   # utfmessage = message.decode('utf-8')#decodes the message to utf-8 
   # modifiedMessage = utfmessage.upper() #moddifies the message to uppercase
    # print modifiedMessage 
    serverSocket.sendto(finalmessage, clientAddress) #send the modifes messages to the client, and encode the utf-8 characters
