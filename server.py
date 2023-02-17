import socket

MESSAGE_RESPONSES = {
    "Naber?": "İyi, sen?",
    "Nerelisin?": "Sivas",
    "Kaç yaşındasın?": "25",
    "Nerde yaşıyorsun?": "Ankara",
    "Uçuşa hazır mısınız?": "Daima hazır"
}

class Server:
    def __init__(self):
        self.port = 12345
        self.host = socket.gethostname()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen() 
        self.client_socket, self.client_address = self.server_socket.accept()

        while True:
            try:
                data = self.client_socket.recv(1024).decode()

                if data in MESSAGE_RESPONSES:
                     message = MESSAGE_RESPONSES[data]
                else:
                    message = 'bilinmeyen_soru'

                self.client_socket.send(message.encode("utf-8"))

            except :
                pass
            #     print("")
                

        # self.client_socket.close()
        # self.server_socket.close()
