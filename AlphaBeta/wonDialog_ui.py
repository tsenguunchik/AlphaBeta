# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\wonDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(266, 116)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #008CBA;\n"
"color: white;\n"
"font-size: 16px;\n"
"padding: 5px 0;\n"
"border: 0;\n"
"font-family: \"Comic Sans MS\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: blue;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Congratulations!"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter your name..."))
        self.pushButton.setText(_translate("Form", "Submit"))
        self.label.setText(_translate("Form", "You Won!"))

import icons_rc
