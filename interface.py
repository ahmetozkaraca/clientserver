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

    def create_server(self):
        """
        Bu fonksiyon server başlatır.
        """
        self.server = Server()
        self.server.new_message_signal.connect(self.update_server_screen)

    def start_server(self):
        self.server.start_server()

    def create_client(self):
        self.client = Client()
        self.client.new_message_signal.connect(self.update_client_screen)

    def init_ui(self):
        self.ui.pushButtonGnder.clicked.connect(lambda:self.client.send_message(self.ui.answer_lineEdit.text()))
        self.ui.pushButtonsil.clicked.connect(self.clear_all_screen)
        self.ui.pushButtonkes.clicked.connect(self.close_client_connection)
        self.ui.pushButtonbaglan.clicked.connect(self.client_connect) 
            
    def clear_all_screen(self):
        self.ui.plainTextEdit_2Client.setPlainText("")
        self.ui.plainTextEditServer.setPlainText("")

    def close_client_connection(self):
        self.client.close()

    def client_connect(self):
        self.create_client()
        self.client.start_client()

    def update_server_screen(self,data,address):
        self.ui.plainTextEditServer.appendPlainText(f"{address}: {data}")

    def update_client_screen(self,data):
        self.ui.plainTextEdit_2Client.appendPlainText(data)
