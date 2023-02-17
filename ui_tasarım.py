# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tasar�maLqpos.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButtonGnder = QPushButton(self.centralwidget)
        self.pushButtonGnder.setObjectName(u"pushButtonGnder")

        self.gridLayout.addWidget(self.pushButtonGnder, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.plainTextEdit_2Client = QPlainTextEdit(self.frame)
        self.plainTextEdit_2Client.setObjectName(u"plainTextEdit_2Client")

        self.gridLayout_2.addWidget(self.plainTextEdit_2Client, 1, 0, 1, 1)

        self.plainTextEditServer = QPlainTextEdit(self.frame)
        self.plainTextEditServer.setObjectName(u"plainTextEditServer")

        self.gridLayout_2.addWidget(self.plainTextEditServer, 1, 2, 1, 1)

        self.label_2Server = QLabel(self.frame)
        self.label_2Server.setObjectName(u"label_2Server")

        self.gridLayout_2.addWidget(self.label_2Server, 0, 0, 1, 1)

        self.labelServer = QLabel(self.frame)
        self.labelServer.setObjectName(u"labelServer")

        self.gridLayout_2.addWidget(self.labelServer, 0, 2, 1, 1)

        self.answer_lineEdit = QLineEdit(self.frame)
        self.answer_lineEdit.setObjectName(u"answer_lineEdit")

        self.gridLayout_2.addWidget(self.answer_lineEdit, 2, 0, 1, 3)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)

        self.pushButtonsil = QPushButton(self.centralwidget)
        self.pushButtonsil.setObjectName(u"pushButtonsil")

        self.gridLayout.addWidget(self.pushButtonsil, 1, 1, 1, 1)

        self.pushButtonbaglan = QPushButton(self.centralwidget)
        self.pushButtonbaglan.setObjectName(u"pushButtonbaglan")

        self.gridLayout.addWidget(self.pushButtonbaglan, 2, 0, 1, 1)

        self.pushButtonkes = QPushButton(self.centralwidget)
        self.pushButtonkes.setObjectName(u"pushButtonkes")

        self.gridLayout.addWidget(self.pushButtonkes, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonGnder.setText(QCoreApplication.translate("MainWindow", u"g\u00f6nder", None))
        self.label_2Server.setText(QCoreApplication.translate("MainWindow", u"client", None))
        self.labelServer.setText(QCoreApplication.translate("MainWindow", u"server", None))
        self.pushButtonsil.setText(QCoreApplication.translate("MainWindow", u"sil", None))
        self.pushButtonbaglan.setText(QCoreApplication.translate("MainWindow", u"ba\u011flan", None))
        self.pushButtonkes.setText(QCoreApplication.translate("MainWindow", u"ba\u011flan\u0131y\u0131 kes", None))
    # retranslateUi

