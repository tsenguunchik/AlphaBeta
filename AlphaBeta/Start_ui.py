# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Start.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(434, 292)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget{\n"
"background-color: #fff;\n"
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
"\n"
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
"\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(69, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 4, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(69, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(69, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(69, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Guess My Number!"))
        self.label.setText(_translate("Form", "Guess my 4 digit number!"))
        self.pushButton.setText(_translate("Form", "Guess!"))
        self.label_2.setText(_translate("Form", "History:"))

import icons_rc
