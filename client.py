import socket

class Client:
    def __init__(self):
        self.port = 12345
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()

    def start_client(self):
        self.client_socket.connect((self.host, self.port))
        while True:
            self.data = self.client_socket.recv(1024).decode()
            #self.client_socket.close()

    def disconnect(self):
        self.client_socket.close()