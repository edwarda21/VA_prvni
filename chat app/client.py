import kivy
from kivy.app import App
from kivy.lang import Builder
import socket
from client_lib import *

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# socket_connect(sock)
# msg = sock.recv(1024)
# print(msg.decode('ascii'))
# sock.close()
kvfile = Builder.load_file('client_app.kv')

class client_App(App):
    def build(self):
        return kvfile

kvapp = client_App()
kvapp.run()