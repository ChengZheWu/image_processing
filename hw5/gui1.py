# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(457, 283)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        Form.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 20, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setObjectName("label")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(40, 120, 83, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(40, 90, 83, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(40, 150, 101, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(40, 180, 141, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(Form)
        self.radioButton_5.setGeometry(QtCore.QRect(40, 210, 111, 16))
        self.radioButton_5.setObjectName("radioButton_5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 261, 16))
        self.label_2.setObjectName("label_2")
        self.radioButton_6 = QtWidgets.QRadioButton(Form)
        self.radioButton_6.setGeometry(QtCore.QRect(40, 240, 111, 16))
        self.radioButton_6.setObjectName("radioButton_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Load Data"))
        self.pushButton_2.setText(_translate("Form", "Plot"))
        self.label.setText(_translate("Form", "Choose a file"))
        self.radioButton_2.setText(_translate("Form", "CMY"))
        self.radioButton.setText(_translate("Form", "RGB"))
        self.radioButton_3.setText(_translate("Form", "HSI"))
        self.radioButton_4.setText(_translate("Form", "XYZ"))
        self.radioButton_5.setText(_translate("Form", "L*a*b"))
        self.label_2.setText(_translate("Form", "Choose a file and select a following item before plotting"))
        self.radioButton_6.setText(_translate("Form", "YUV"))
