# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tcpconfig.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TcpConfig(object):
	def setupUi(self, TcpConfig):
		TcpConfig.setObjectName("TcpConfig")
		TcpConfig.resize(400, 257)
		self.lineEdit = QtWidgets.QLineEdit(TcpConfig)
		self.lineEdit.setGeometry(QtCore.QRect(50, 20, 41, 27))
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit_2 = QtWidgets.QLineEdit(TcpConfig)
		self.lineEdit_2.setGeometry(QtCore.QRect(170, 20, 41, 27))
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_3 = QtWidgets.QLineEdit(TcpConfig)
		self.lineEdit_3.setGeometry(QtCore.QRect(110, 20, 41, 27))
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.lineEdit_4 = QtWidgets.QLineEdit(TcpConfig)
		self.lineEdit_4.setGeometry(QtCore.QRect(330, 120, 41, 27))
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.lineEdit_5 = QtWidgets.QLineEdit(TcpConfig)
		self.lineEdit_5.setGeometry(QtCore.QRect(330, 70, 41, 27))
		self.lineEdit_5.setObjectName("lineEdit_5")
		self.lineEdit_6 = QtWidgets.QLineEdit(TcpConfig)
		self.lineEdit_6.setGeometry(QtCore.QRect(330, 20, 41, 27))
		self.lineEdit_6.setObjectName("lineEdit_6")
		self.label = QtWidgets.QLabel(TcpConfig)
		self.label.setGeometry(QtCore.QRect(10, 20, 16, 17))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(TcpConfig)
		self.label_2.setGeometry(QtCore.QRect(290, 20, 16, 17))
		self.label_2.setObjectName("label_2")
		self.pushButton = QtWidgets.QPushButton(TcpConfig)
		self.pushButton.setGeometry(QtCore.QRect(20, 210, 81, 27))
		self.pushButton.setObjectName("pushButton")
		self.lineEdit_14 = QtWidgets.QLineEdit(TcpConfig)
		self.lineEdit_14.setGeometry(QtCore.QRect(170, 70, 41, 27))
		self.lineEdit_14.setObjectName("lineEdit_14")
		self.lineEdit_15 = QtWidgets.QLineEdit(TcpConfig)
		self.lineEdit_15.setGeometry(QtCore.QRect(110, 70, 41, 27))
		self.lineEdit_15.setObjectName("lineEdit_15")
		self.lineEdit_16 = QtWidgets.QLineEdit(TcpConfig)
		self.lineEdit_16.setGeometry(QtCore.QRect(50, 70, 41, 27))
		self.lineEdit_16.setObjectName("lineEdit_16")
		self.lineEdit_17 = QtWidgets.QLineEdit(TcpConfig)
		self.lineEdit_17.setGeometry(QtCore.QRect(170, 120, 41, 27))
		self.lineEdit_17.setObjectName("lineEdit_17")
		self.lineEdit_18 = QtWidgets.QLineEdit(TcpConfig)
		self.lineEdit_18.setGeometry(QtCore.QRect(110, 120, 41, 27))
		self.lineEdit_18.setObjectName("lineEdit_18")
		self.lineEdit_19 = QtWidgets.QLineEdit(TcpConfig)
		self.lineEdit_19.setGeometry(QtCore.QRect(50, 120, 41, 27))
		self.lineEdit_19.setObjectName("lineEdit_19")
		self.pushButton_4 = QtWidgets.QPushButton(TcpConfig)
		self.pushButton_4.setGeometry(QtCore.QRect(160, 210, 81, 27))
		self.pushButton_4.setObjectName("pushButton_4")
		self.pushButton_2 = QtWidgets.QPushButton(TcpConfig)
		self.pushButton_2.setGeometry(QtCore.QRect(290, 210, 81, 27))
		self.pushButton_2.setObjectName("pushButton_2")

		self.retranslateUi(TcpConfig)
		QtCore.QMetaObject.connectSlotsByName(TcpConfig)

	def retranslateUi(self, TcpConfig):
		_translate = QtCore.QCoreApplication.translate
		TcpConfig.setWindowTitle(_translate("TcpConfig", "TCP配置"))
		self.label.setText(_translate("TcpConfig", "R"))
		self.label_2.setText(_translate("TcpConfig", "T"))
		self.pushButton.setText(_translate("TcpConfig", "重置"))
		self.pushButton_4.setText(_translate("TcpConfig", "保存"))
		self.pushButton_2.setText(_translate("TcpConfig", "取消"))

