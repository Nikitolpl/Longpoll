# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: #3A3A3A;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #3A3A3A;")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 531, 41))
        self.label.setStyleSheet("color: #FFEB2C;\n"
"font: 87 18pt \"Arial Black\";\n"
"text-size: 500px;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 160, 331, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(80, 80, 80);\n"
"    color: rgb(255, 235, 44);\n"
"    font: 87 12pt \"Arial\";\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(109, 109, 109);\n"
"    color: rgb(255, 235, 44);\n"
"    font: 87 12pt \"Arial\";\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(67, 67, 67);\n"
"    color: rgb(207, 207, 207);\n"
"    font: 87 12pt \"Arial\";\n"
"    border: none;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 430, 271, 91))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(80, 80, 80);\n"
"    color: rgb(255, 235, 44);\n"
"    font: 87 12pt \"Arial\";\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(109, 109, 109);\n"
"    color: rgb(255, 235, 44);\n"
"    font: 87 12pt \"Arial\";\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(67, 67, 67);\n"
"    color: rgb(207, 207, 207);\n"
"    font: 87 12pt \"Arial\";\n"
"    border: none;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 90, 511, 51))
        self.lineEdit.setStyleSheet("background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 235, 44);\n"
"font: 9pt \"Arial\";\n"
"border: none;")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Longpoll v 3.0 beta"))
        self.label.setText(_translate("MainWindow", "Longpoll v 3.0 beta by Nikitol"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить токен"))
        self.pushButton_2.setText(_translate("MainWindow", "Запустить longpoll"))
        self.lineEdit.setText(_translate("MainWindow", "Ваш токен"))
