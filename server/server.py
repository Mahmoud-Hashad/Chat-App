import socket

from _thread import start_new_thread
import string

HOST = "localhost"
PORT = 4444

class chat():
    def __init__(self, host, port):
        self.server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        
        self.server.bind((host, port))
        self.server.listen(100)

        self.clients_conn = []
    
    # wait for new connection
    def run(self):
        while True:
            try:
                conn, addr = self.server.accept()
                print(addr, 'is connected')
                self.clients_conn.append(conn)

                start_new_thread(self.clientthread,(conn, ))  
            except:
                continue


    # broadcast message to all chats
    def broadcast(self, message, sender_conn):
        for client_conn in self.clients_conn:
            if client_conn != sender_conn:
                try:
                    print('send> ', message)
                    client_conn.send(message)
                except:
                    continue

    # recive data from client
    def clientthread(self, client_conn):
        while True:
            try:
                message = client_conn.recv(2048)
                if message:
                    self.broadcast(message, client_conn)
            except:
                self.clients_conn.remove(client_conn)
                break
                    


  



chat_room =  chat(HOST, PORT)

chat_room.run()