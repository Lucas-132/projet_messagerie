from threading import Thread
from socket import socket as Socket, AF_INET, SOCK_STREAM

class Client(Thread):
    def __init__(self, Host:str, Port:int):
        super().__init__()
        socket = Socket(AF_INET,SOCK_STREAM)
        socket.connect((Host,Port))
        
        while True:
            msg = input('->')
            msg = msg.encode('utf-8')
            socket.send(msg)

            requete_server = socket.recv(500)
            requete_server = requete_server.decode("utf-8")
            print(requete_server)