import socket
import select
import func

from constant import port,max_message_len

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('',port))
server.listen(5)

print('Launching server...')

server_running = True

clients = []

while server_running:
    # On cherche les nouvelles connections
    nouvelles_connexions,wlist,xlist = select.select([server],[],[],0.05)
    for connexions in nouvelles_connexions:
        clients.append(func.new_connection(connexions))

    # On lit les messages reçu
    # renvoi erreur si liste vide
    to_read = []
    try:
        to_read,wlist,xlist = select.select([a[0] for a in clients],[],[],0.05)
    except select.error:
        pass
    else:
        for client in to_read:
            message = client.recv(max_message_len)
            message = message.decode()
            user = func.get_info(clients,client)
            print("Message reçu de la part de {}".format(user))
            print("Le message reçu : '{}'".format(message))
            client.send(b'message recu')
            if message == 'fin':
                server_running = False
print("Fermeture du server")
for client in clients:
    client[0].close()
server.close()
