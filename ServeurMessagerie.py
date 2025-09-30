from threading import Thread
from socket import socket as Socket, AF_INET, SOCK_STREAM

class ServeurMessagerie(Thread):
    def __init__(self, Host:str, Port:int):
        super().__init__()
        socket = Socket(AF_INET,SOCK_STREAM)
        socket.bind((Host,Port))
        socket.listen(1)

        client, ip = socket.accept()
        print("Le client d'ip",ip,"s'est connecté")

        while True:
            requete_client = client.recv(500)
            requete_client = requete_client.decode('utf-8')
            print(requete_client)
            if not requete_client : #Si on perd la connexion
                print("CLOSE")
                break
            msg = input("->")
            msg = msg.encode("utf-8")
            client.send(msg)
        
        client.close()
        socket.close()

