# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'snapshot.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Snapshot(object):
	def setupUi(self, Snapshot):
		Snapshot.setObjectName("Snapshot")
		Snapshot.resize(330, 183)
		self.pushButton = QtWidgets.QPushButton(Snapshot)
		self.pushButton.setGeometry(QtCore.QRect(40, 130, 99, 27))
		self.pushButton.setObjectName("pushButton")
		self.pushButton_2 = QtWidgets.QPushButton(Snapshot)
		self.pushButton_2.setGeometry(QtCore.QRect(190, 130, 99, 27))
		self.pushButton_2.setObjectName("pushButton_2")
		self.pushButton_3 = QtWidgets.QPushButton(Snapshot)
		self.pushButton_3.setGeometry(QtCore.QRect(200, 70, 51, 27))
		self.pushButton_3.setObjectName("pushButton_3")
		self.pushButton_4 = QtWidgets.QPushButton(Snapshot)
		self.pushButton_4.setGeometry(QtCore.QRect(200, 30, 51, 27))
		self.pushButton_4.setObjectName("pushButton_4")
		self.label = QtWidgets.QLabel(Snapshot)
		self.label.setGeometry(QtCore.QRect(110, 30, 71, 31))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(Snapshot)
		self.label_2.setGeometry(QtCore.QRect(110, 70, 71, 31))
		self.label_2.setObjectName("label_2")
		self.checkBox = QtWidgets.QCheckBox(Snapshot)
		self.checkBox.setGeometry(QtCore.QRect(60, 40, 21, 22))
		self.checkBox.setText("")
		self.checkBox.setChecked(True)
		self.checkBox.setObjectName("checkBox")
		self.checkBox_2 = QtWidgets.QCheckBox(Snapshot)
		self.checkBox_2.setGeometry(QtCore.QRect(60, 70, 21, 22))
		self.checkBox_2.setText("")
		self.checkBox_2.setObjectName("checkBox_2")

		self.retranslateUi(Snapshot)
		QtCore.QMetaObject.connectSlotsByName(Snapshot)

	def retranslateUi(self, Snapshot):
		_translate = QtCore.QCoreApplication.translate
		Snapshot.setWindowTitle(_translate("Snapshot", "快照"))
		self.pushButton.setText(_translate("Snapshot", "确定"))
		self.pushButton_2.setText(_translate("Snapshot", "取消"))
		self.pushButton_3.setText(_translate("Snapshot", "清空"))
		self.pushButton_4.setText(_translate("Snapshot", "重置"))
		self.label.setText(_translate("Snapshot", "关机位置"))
		self.label_2.setText(_translate("Snapshot", "标定位置"))

