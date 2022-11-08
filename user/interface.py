import datetime



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDataStream, QIODevice
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import QDialog, QPushButton

import utils


class Ui_MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.tcpSocket = QTcpSocket(self)
        self.blockSize = 0
        self.make_request()
        self.tcpSocket.waitForConnected(10)
        self.tcpSocket.readyRead.connect(self.deal_communication)
        self.tcpSocket.error.connect(self.display_error)

    def make_request(self):
        self.tcpSocket.connectToHost(utils.IP, utils.PORT, QIODevice.ReadWrite)

    def deal_communication(self):
        _translate = QtCore.QCoreApplication.translate
        socket = QDataStream(self.tcpSocket)
        socket.setVersion(QDataStream.Qt_5_0)
        if self.blockSize == 0:
            if self.tcpSocket.bytesAvailable() < 2:
                return
            self.blockSize = socket.readUInt16()
        if self.tcpSocket.bytesAvailable() < self.blockSize:
            return
        data = str(socket.readString())
        # Где-то тут будет перевод из QByteArray в строку
        if len(data) < 3: #Нужна другая реализация, чтобы отличать запросы
            self.label_4.setText(_translate("MainWindow", "Output 22"))
        else:
            self.label_3.SetText(data)
        # Как подключить класс Клиента для соеденения к классу интерфейса, хотя скорее все в 1 класс

    def display_error(self):
        pass

    def request_for_fast_response(self, data):
        #Прикрепить к кнопке, функционал +- из test_server
        pass

    def request_for_slow_response(self, delay):
        pass

    def test(self):
        print(datetime.datetime.now())

    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(704, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(210, 50, 104, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 140, 120, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 220, 120, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(210, 140, 104, 40))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(210, 220, 104, 40))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 140, 320, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 220, 320, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 140, 320, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 704, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Введите порт:"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.label_2.setText(_translate("MainWindow", "Output 1:"))
        self.label_3.setText(_translate("MainWindow", "Output 2"))
        self.pushButton.clicked.connect(self.request_for_fast_response)
        self.pushButton_2.clicked.connect(self.request_for_slow_response)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
