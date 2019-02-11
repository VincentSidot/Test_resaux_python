import socket
import select
import communication as com

from constant import port,max_message_len


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',port))

#Phase de connection
while com.recevoir_message(client) != 'Aborting...':
    pass
print('Closing')
com.envoyer_message(client,'fin')
client.close()
