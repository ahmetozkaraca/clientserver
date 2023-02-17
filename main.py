from interface import *
from PySide2.QtWidgets import QApplication,QMainWindow



if __name__ == "__main__":
	import sys
	application = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	window.create_server()
	window.start_requirements_server()
	sys.exit(application.exec_())

	"""
YAPILACAKLAR

isimlendirmeler düzeltilecek,  CamelCase   snake_case
methodların içeriği sadeleştirelecek. tek görevi olacak

def reconnect(self): sadece client servera bağlanması şeklinde olacak server hiç kapanmıyacak client program çalışmaya başladığında kapalı kalacak bağlan butonuna basınca client açılacak bağlantıyı kes butonuna basınca clint tekrar kapanacak


"""