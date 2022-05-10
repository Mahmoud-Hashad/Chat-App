from asyncio import constants
import eel
import socket
from threading import Thread
import json


server = None
 
configs = {
    "username": "user",
    "host": "localhost",
    "port": 12345
}



@eel.expose
def connect(username, host, port):
    set_configs(username, host, port)
    create_socket()


def set_configs(username, host, port):
    configs['username'] = username
    configs['host'] = host
    configs['port'] = int(port)





def create_socket():
    global server
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((configs['host'], configs['port']))
    except:
        exit(0)


def recv():
    global server
    while True:
        try:
            json = server.recv(2048)
            if json:
                json = json.decode()
                eel.recive_message(json)
                print(json)     
        except:
            exit(0)

           
@eel.expose
def send(message):
    print(message)
    data = {
        'name': configs['username'],
        'message': message,
    }

    json_data = json.dumps(data).encode()
    print(json_data)
    server.send(json_data)


@eel.expose
def start():
    Thread(target=recv).start()
    eel.set_name(configs['username'])
    


