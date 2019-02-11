import socket
import pickle

from constant import  max_message_len

def envoyer(dest,message):
    to_send = pickle.dumps(message)
    return dest.send(to_send)

def recevoir(rec):
    rep = rec.recv(max_message_len)
    return pickle.loads(rep)

def built_message(message,need_answer):
    """ on envoie un tupple avec le message suivie d'un boolean """
    return (message,need_answer)

def envoyer_message(dest,message,need_answer = False):
    to_send = built_message(message,need_answer)
    envoyer(dest,to_send)
    if need_answer:
        return recevoir_message(dest)
    else:
        return

def recevoir_message(rec):
    rep = recevoir(rec)
    print(rep[0])
    if rep[1]:
        message = input(">")
        envoyer_message(rec,message)
    return rep[0]

def encrypt(message,passphrase):
    """ message and passphrase needs to be encoded """
    rep = []
    n,m = len(message),len(passphrase)
    for i in range(n):
        rep.append(message[i] ^ passphrase[i%m])
    return rep

def decrypt(message,passphrase):
    """ message and passphrase needs to be encoded """
    rep = []
    n,m = len(message),len(passphrase)
    for i in range(n):
        rep.append(message[i] ^ passphrase[i%m])
    return rep
