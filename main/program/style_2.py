# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_2.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(837, 574)
        Dialog.setStyleSheet("background-color: #3A3A3A;")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 531, 41))
        self.label.setStyleSheet("color: #FFEB2C;\n"
"font: 87 18pt \"Arial Black\";\n"
"text-size: 500px;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 340, 391, 181))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(80, 80, 80);\n"
"    color: rgb(255, 235, 44);\n"
"    font: 87 18pt \"Arial\";\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(109, 109, 109);\n"
"    color: rgb(255, 235, 44);\n"
"    font: 87 18pt \"Arial\";\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(67, 67, 67);\n"
"    color: rgb(207, 207, 207);\n"
"    font: 87 18pt \"Arial\";\n"
"    border: none;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 340, 391, 181))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(80, 80, 80);\n"
"    color: rgb(255, 235, 44);\n"
"    font: 87 18pt \"Arial\";\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(109, 109, 109);\n"
"    color: rgb(255, 235, 44);\n"
"    font: 87 18pt \"Arial\";\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(67, 67, 67);\n"
"    color: rgb(207, 207, 207);\n"
"    font: 87 18pt \"Arial\";\n"
"    border: none;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Longpoll v 3.0.1 beta"))
        self.label.setText(_translate("Dialog", "Longpoll v 3.0.1 beta by Nikitol"))
        self.pushButton.setText(_translate("Dialog", "Перезапустить longpoll"))
        self.pushButton_2.setText(_translate("Dialog", "Отключить longpoll"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
