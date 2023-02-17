from server import Server
from client import Client
from PySide2.QtWidgets import QMainWindow, QApplication
from ui_tasarım import Ui_MainWindow
import threading

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.create_client()
        self.create_server()

    def create_server(self):
        """
        Bu fonksiyon server başlatır.
        """
        self.server = Server()
    
    def create_client(self):
        self.client = Client()

    def start_requirements_server(self):
        
        threading.Thread(target=self.server.start_server, daemon=True).start()
        # self.server.start_server()

    def start_requirements_client(self):

        threading.Thread(target=self.client.start_client, daemon=True).start()

    def init_ui(self):
        
        self.ui.pushButtonGnder.clicked.connect(self.send_message)
        self.ui.pushButtonsil.clicked.connect(self.clear)
        self.ui.pushButtonkes.clicked.connect(self.close_connection)
        self.ui.pushButtonbaglan.clicked.connect(self.reconnect) 
        
                

    def clear(self):
        self.client.disconnect()
        self.ui.plainTextEdit_2Client.setPlainText("")
        self.ui.plainTextEditServer.setPlainText("")


    def send_message(self):
       
        self.message = self.ui.answer_lineEdit.text()
        self.ui.answer_lineEdit.setText("")
        self.client.client_socket.send(self.message.encode('utf-8'))
        self.ui.plainTextEdit_2Client.appendPlainText(self.message)
        answer = self.client.client_socket.recv(1024).decode('utf-8')
        self.ui.plainTextEditServer.appendPlainText(answer)
            
        # except  OSError:
            # self.ui.plainTextEdit_2Client.setPlainText("")

    def close_connection(self):
        self.client.disconnect()
        self.ui.plainTextEdit_2Client.appendPlainText('Bağlantı kesildi')

    def reconnect(self):
        
            self.client.disconnect()
            self.create_client()
            self.start_requirements_client()
        # self.start_requirements_server()
            self.ui.plainTextEditServer.appendPlainText('Bağlandı')

         
