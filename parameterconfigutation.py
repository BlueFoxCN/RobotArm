# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameterconfiguration.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os



class Ui_ParameterConfiguration(object):
    def setupUi(self, ParameterConfiguration):
        ParameterConfiguration.setObjectName("ParameterConfiguration")
        ParameterConfiguration.resize(538, 166)
        self.label_9 = QtWidgets.QLabel(ParameterConfiguration)
        self.label_9.setGeometry(QtCore.QRect(360, 20, 16, 21))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(ParameterConfiguration)
        self.label_11.setGeometry(QtCore.QRect(190, 60, 16, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(ParameterConfiguration)
        self.label_12.setGeometry(QtCore.QRect(360, 60, 16, 21))
        self.label_12.setObjectName("label_12")
        self.lineEdit_6 = QtWidgets.QLineEdit(ParameterConfiguration)
        self.lineEdit_6.setGeometry(QtCore.QRect(390, 60, 51, 27))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit = QtWidgets.QLineEdit(ParameterConfiguration)
        self.lineEdit.setGeometry(QtCore.QRect(50, 20, 51, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(ParameterConfiguration)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 20, 51, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(ParameterConfiguration)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 16, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(ParameterConfiguration)
        self.lineEdit_3.setGeometry(QtCore.QRect(390, 20, 51, 27))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_21 = QtWidgets.QPushButton(ParameterConfiguration)
        self.pushButton_21.setGeometry(QtCore.QRect(380, 120, 61, 27))
        self.pushButton_21.setObjectName("pushButton_21")
        self.label_8 = QtWidgets.QLabel(ParameterConfiguration)
        self.label_8.setGeometry(QtCore.QRect(190, 20, 16, 21))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(ParameterConfiguration)
        self.label_10.setGeometry(QtCore.QRect(20, 60, 16, 21))
        self.label_10.setObjectName("label_10")
        self.lineEdit_4 = QtWidgets.QLineEdit(ParameterConfiguration)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 60, 51, 27))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(ParameterConfiguration)
        self.lineEdit_5.setGeometry(QtCore.QRect(220, 60, 51, 27))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(ParameterConfiguration)
        self.lineEdit_7.setGeometry(QtCore.QRect(120, 20, 51, 27))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(ParameterConfiguration)
        self.lineEdit_8.setGeometry(QtCore.QRect(120, 60, 51, 27))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(ParameterConfiguration)
        self.lineEdit_9.setGeometry(QtCore.QRect(290, 60, 51, 27))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(ParameterConfiguration)
        self.lineEdit_10.setGeometry(QtCore.QRect(290, 20, 51, 27))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(ParameterConfiguration)
        self.lineEdit_11.setGeometry(QtCore.QRect(460, 60, 51, 27))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(ParameterConfiguration)
        self.lineEdit_12.setGeometry(QtCore.QRect(460, 20, 51, 27))
        self.lineEdit_12.setObjectName("lineEdit_12")

        self.retranslateUi(ParameterConfiguration)
        QtCore.QMetaObject.connectSlotsByName(ParameterConfiguration)

    def retranslateUi(self, ParameterConfiguration):
        _translate = QtCore.QCoreApplication.translate
        ParameterConfiguration.setWindowTitle(_translate("ParameterConfiguration", "参数配置"))
        self.label_9.setText(_translate("ParameterConfiguration", "J3"))
        self.label_11.setText(_translate("ParameterConfiguration", "J5"))
        self.label_12.setText(_translate("ParameterConfiguration", "J6"))
        self.label_7.setText(_translate("ParameterConfiguration", "J1"))
        self.pushButton_21.setText(_translate("ParameterConfiguration", "确定"))
        self.pushButton_21.clicked.connect(self.pushButton_21ClickedFunc)
        self.label_8.setText(_translate("ParameterConfiguration", "J2"))
        self.label_10.setText(_translate("ParameterConfiguration", "J4"))

    def pushButton_21ClickedFunc(self):
        print("call Ui_ParameterConfiguration.pushButton_21ClickedFunc")
        print("确定")

        j1left = self.lineEdit.text()
        j2left = self.lineEdit_2.text()
        j3left = self.lineEdit_3.text()
        j4left = self.lineEdit_4.text()
        j5left = self.lineEdit_5.text()
        j6left = self.lineEdit_6.text()

        j1right = self.lineEdit_7.text()
        j2right = self.lineEdit_10.text()
        j3right = self.lineEdit_12.text()
        j4right = self.lineEdit_8.text()
        j5right = self.lineEdit_9.text()
        j6right = self.lineEdit_11.text()

        f = open("motorAngleScopeConfig.txt","w+")
        f.write("J1 "+j1left+" ")
        f.write(j1right+"\n")
        f.write("J2 "+j2left+" ")
        f.write(j2right+"\n")
        f.write("J3 "+j3left+" ")
        f.write(j3right+"\n")
        f.write("J4 "+j4left+" ")
        f.write(j4right+"\n")
        f.write("J5 "+j5left+" ")
        f.write(j5right+"\n")
        f.write("J6 "+j6left+" ")
        f.write(j6right+"\n")
        f.close()
        self.pushButton_21.setText("成功")

       



