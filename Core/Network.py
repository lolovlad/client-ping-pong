from socket import *
from json import *
from Class.Interfase.ISolid import Solide


class NetWork(metaclass=Solide):
    def __init__(self):
        self.__ip = None
        self.__port = None
        self.__socket = socket()

    def __call__(self, ip, port):
        self.__ip = ip
        self.__port = port
        self.__socket.connect((ip, port))

    def listener(self):
        try:
            message = self.__socket.recv(1024).decode()
            js_convert_message = loads(message)
            return js_convert_message
        except ConnectionResetError:
            return None

    def send_message(self, message):
        message = dumps(message)
        self.__socket.send(message.encode())

    def close(self):
        self.__socket.close()

    def get_socket(self):
        return self.__socket
