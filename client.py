import socket
import threading
from PySide2.QtCore import Signal,QObject

class Client(QObject):
    new_message_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.port = 12345
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.client_active = True

    def start_client(self):
        self.client_socket.connect((self.host, self.port))
        self.start_read_data_thread()
            #self.client_socket.close()
    
    def read_data(self):
        while self.client_active:
            try:
                self.data = self.client_socket.recv(1024).decode()
                print("data gelen",self.data)
                self.new_message_signal.emit(self.data)
            except:
                pass

    def start_read_data_thread(self):
        threading.Thread(target=self.read_data,daemon=True).start()

    def close(self):
        self.client_active = False
        self.client_socket.close()
    
    def send_message(self,message):
        self.client_socket.send(message.encode("utf-8"))
    