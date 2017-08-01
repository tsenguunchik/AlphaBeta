# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("QWidget#Form{\n"
"background-image: url(:bg.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-color: white;\n"
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
"}\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout.addWidget(self.frame_3, 1, 2, 3, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 3)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout.addWidget(self.frame_2, 1, 0, 3, 1)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Main Menu"))
        self.pushButton_2.setText(_translate("Form", "HighScore"))
        self.pushButton.setText(_translate("Form", "Start"))
        self.pushButton_3.setText(_translate("Form", "Options"))
        self.pushButton_4.setText(_translate("Form", "How To Play"))

import icons_rc
