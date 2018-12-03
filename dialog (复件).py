# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from tcpconfig import *   
from snapshot import *   

class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(1046, 583)
		self.groupBox = QtWidgets.QGroupBox(Dialog)
		self.groupBox.setGeometry(QtCore.QRect(10, 60, 481, 121))
		self.groupBox.setStyleSheet("QGroupBox{\n"
		"    border-width:2px;\n"
		"    border-style:solid;\n"
		"    border-color:#c5c5c5;\n"
		"    margin-top:0.5ex;\n"
		"\n"
		"}\n"
		"QGroupBox::title{\n"
		"    subcontrol-origin:margin;\n"
		"    subcontrol-position:top left;\n"
		"    left:10px;\n"
		"    margin-left:0px;\n"
		"    padding:0 1px;\n"
		"}\n"
		"")
		self.groupBox.setObjectName("groupBox")
		self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_10.setGeometry(QtCore.QRect(90, 20, 41, 27))
		self.pushButton_10.setObjectName("pushButton_10")
		self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_8.setGeometry(QtCore.QRect(20, 20, 41, 27))
		self.pushButton_8.setObjectName("pushButton_8")
		self.label = QtWidgets.QLabel(self.groupBox)
		self.label.setGeometry(QtCore.QRect(70, 20, 16, 21))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.groupBox)
		self.label_2.setGeometry(QtCore.QRect(226, 20, 20, 21))
		self.label_2.setObjectName("label_2")
		self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_11.setGeometry(QtCore.QRect(250, 20, 41, 27))
		self.pushButton_11.setObjectName("pushButton_11")
		self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_9.setGeometry(QtCore.QRect(180, 20, 41, 27))
		self.pushButton_9.setObjectName("pushButton_9")
		self.label_3 = QtWidgets.QLabel(self.groupBox)
		self.label_3.setGeometry(QtCore.QRect(390, 20, 16, 21))
		self.label_3.setObjectName("label_3")
		self.pushButton_12 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_12.setGeometry(QtCore.QRect(410, 20, 41, 27))
		self.pushButton_12.setObjectName("pushButton_12")
		self.pushButton_13 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_13.setGeometry(QtCore.QRect(340, 20, 41, 27))
		self.pushButton_13.setObjectName("pushButton_13")
		self.label_4 = QtWidgets.QLabel(self.groupBox)
		self.label_4.setGeometry(QtCore.QRect(70, 80, 16, 21))
		self.label_4.setObjectName("label_4")
		self.pushButton_14 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_14.setGeometry(QtCore.QRect(90, 80, 41, 27))
		self.pushButton_14.setObjectName("pushButton_14")
		self.pushButton_15 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_15.setGeometry(QtCore.QRect(20, 80, 41, 27))
		self.pushButton_15.setObjectName("pushButton_15")
		self.label_5 = QtWidgets.QLabel(self.groupBox)
		self.label_5.setGeometry(QtCore.QRect(230, 80, 16, 21))
		self.label_5.setObjectName("label_5")
		self.pushButton_16 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_16.setGeometry(QtCore.QRect(250, 80, 41, 27))
		self.pushButton_16.setObjectName("pushButton_16")
		self.pushButton_17 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_17.setGeometry(QtCore.QRect(180, 80, 41, 27))
		self.pushButton_17.setObjectName("pushButton_17")
		self.label_6 = QtWidgets.QLabel(self.groupBox)
		self.label_6.setGeometry(QtCore.QRect(390, 80, 16, 21))
		self.label_6.setObjectName("label_6")
		self.pushButton_18 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_18.setGeometry(QtCore.QRect(410, 80, 41, 27))
		self.pushButton_18.setObjectName("pushButton_18")
		self.pushButton_19 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_19.setGeometry(QtCore.QRect(340, 80, 41, 27))
		self.pushButton_19.setObjectName("pushButton_19")
		self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
		self.groupBox_2.setGeometry(QtCore.QRect(530, 390, 511, 171))
		self.groupBox_2.setStyleSheet("QGroupBox{\n"
		"    border-width:2px;\n"
		"    border-style:solid;\n"
		"    border-color:#c5c5c5;\n"
		"    margin-top:0.5ex;\n"
		"\n"
		"}\n"
		"QGroupBox::title{\n"
		"    subcontrol-origin:margin;\n"
		"    subcontrol-position:top left;\n"
		"    left:10px;\n"
		"    margin-left:0px;\n"
		"    padding:0 1px;\n"
		"}\n"
		"")
		self.groupBox_2.setObjectName("groupBox_2")
		self.label_25 = QtWidgets.QLabel(self.groupBox_2)
		self.label_25.setGeometry(QtCore.QRect(15, 30, 21, 21))
		self.label_25.setObjectName("label_25")
		self.label_26 = QtWidgets.QLabel(self.groupBox_2)
		self.label_26.setGeometry(QtCore.QRect(50, 30, 16, 21))
		self.label_26.setObjectName("label_26")
		self.label_29 = QtWidgets.QLabel(self.groupBox_2)
		self.label_29.setGeometry(QtCore.QRect(95, 30, 21, 21))
		self.label_29.setObjectName("label_29")
		self.label_30 = QtWidgets.QLabel(self.groupBox_2)
		self.label_30.setGeometry(QtCore.QRect(130, 30, 16, 21))
		self.label_30.setObjectName("label_30")
		self.label_31 = QtWidgets.QLabel(self.groupBox_2)
		self.label_31.setGeometry(QtCore.QRect(180, 30, 21, 21))
		self.label_31.setObjectName("label_31")
		self.label_32 = QtWidgets.QLabel(self.groupBox_2)
		self.label_32.setGeometry(QtCore.QRect(215, 30, 16, 21))
		self.label_32.setObjectName("label_32")
		self.label_33 = QtWidgets.QLabel(self.groupBox_2)
		self.label_33.setGeometry(QtCore.QRect(295, 30, 21, 21))
		self.label_33.setObjectName("label_33")
		self.label_34 = QtWidgets.QLabel(self.groupBox_2)
		self.label_34.setGeometry(QtCore.QRect(330, 30, 16, 21))
		self.label_34.setObjectName("label_34")
		self.label_35 = QtWidgets.QLabel(self.groupBox_2)
		self.label_35.setGeometry(QtCore.QRect(375, 30, 21, 21))
		self.label_35.setObjectName("label_35")
		self.label_36 = QtWidgets.QLabel(self.groupBox_2)
		self.label_36.setGeometry(QtCore.QRect(410, 30, 16, 21))
		self.label_36.setObjectName("label_36")
		self.label_37 = QtWidgets.QLabel(self.groupBox_2)
		self.label_37.setGeometry(QtCore.QRect(445, 30, 21, 21))
		self.label_37.setObjectName("label_37")
		self.label_38 = QtWidgets.QLabel(self.groupBox_2)
		self.label_38.setGeometry(QtCore.QRect(480, 30, 16, 21))
		self.label_38.setObjectName("label_38")
		self.label_39 = QtWidgets.QLabel(self.groupBox_2)
		self.label_39.setGeometry(QtCore.QRect(100, 90, 21, 21))
		self.label_39.setObjectName("label_39")
		self.label_40 = QtWidgets.QLabel(self.groupBox_2)
		self.label_40.setGeometry(QtCore.QRect(20, 90, 21, 21))
		self.label_40.setObjectName("label_40")
		self.label_41 = QtWidgets.QLabel(self.groupBox_2)
		self.label_41.setGeometry(QtCore.QRect(415, 90, 16, 21))
		self.label_41.setObjectName("label_41")
		self.label_42 = QtWidgets.QLabel(self.groupBox_2)
		self.label_42.setGeometry(QtCore.QRect(380, 90, 21, 21))
		self.label_42.setObjectName("label_42")
		self.label_43 = QtWidgets.QLabel(self.groupBox_2)
		self.label_43.setGeometry(QtCore.QRect(135, 90, 16, 21))
		self.label_43.setObjectName("label_43")
		self.label_44 = QtWidgets.QLabel(self.groupBox_2)
		self.label_44.setGeometry(QtCore.QRect(485, 90, 16, 21))
		self.label_44.setObjectName("label_44")
		self.label_45 = QtWidgets.QLabel(self.groupBox_2)
		self.label_45.setGeometry(QtCore.QRect(300, 90, 21, 21))
		self.label_45.setObjectName("label_45")
		self.label_46 = QtWidgets.QLabel(self.groupBox_2)
		self.label_46.setGeometry(QtCore.QRect(450, 90, 21, 21))
		self.label_46.setObjectName("label_46")
		self.label_47 = QtWidgets.QLabel(self.groupBox_2)
		self.label_47.setGeometry(QtCore.QRect(185, 90, 21, 21))
		self.label_47.setObjectName("label_47")
		self.label_48 = QtWidgets.QLabel(self.groupBox_2)
		self.label_48.setGeometry(QtCore.QRect(335, 90, 16, 21))
		self.label_48.setObjectName("label_48")
		self.label_49 = QtWidgets.QLabel(self.groupBox_2)
		self.label_49.setGeometry(QtCore.QRect(55, 90, 16, 21))
		self.label_49.setObjectName("label_49")
		self.label_50 = QtWidgets.QLabel(self.groupBox_2)
		self.label_50.setGeometry(QtCore.QRect(220, 90, 16, 21))
		self.label_50.setObjectName("label_50")
		self.pushButton_25 = QtWidgets.QPushButton(self.groupBox_2)
		self.pushButton_25.setGeometry(QtCore.QRect(420, 130, 71, 27))
		self.pushButton_25.setObjectName("pushButton_25")
		self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
		self.groupBox_4.setGeometry(QtCore.QRect(10, 210, 481, 101))
		self.groupBox_4.setStyleSheet("QGroupBox{\n"
		"    border-width:2px;\n"
		"    border-style:solid;\n"
		"    border-color:#c5c5c5;\n"
		"    margin-top:0.5ex;\n"
		"\n"
		"}\n"
		"QGroupBox::title{\n"
		"    subcontrol-origin:margin;\n"
		"    subcontrol-position:top left;\n"
		"    left:10px;\n"
		"    margin-left:0px;\n"
		"    padding:0 1px;\n"
		"}\n"
		"")
		self.groupBox_4.setObjectName("groupBox_4")
		self.label_7 = QtWidgets.QLabel(self.groupBox_4)
		self.label_7.setGeometry(QtCore.QRect(40, 20, 16, 21))
		self.label_7.setObjectName("label_7")
		self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
		self.lineEdit.setGeometry(QtCore.QRect(70, 20, 31, 27))
		self.lineEdit.setObjectName("lineEdit")
		self.label_8 = QtWidgets.QLabel(self.groupBox_4)
		self.label_8.setGeometry(QtCore.QRect(150, 20, 16, 21))
		self.label_8.setObjectName("label_8")
		self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_4)
		self.lineEdit_2.setGeometry(QtCore.QRect(180, 20, 31, 27))
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.label_9 = QtWidgets.QLabel(self.groupBox_4)
		self.label_9.setGeometry(QtCore.QRect(260, 20, 16, 21))
		self.label_9.setObjectName("label_9")
		self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_4)
		self.lineEdit_3.setGeometry(QtCore.QRect(290, 20, 31, 27))
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.label_10 = QtWidgets.QLabel(self.groupBox_4)
		self.label_10.setGeometry(QtCore.QRect(40, 60, 16, 21))
		self.label_10.setObjectName("label_10")
		self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
		self.lineEdit_4.setGeometry(QtCore.QRect(70, 60, 31, 27))
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.label_11 = QtWidgets.QLabel(self.groupBox_4)
		self.label_11.setGeometry(QtCore.QRect(150, 60, 16, 21))
		self.label_11.setObjectName("label_11")
		self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
		self.lineEdit_5.setGeometry(QtCore.QRect(180, 60, 31, 27))
		self.lineEdit_5.setObjectName("lineEdit_5")
		self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_4)
		self.lineEdit_6.setGeometry(QtCore.QRect(290, 60, 31, 27))
		self.lineEdit_6.setObjectName("lineEdit_6")
		self.label_12 = QtWidgets.QLabel(self.groupBox_4)
		self.label_12.setGeometry(QtCore.QRect(260, 60, 16, 21))
		self.label_12.setObjectName("label_12")
		self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_4)
		self.pushButton_20.setGeometry(QtCore.QRect(380, 40, 61, 27))
		self.pushButton_20.setObjectName("pushButton_20")
		self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_4)
		self.pushButton_21.setGeometry(QtCore.QRect(380, 70, 61, 27))
		self.pushButton_21.setObjectName("pushButton_21")
		self.label_27 = QtWidgets.QLabel(self.groupBox_4)
		self.label_27.setGeometry(QtCore.QRect(360, 10, 41, 21))
		self.label_27.setObjectName("label_27")
		self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_4)
		self.lineEdit_19.setGeometry(QtCore.QRect(410, 10, 31, 21))
		self.lineEdit_19.setObjectName("lineEdit_19")
		self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
		self.groupBox_3.setGeometry(QtCore.QRect(10, 340, 481, 221))
		self.groupBox_3.setStyleSheet("QGroupBox{\n"
		"    border-width:2px;\n"
		"    border-style:solid;\n"
		"    border-color:#c5c5c5;\n"
		"    margin-top:0.5ex;\n"
		"\n"
		"}\n"
		"QGroupBox::title{\n"
		"    subcontrol-origin:margin;\n"
		"    subcontrol-position:top left;\n"
		"    left:10px;\n"
		"    margin-left:0px;\n"
		"    padding:0 1px;\n"
		"}\n"
		"")
		self.groupBox_3.setObjectName("groupBox_3")
		self.label_18 = QtWidgets.QLabel(self.groupBox_3)
		self.label_18.setGeometry(QtCore.QRect(260, 30, 16, 21))
		self.label_18.setObjectName("label_18")
		self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_3)
		self.lineEdit_8.setGeometry(QtCore.QRect(290, 30, 31, 27))
		self.lineEdit_8.setObjectName("lineEdit_8")
		self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_3)
		self.lineEdit_9.setGeometry(QtCore.QRect(180, 30, 31, 27))
		self.lineEdit_9.setObjectName("lineEdit_9")
		self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_3)
		self.lineEdit_11.setGeometry(QtCore.QRect(290, 70, 31, 27))
		self.lineEdit_11.setObjectName("lineEdit_11")
		self.pushButton_23 = QtWidgets.QPushButton(self.groupBox_3)
		self.pushButton_23.setGeometry(QtCore.QRect(380, 70, 61, 27))
		self.pushButton_23.setObjectName("pushButton_23")
		self.label_16 = QtWidgets.QLabel(self.groupBox_3)
		self.label_16.setGeometry(QtCore.QRect(40, 30, 16, 21))
		self.label_16.setObjectName("label_16")
		self.label_17 = QtWidgets.QLabel(self.groupBox_3)
		self.label_17.setGeometry(QtCore.QRect(40, 70, 16, 21))
		self.label_17.setObjectName("label_17")
		self.label_13 = QtWidgets.QLabel(self.groupBox_3)
		self.label_13.setGeometry(QtCore.QRect(260, 70, 16, 21))
		self.label_13.setObjectName("label_13")
		self.label_15 = QtWidgets.QLabel(self.groupBox_3)
		self.label_15.setGeometry(QtCore.QRect(150, 70, 16, 21))
		self.label_15.setObjectName("label_15")
		self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_3)
		self.lineEdit_12.setGeometry(QtCore.QRect(70, 70, 31, 27))
		self.lineEdit_12.setObjectName("lineEdit_12")
		self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_3)
		self.pushButton_22.setGeometry(QtCore.QRect(380, 30, 61, 27))
		self.pushButton_22.setObjectName("pushButton_22")
		self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_3)
		self.lineEdit_10.setGeometry(QtCore.QRect(70, 30, 31, 27))
		self.lineEdit_10.setObjectName("lineEdit_10")
		self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_3)
		self.lineEdit_7.setGeometry(QtCore.QRect(180, 70, 31, 27))
		self.lineEdit_7.setObjectName("lineEdit_7")
		self.label_14 = QtWidgets.QLabel(self.groupBox_3)
		self.label_14.setGeometry(QtCore.QRect(150, 30, 16, 21))
		self.label_14.setObjectName("label_14")
		self.label_24 = QtWidgets.QLabel(self.groupBox_3)
		self.label_24.setGeometry(QtCore.QRect(40, 180, 16, 21))
		self.label_24.setObjectName("label_24")
		self.label_19 = QtWidgets.QLabel(self.groupBox_3)
		self.label_19.setGeometry(QtCore.QRect(260, 180, 16, 21))
		self.label_19.setObjectName("label_19")
		self.label_20 = QtWidgets.QLabel(self.groupBox_3)
		self.label_20.setGeometry(QtCore.QRect(150, 140, 16, 21))
		self.label_20.setObjectName("label_20")
		self.label_21 = QtWidgets.QLabel(self.groupBox_3)
		self.label_21.setGeometry(QtCore.QRect(150, 180, 16, 21))
		self.label_21.setObjectName("label_21")
		self.label_23 = QtWidgets.QLabel(self.groupBox_3)
		self.label_23.setGeometry(QtCore.QRect(260, 140, 16, 21))
		self.label_23.setObjectName("label_23")
		self.label_22 = QtWidgets.QLabel(self.groupBox_3)
		self.label_22.setGeometry(QtCore.QRect(40, 140, 16, 21))
		self.label_22.setObjectName("label_22")
		self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_3)
		self.lineEdit_14.setGeometry(QtCore.QRect(290, 140, 31, 27))
		self.lineEdit_14.setObjectName("lineEdit_14")
		self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_3)
		self.lineEdit_18.setGeometry(QtCore.QRect(70, 180, 31, 27))
		self.lineEdit_18.setObjectName("lineEdit_18")
		self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_3)
		self.lineEdit_16.setGeometry(QtCore.QRect(70, 140, 31, 27))
		self.lineEdit_16.setObjectName("lineEdit_16")
		self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_3)
		self.lineEdit_15.setGeometry(QtCore.QRect(180, 140, 31, 27))
		self.lineEdit_15.setObjectName("lineEdit_15")
		self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_3)
		self.lineEdit_17.setGeometry(QtCore.QRect(290, 180, 31, 27))
		self.lineEdit_17.setObjectName("lineEdit_17")
		self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_3)
		self.lineEdit_13.setGeometry(QtCore.QRect(180, 180, 31, 27))
		self.lineEdit_13.setObjectName("lineEdit_13")
		self.pushButton_24 = QtWidgets.QPushButton(self.groupBox_3)
		self.pushButton_24.setGeometry(QtCore.QRect(380, 160, 61, 27))
		self.pushButton_24.setObjectName("pushButton_24")
		self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
		self.groupBox_5.setGeometry(QtCore.QRect(530, 40, 511, 331))
		self.groupBox_5.setStyleSheet("QGroupBox{\n"
		"    border-width:2px;\n"
		"    border-style:solid;\n"
		"    border-color:#c5c5c5;\n"
		"    margin-top:0.5ex;\n"
		"\n"
		"}\n"
		"QGroupBox::title{\n"
		"    subcontrol-origin:margin;\n"
		"    subcontrol-position:top left;\n"
		"    left:10px;\n"
		"    margin-left:0px;\n"
		"    padding:0 1px;\n"
		"}\n"
		"")
		self.groupBox_5.setObjectName("groupBox_5")
		self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 481, 51))
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.pushButton_2.setObjectName("pushButton_2")
		self.horizontalLayout.addWidget(self.pushButton_2)
		self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.pushButton_3.setObjectName("pushButton_3")
		self.horizontalLayout.addWidget(self.pushButton_3)
		self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayout.addWidget(self.pushButton)
		self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
		self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(530, 0, 511, 41))
		self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
		self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.label_51 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
		self.label_51.setObjectName("label_51")
		self.horizontalLayout_2.addWidget(self.label_51)
		self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
		self.comboBox.setObjectName("comboBox")
		self.horizontalLayout_2.addWidget(self.comboBox)
		self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
		self.pushButton_4.setObjectName("pushButton_4")
		self.horizontalLayout_2.addWidget(self.pushButton_4)

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "示教"))
		self.groupBox.setTitle(_translate("Dialog", "手动"))
		self.pushButton_10.setText(_translate("Dialog", ">"))
		self.pushButton_8.setText(_translate("Dialog", "<"))
		self.label.setText(_translate("Dialog", "J1"))
		self.label_2.setText(_translate("Dialog", "J2"))
		self.pushButton_11.setText(_translate("Dialog", ">"))
		self.pushButton_9.setText(_translate("Dialog", "<"))
		self.label_3.setText(_translate("Dialog", "J3"))
		self.pushButton_12.setText(_translate("Dialog", ">"))
		self.pushButton_13.setText(_translate("Dialog", "<"))
		self.label_4.setText(_translate("Dialog", "J4"))
		self.pushButton_14.setText(_translate("Dialog", ">"))
		self.pushButton_15.setText(_translate("Dialog", "<"))
		self.label_5.setText(_translate("Dialog", "J5"))
		self.pushButton_16.setText(_translate("Dialog", ">"))
		self.pushButton_17.setText(_translate("Dialog", "<"))
		self.label_6.setText(_translate("Dialog", "J6"))
		self.pushButton_18.setText(_translate("Dialog", ">"))
		self.pushButton_19.setText(_translate("Dialog", "<"))
		self.groupBox_2.setTitle(_translate("Dialog", "状态"))
		self.label_25.setText(_translate("Dialog", "J1:"))
		self.label_26.setText(_translate("Dialog", "0"))
		self.label_29.setText(_translate("Dialog", "J2:"))
		self.label_30.setText(_translate("Dialog", "0"))
		self.label_31.setText(_translate("Dialog", "J3:"))
		self.label_32.setText(_translate("Dialog", "0"))
		self.label_33.setText(_translate("Dialog", "J4:"))
		self.label_34.setText(_translate("Dialog", "0"))
		self.label_35.setText(_translate("Dialog", "J5:"))
		self.label_36.setText(_translate("Dialog", "0"))
		self.label_37.setText(_translate("Dialog", "J6:"))
		self.label_38.setText(_translate("Dialog", "0"))
		self.label_39.setText(_translate("Dialog", "Y:"))
		self.label_40.setText(_translate("Dialog", "X:"))
		self.label_41.setText(_translate("Dialog", "0"))
		self.label_42.setText(_translate("Dialog", "j:"))
		self.label_43.setText(_translate("Dialog", "0"))
		self.label_44.setText(_translate("Dialog", "0"))
		self.label_45.setText(_translate("Dialog", "i:"))
		self.label_46.setText(_translate("Dialog", "k:"))
		self.label_47.setText(_translate("Dialog", "Z:"))
		self.label_48.setText(_translate("Dialog", "0"))
		self.label_49.setText(_translate("Dialog", "0"))
		self.label_50.setText(_translate("Dialog", "0"))
		self.pushButton_25.setText(_translate("Dialog", "快照"))
		self.pushButton_25.clicked.connect(self.pushButton_25ClickedFunc)
		self.groupBox_4.setTitle(_translate("Dialog", "点动"))
		self.label_7.setText(_translate("Dialog", "J1"))
		self.label_8.setText(_translate("Dialog", "J2"))
		self.label_9.setText(_translate("Dialog", "J3"))
		self.label_10.setText(_translate("Dialog", "J4"))
		self.label_11.setText(_translate("Dialog", "J5"))
		self.label_12.setText(_translate("Dialog", "J6"))
		self.pushButton_20.setText(_translate("Dialog", "执行"))
		self.pushButton_21.setText(_translate("Dialog", "重置"))
		self.label_27.setText(_translate("Dialog", "步长:"))
		self.groupBox_3.setTitle(_translate("Dialog", "逆解"))
		self.label_18.setText(_translate("Dialog", "Z"))
		self.pushButton_23.setText(_translate("Dialog", "执行"))
		self.label_16.setText(_translate("Dialog", "X"))
		self.label_17.setText(_translate("Dialog", "i"))
		self.label_13.setText(_translate("Dialog", "k"))
		self.label_15.setText(_translate("Dialog", "j"))
		self.pushButton_22.setText(_translate("Dialog", "求解"))
		self.label_14.setText(_translate("Dialog", "Y"))
		self.label_24.setText(_translate("Dialog", "J4"))
		self.label_19.setText(_translate("Dialog", "J6"))
		self.label_20.setText(_translate("Dialog", "J2"))
		self.label_21.setText(_translate("Dialog", "J5"))
		self.label_23.setText(_translate("Dialog", "J3"))
		self.label_22.setText(_translate("Dialog", "J1"))
		self.pushButton_24.setText(_translate("Dialog", "重置"))
		self.groupBox_5.setTitle(_translate("Dialog", "三维模拟区"))
		self.pushButton_2.setText(_translate("Dialog", "关机复位"))
		self.pushButton_3.setText(_translate("Dialog", "归零复位"))
		self.pushButton.setText(_translate("Dialog", "TCP配置"))
		self.pushButton.clicked.connect(self.pushButtonClickedFunc)
		self.label_51.setText(_translate("Dialog", "                                Port:"))
		self.pushButton_4.setText(_translate("Dialog", "Open"))

	def pushButtonClickedFunc(self):
		print("call Ui_Dialog.pushButtonClickedFunc")
		#self.form.hide()            #如果没有self.form.show()这一句，关闭Demo1界面后就会关闭程序
		form1 = QtWidgets.QDialog()
		ui = Ui_TcpConfig()
		ui.setupUi(form1)
		form1.show()
		form1.exec_()
		#self.form.show()


		return

	def pushButton_25ClickedFunc(self):
		print("call Ui_Dialog.pushButtonClickedFunc")
		#self.form.hide()            #如果没有self.form.show()这一句，关闭Demo1界面后就会关闭程序
		form1 = QtWidgets.QDialog()
		ui = Ui_Snapshot()
		ui.setupUi(form1)
		form1.show()
		form1.exec_()
		#self.form.show()


		return

