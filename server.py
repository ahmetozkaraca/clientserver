import socket
import threading
from PySide2.QtCore import Signal,QObject

MESSAGE_RESPONSES = {
    "Naber?": "İyi, sen?",
    "Nerelisin?": "Sivas",
    "Kaç yaşındasın?": "25",
    "Nerde yaşıyorsun?": "Ankara",
    "Uçuşa hazır mısınız?": "Daima hazır"
}

class Server(QObject):
    new_message_signal = Signal(str,str)

    def __init__(self):
        super().__init__()
        self.port = 12345
        self.host = socket.gethostname()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_active = True
        self.new_message_signal.connect(self.send_answer)    
        self.server_socket.bind((self.host, self.port))
    
    def read_data(self,address):
        client_active = True
        address =str(address)
        while client_active:
            try:
                data = self.client_socket.recv(1024).decode()
                self.new_message_signal.emit(data,address)
            except :
                client_active = False
    
    def handle_clients(self):
        while self.server_active:
            self.server_socket.listen() 
            self.client_socket, self.client_address = self.server_socket.accept()
            threading.Thread(target=self.read_data,daemon=True,args=(self.client_address,)).start()

    def start_server(self):
        threading.Thread(target=self.handle_clients,daemon=True).start()

    def close_server(self):
        self.server_active = False
        self.server_socket.close()
    
    def send_answer(self,data):
        if data in MESSAGE_RESPONSES:
            answer = MESSAGE_RESPONSES[data]
        else:
            answer = 'bilinmeyen_soru'
        
        self.client_socket.send(answer.encode("utf-8"))
            