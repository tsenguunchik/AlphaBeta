# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\highscore.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(340, 400)
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
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setEnabled(False)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "High Score List"))
        self.pushButton.setText(_translate("Form", "Close"))
        self.label.setText(_translate("Form", "High Scores"))

import icons_rc
