import hashlib
import communication as com
from constant import max_login_len,max_passwd_len,max_message_len,users_dict

def new_users(login,password):
    """ ajoute un client au server """
    if len(login)>max_login_len or len(password)>max_passwd_len:
        return "Too long"
    if not login in users_dict:
        users_dict[login] = hashlib.md5(password.encode()).hexdigest()
        return "Succesfully signed up"
    else:
        return "Username already took"

def check_connexion(login,password):
    """ verifie si le client est deja dans la base
        input : login (str), password (str)
        output : 0 if okay,1 if wrong password,2 if uknown client,4 wrong parameter
    """
    if len(login)>max_login_len or len(password)>max_passwd_len:
        return 4
    if login in users_dict:
        if users_dict[login] == hashlib.md5(password.encode()).hexdigest():
            return 0
        else:
            return 1
    else:
        return 2

def get_info(list_clients,client):
    """ return 0 if client not found """
    for i in list_clients:
        if i[0] == client:
            return i[1]
    return 0

def new_connection(connect):
    """ return client """
    client,info_client = connect.accept()
    rr = 4 # on attend d'avoir les bonnes longueurs
    users,password = "",""
    while rr != 0:
        print(users_dict)
        rep = com.envoyer_message(client,'What do you want to do ?\n1-Connection\n2-Create account\n3- Abort',True)
        if rep == '1':
            users = com.envoyer_message(client,'User :',True)
            password = com.envoyer_message(client,'Password :',True)
            rr = check_connexion(users,password)
            if rr != 0:
                com.envoyer_message(client,'Erreur lors de la connection')
        elif rep == '2':
            com.envoyer_message(client,'Suscribing')
            users = com.envoyer_message(client,'User :',True)
            password = com.envoyer_message(client,'Password :',True)
            com.envoyer_message(client,new_users(users,password))
        else:
            com.envoyer_message(client,'Aborting...')
            return
    com.envoyer_message(client,'Succesfully connected')
    return (client,users)
