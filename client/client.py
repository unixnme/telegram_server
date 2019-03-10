import socket

class Client(object):
    def __init__(self, host:str='localhost', port:int=9876):
        self.host = host
        self.port = port

    def send(self, msg:str) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            sock.sendall(bytes(msg, 'utf-8'))

            received = str(sock.recv(1024), 'utf-8')
            if received == 'ok':
                return True
            else:
                return False

