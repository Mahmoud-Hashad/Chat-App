import eel
import utils
import socket


# get localport
sock = socket.socket()
sock.bind(('', 0))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = sock.getsockname()[1]


eel.init('gui')
eel.start('login.html', port=port)
