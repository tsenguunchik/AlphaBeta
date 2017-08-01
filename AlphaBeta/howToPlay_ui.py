# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\howToPlay.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(517, 343)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        Form.setFont(font)
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
"QLabel{\n"
"font-family: \"Comic Sans MS\";\n"
"font-size: 12px;\n"
"}\n"
"\n"
"QLabel#label{\n"
"font-size:16px;\n"
"font-weight: bold;\n"
"background-color: rgb(170, 255, 255);\n"
"}\n"
"\n"
"QLabel#label_6{\n"
"font-weight: bold;\n"
"text-decoration: underline;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: blue;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMinimumSize(QtCore.QSize(400, 70))
        self.frame.setStyleSheet("QFrame#frame{\n"
"background-image: url(:/myFormula.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 7, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 8, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 9, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
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
        Form.setWindowTitle(_translate("Form", "How To Play - Guide"))
        self.label_6.setText(_translate("Form", "Objective:"))
        self.label_3.setText(_translate("Form", "• You have to guess the randomly generated number using the given hints."))
        self.label_5.setText(_translate("Form", "• After each guess, you get a clue."))
        self.label_7.setText(_translate("Form", "• You get \'alpha\' for every digit that you guess correctly if its in the correct position"))
        self.label_8.setText(_translate("Form", "• You get \'beta\' for every digit that you guess correctly but if its in a different position"))
        self.label_4.setText(_translate("Form", "• The score is calculated by the following formula:"))
        self.label_2.setText(_translate("Form", "• You choose the length of the number(3 - 9) in Options Menu"))
        self.pushButton.setText(_translate("Form", "Close"))
        self.label.setText(_translate("Form", "How To Play"))

import icons_rc
