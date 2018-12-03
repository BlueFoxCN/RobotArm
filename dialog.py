# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from tcpconfig import *   
from snapshot import *
from parameterconfigutation import *  
import serial
import serial.tools.list_ports
import threading
import time
import random
from PyQt5.QtCore import pyqtSignal,Qt
from PyQt5.QtWidgets import (QApplication, QWidget,QToolTip,QPushButton,QMessageBox,QDesktopWidget,QMainWindow,
                             QVBoxLayout,QHBoxLayout,QGridLayout,QTextEdit,QLabel,QRadioButton,QCheckBox,
                             QLineEdit,QGroupBox,QSplitter)
import numpy as np
from robot_kinematics import *
import sys 
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QListView,QMessageBox 
from PyQt5.QtCore import QStringListModel 
from PyQt5 import QtCore, QtGui, QtWidgets

#import pdb

#class Ui_Dialog(object):QMainWindow
global J1
J1 = ""
global J2
J2 = ""
global J3
J3 = ""
global J4
J4 = ""
global J5
J5 = ""
global J6
J6 = ""
class Ui_Dialog(QMainWindow,QWidget):
	isDetectSerialPort = False
	LoopCounter = 0
	receiveCounter = 0
	step = 0.1
	zeroingOperationFlag = 0
	# J1 = ""
	# J2 = ""
	# J3 = ""
	# J4 = ""
	# J5 = ""
	# J6 = ""
	X = 0
	Y = 0
	Z = 0
	i = 0
	j = 0
	k = 0
	recvData = bytes([0x00,0x00,0x00])
	recvDataFlag = 0
	receiveUpdateSignal = pyqtSignal(str)
	G07GCMFlag = 0

	def setupUi(self, Dialog):
		self.stopFlag = 0
		#super().__init__()
		Dialog.setObjectName("Dialog")
		Dialog.resize(1446, 983-400)
		
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
		self.pushButton_10.setGeometry(QtCore.QRect(90-20+6, 20, 41, 27))
		self.pushButton_10.setObjectName("pushButton_10")
		self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_8.setGeometry(QtCore.QRect(20-20+6, 20, 41, 27))
		self.pushButton_8.setObjectName("pushButton_8")
		self.label = QtWidgets.QLabel(self.groupBox)
		self.label.setGeometry(QtCore.QRect(70-20+6, 20, 16, 21))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.groupBox)
		self.label_2.setGeometry(QtCore.QRect(226-20-20, 20, 20, 21))
		self.label_2.setObjectName("label_2")
		self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_11.setGeometry(QtCore.QRect(250-20-20, 20, 41, 27))
		self.pushButton_11.setObjectName("pushButton_11")
		self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_9.setGeometry(QtCore.QRect(180-20-20, 20, 41, 27))
		self.pushButton_9.setObjectName("pushButton_9")
		self.label_3 = QtWidgets.QLabel(self.groupBox)
		self.label_3.setGeometry(QtCore.QRect(390-20-20-20-5, 20, 16, 21))
		self.label_3.setObjectName("label_3")
		self.pushButton_12 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_12.setGeometry(QtCore.QRect(410-20-20-20-5, 20, 41, 27))
		self.pushButton_12.setObjectName("pushButton_12")
		self.pushButton_c = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_c.setGeometry(QtCore.QRect(410, 20, 61, 27))
		self.pushButton_c.setObjectName("pushButton_c")
		self.pushButton_c.setText("关节输出")
		self.pushButton_c.clicked.connect(self.pushButton_cClickedFunc)
		self.pushButton_13 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_13.setGeometry(QtCore.QRect(340-20-20-20-5, 20, 41, 27))
		self.pushButton_13.setObjectName("pushButton_13")
		self.label_4 = QtWidgets.QLabel(self.groupBox)
		self.label_4.setGeometry(QtCore.QRect(70-20+6, 80, 16, 21))
		self.label_4.setObjectName("label_4")
		self.pushButton_14 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_14.setGeometry(QtCore.QRect(90-20+6, 80, 41, 27))
		self.pushButton_14.setObjectName("pushButton_14")
		self.pushButton_15 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_15.setGeometry(QtCore.QRect(20-20+6, 80, 41, 27))
		self.pushButton_15.setObjectName("pushButton_15")
		self.label_5 = QtWidgets.QLabel(self.groupBox)
		self.label_5.setGeometry(QtCore.QRect(230-20-20, 80, 16, 21))
		self.label_5.setObjectName("label_5")
		self.pushButton_16 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_16.setGeometry(QtCore.QRect(250-20-20, 80, 41, 27))
		self.pushButton_16.setObjectName("pushButton_16")
		self.pushButton_17 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_17.setGeometry(QtCore.QRect(180-20-20, 80, 41, 27))
		self.pushButton_17.setObjectName("pushButton_17")
		self.label_6 = QtWidgets.QLabel(self.groupBox)
		self.label_6.setGeometry(QtCore.QRect(390-20-20-20-5, 80, 16, 21))
		self.label_6.setObjectName("label_6")
		self.pushButton_18 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_18.setGeometry(QtCore.QRect(410-20-20-20-5, 80, 41, 27))
		self.pushButton_18.setObjectName("pushButton_18")
		self.pushButton_19 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_19.setGeometry(QtCore.QRect(340-20-20-20-5, 80, 41, 27))
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
		self.label_26.setGeometry(QtCore.QRect(50, 30, 16+15, 21))
		self.label_26.setObjectName("label_26")
		self.label_29 = QtWidgets.QLabel(self.groupBox_2)
		self.label_29.setGeometry(QtCore.QRect(95, 30, 21, 21))
		self.label_29.setObjectName("label_29")
		self.label_30 = QtWidgets.QLabel(self.groupBox_2)
		self.label_30.setGeometry(QtCore.QRect(130, 30, 16+15, 21))
		self.label_30.setObjectName("label_30")
		self.label_31 = QtWidgets.QLabel(self.groupBox_2)
		self.label_31.setGeometry(QtCore.QRect(180, 30, 21, 21))
		self.label_31.setObjectName("label_31")
		self.label_32 = QtWidgets.QLabel(self.groupBox_2)
		self.label_32.setGeometry(QtCore.QRect(215, 30, 16+15, 21))
		self.label_32.setObjectName("label_32")
		self.label_33 = QtWidgets.QLabel(self.groupBox_2)
		self.label_33.setGeometry(QtCore.QRect(295-20, 30, 21, 21))
		self.label_33.setObjectName("label_33")
		self.label_34 = QtWidgets.QLabel(self.groupBox_2)
		self.label_34.setGeometry(QtCore.QRect(330-20, 30, 16+15, 21))
		self.label_34.setObjectName("label_34")
		self.label_35 = QtWidgets.QLabel(self.groupBox_2)
		self.label_35.setGeometry(QtCore.QRect(375-20, 30, 21, 21))
		self.label_35.setObjectName("label_35")
		self.label_36 = QtWidgets.QLabel(self.groupBox_2)
		self.label_36.setGeometry(QtCore.QRect(410-20, 30, 16+15, 21))
		self.label_36.setObjectName("label_36")
		self.label_37 = QtWidgets.QLabel(self.groupBox_2)
		self.label_37.setGeometry(QtCore.QRect(445-20, 30, 21, 21))
		self.label_37.setObjectName("label_37")
		self.label_38 = QtWidgets.QLabel(self.groupBox_2)
		self.label_38.setGeometry(QtCore.QRect(480-20, 30, 16+15, 21))
		self.label_38.setObjectName("label_38")
		self.label_39 = QtWidgets.QLabel(self.groupBox_2)
		self.label_39.setGeometry(QtCore.QRect(100, 90, 21, 21))
		self.label_39.setObjectName("label_39")
		self.label_40 = QtWidgets.QLabel(self.groupBox_2)
		self.label_40.setGeometry(QtCore.QRect(20, 90, 21, 21))
		self.label_40.setObjectName("label_40")
		self.label_41 = QtWidgets.QLabel(self.groupBox_2)
		self.label_41.setGeometry(QtCore.QRect(415-20, 90, 16+15, 21))
		self.label_41.setObjectName("label_41")
		self.label_42 = QtWidgets.QLabel(self.groupBox_2)
		self.label_42.setGeometry(QtCore.QRect(380-20, 90, 21, 21))
		self.label_42.setObjectName("label_42")
		self.label_43 = QtWidgets.QLabel(self.groupBox_2)
		self.label_43.setGeometry(QtCore.QRect(135-20, 90, 16+15, 21))
		self.label_43.setObjectName("label_43")
		self.label_44 = QtWidgets.QLabel(self.groupBox_2)
		self.label_44.setGeometry(QtCore.QRect(485-20, 90, 16+15, 21))
		self.label_44.setObjectName("label_44")
		self.label_45 = QtWidgets.QLabel(self.groupBox_2)
		self.label_45.setGeometry(QtCore.QRect(300-20, 90, 21, 21))
		self.label_45.setObjectName("label_45")
		self.label_46 = QtWidgets.QLabel(self.groupBox_2)
		self.label_46.setGeometry(QtCore.QRect(450-20, 90, 21, 21))
		self.label_46.setObjectName("label_46")
		self.label_47 = QtWidgets.QLabel(self.groupBox_2)
		self.label_47.setGeometry(QtCore.QRect(185, 90, 21, 21))
		self.label_47.setObjectName("label_47")
		self.label_48 = QtWidgets.QLabel(self.groupBox_2)
		self.label_48.setGeometry(QtCore.QRect(335-20, 90, 16+15, 21))
		self.label_48.setObjectName("label_48")
		self.label_49 = QtWidgets.QLabel(self.groupBox_2)
		self.label_49.setGeometry(QtCore.QRect(55-20, 90, 16+15, 21))
		self.label_49.setObjectName("label_49")
		self.label_50 = QtWidgets.QLabel(self.groupBox_2)
		self.label_50.setGeometry(QtCore.QRect(220-20, 90, 16+15, 21))
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
		self.lineEdit.setGeometry(QtCore.QRect(70, 20, 31+20, 27))
		self.lineEdit.setObjectName("lineEdit")
		self.label_8 = QtWidgets.QLabel(self.groupBox_4)
		self.label_8.setGeometry(QtCore.QRect(150, 20, 16, 21))
		self.label_8.setObjectName("label_8")
		self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_4)
		self.lineEdit_2.setGeometry(QtCore.QRect(180, 20, 31+20, 27))
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.label_9 = QtWidgets.QLabel(self.groupBox_4)
		self.label_9.setGeometry(QtCore.QRect(260, 20, 16, 21))
		self.label_9.setObjectName("label_9")
		self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_4)
		self.lineEdit_3.setGeometry(QtCore.QRect(290, 20, 31+20, 27))
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.label_10 = QtWidgets.QLabel(self.groupBox_4)
		self.label_10.setGeometry(QtCore.QRect(40, 60, 16, 21))
		self.label_10.setObjectName("label_10")
		self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
		self.lineEdit_4.setGeometry(QtCore.QRect(70, 60, 31+20, 27))
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.label_11 = QtWidgets.QLabel(self.groupBox_4)
		self.label_11.setGeometry(QtCore.QRect(150, 60, 16, 21))
		self.label_11.setObjectName("label_11")
		self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
		self.lineEdit_5.setGeometry(QtCore.QRect(180, 60, 31+20, 27))
		self.lineEdit_5.setObjectName("lineEdit_5")
		self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_4)
		self.lineEdit_6.setGeometry(QtCore.QRect(290, 60, 31+20, 27))
		self.lineEdit_6.setObjectName("lineEdit_6")
		self.label_12 = QtWidgets.QLabel(self.groupBox_4)
		self.label_12.setGeometry(QtCore.QRect(260, 60, 16, 21))
		self.label_12.setObjectName("label_12")		
		self.pushButton_b = QtWidgets.QPushButton(self.groupBox_4)
		self.pushButton_b.setGeometry(QtCore.QRect(380-40+5, 40-20+3, 31, 20))
		self.pushButton_b.setObjectName("pushButton_b")
		self.pushButton_b.setText("随机")
		self.pushButton_b.clicked.connect(self.pushButton_bClickedFunc)
		self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_4)
		self.pushButton_20.setGeometry(QtCore.QRect(380, 40-20, 61, 27))
		self.pushButton_20.setObjectName("pushButton_20")
		self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_4)
		self.pushButton_21.setGeometry(QtCore.QRect(380, 70-10, 61, 27))
		self.pushButton_21.setObjectName("pushButton_21")
		#self.label_27 = QtWidgets.QLabel(self.groupBox_4)
		self.label_27 = QtWidgets.QLabel(self.groupBox)
		self.label_27.setGeometry(QtCore.QRect(360+40+10, 10+10+30, 41, 21))
		self.label_27.setObjectName("label_27")

		self.pushButton_21示教 = QtWidgets.QPushButton(self.groupBox)
		self.pushButton_21示教.setGeometry(QtCore.QRect(360+40+10, 10+10+30+30, 41, 21))
		self.pushButton_21示教.setObjectName("pushButton_21示教")
		#self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_4)
		self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox)
		self.lineEdit_19.setGeometry(QtCore.QRect(410+40-20+10, 10+40, 31, 21))
		self.lineEdit_19.setObjectName("lineEdit_19")
		self.lineEdit_19.setText("0.1")
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
		self.groupBox_5.setGeometry(QtCore.QRect(530, 10, 511, 331))
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
		self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_5)
		self.textBrowser.setGeometry(QtCore.QRect(20, 40, 471, 281))
		self.textBrowser.setObjectName("textBrowser")
		self.label_28 = QtWidgets.QLabel(self.groupBox_5)
		self.label_28.setGeometry(QtCore.QRect(220, 10, 67, 17))
		self.label_28.setObjectName("label_28")
		self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 481, 51))
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)

		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.pushButton_2.setObjectName("pushButton_2")
		self.horizontalLayout.addWidget(self.pushButton_2)
		self.pushButton_a = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.pushButton_a.setObjectName("pushButton_a")
		self.horizontalLayout.addWidget(self.pushButton_a)
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
		# self.label_51 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
		# self.label_51.setObjectName("label_51")
		# self.horizontalLayout_2.addWidget(self.label_51)
		# self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
		# self.comboBox.setObjectName("comboBox")
		# self.horizontalLayout_2.addWidget(self.comboBox)
		# self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
		# self.pushButton_4.setObjectName("pushButton_4")
		# self.horizontalLayout_2.addWidget(self.pushButton_4)

		self.pushButtona1 = QtWidgets.QPushButton(Dialog)
		self.pushButtona1.setGeometry(QtCore.QRect(20+540+510, 480, 99, 27))
		self.pushButtona1.setObjectName("pushButton")
		self.pushButton_2a8 = QtWidgets.QPushButton(Dialog)
		self.pushButton_2a8.setGeometry(QtCore.QRect(20+540+510, 520, 99, 27))
		self.pushButton_2a8.setObjectName("pushButton_2")
		self.pushButton_3a4 = QtWidgets.QPushButton(Dialog)
		self.pushButton_3a4.setGeometry(QtCore.QRect(140+540+510, 480, 99, 27))
		self.pushButton_3a4.setObjectName("pushButton_3")
		self.pushButton_4a7 = QtWidgets.QPushButton(Dialog)
		self.pushButton_4a7.setGeometry(QtCore.QRect(140+540+510, 520, 99, 27))
		self.pushButton_4a7.setObjectName("pushButton_4")
		self.pushButton_5a3 = QtWidgets.QPushButton(Dialog)
		self.pushButton_5a3.setGeometry(QtCore.QRect(260+540+510, 480, 99, 27))
		self.pushButton_5a3.setObjectName("pushButton_5")
		self.pushButton_5b3 = QtWidgets.QPushButton(Dialog)
		self.pushButton_5b3.setGeometry(QtCore.QRect(260+540+510, 520, 99, 27))
		self.pushButton_5b3.setObjectName("pushButton_5")

		self.lineEdita2 = QtWidgets.QLineEdit(Dialog)
		self.lineEdita2.setGeometry(QtCore.QRect(60+540+510, 445, 113, 27))
		self.lineEdita2.setObjectName("lineEdit")
		self.label_2a5 = QtWidgets.QLabel(Dialog)
		self.label_2a5.setGeometry(QtCore.QRect(20+540+510, 450, 41, 17))
		self.label_2a5.setObjectName("label_2")


		self.labela6 = QtWidgets.QLabel(Dialog)
		self.labela6.setGeometry(QtCore.QRect(100+540+510, 10, 67, 17))
		self.labela6.setObjectName("label")
		self.listViewa9 = QtWidgets.QListView(Dialog)
		self.listViewa9.setGeometry(QtCore.QRect(40+540+510-30, 30, 350, 400))
		self.listViewa9.setObjectName("listView")
		self.listViewa9.clicked.connect(self.listViewa9ClickedFunc) #设置窗口布局，加载控件 
		# self.listViewa9.item.selected.s
		# QListView::item:selected {
  #    				border: 1px solid #6a6ea9;
 	# 				}
		self.slm=QStringListModel() 
		# self.qList=['Item 1','Item 2','Item 3','Item 4','Item 5','Item 6','Item 7','Item 8','Item 9','Item 10','Item 11','Item 12','Item 13','Item 14','Item 15','Item 16','Item 17','Item 18','Item 19','Item 20'] #设置模型列表视图，加载数据列表 
		self.qList = []
		self.qListCommand = []
		self.slm.setStringList(self.qList) #设置列表视图的模型 
		self.listViewa9.setModel(self.slm) #单击触发自定义的槽函数 
        
		self.retranslateUi(Dialog)

	def clicked(self,qModelIndex): #提示信息弹窗，你选择的信息 
		QMessageBox.information(self,'ListWidget','你选择了：'+self.qList[qModelIndex.row()]) 

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "示教"))
		self.groupBox.setTitle(_translate("Dialog", "手动"))
		self.pushButton_10.setText(_translate("Dialog", ">"))
		self.pushButton_10.clicked.connect(self.pushButton_10ClickedFunc)
		self.pushButton_10.pressed.connect(self.pushButton_10PressedFunc)
		self.pushButton_10.released.connect(self.pushButton_10ReleasedFunc)
		self.pushButton_8.setText(_translate("Dialog", "<"))
		self.pushButton_8.clicked.connect(self.pushButton_8ClickedFunc)
		self.pushButton_8.pressed.connect(self.pushButton_8PressedFunc)
		self.pushButton_8.released.connect(self.pushButton_8ReleasedFunc)
		self.label.setText(_translate("Dialog", "J1"))
		self.label_2.setText(_translate("Dialog", "J2"))
		self.pushButton_11.setText(_translate("Dialog", ">"))
		self.pushButton_11.clicked.connect(self.pushButton_11ClickedFunc)
		self.pushButton_11.pressed.connect(self.pushButton_11PressedFunc)
		self.pushButton_11.released.connect(self.pushButton_11ReleasedFunc)
		self.pushButton_9.setText(_translate("Dialog", "<"))
		self.pushButton_9.clicked.connect(self.pushButton_9ClickedFunc)
		self.pushButton_9.pressed.connect(self.pushButton_9PressedFunc)
		self.pushButton_9.released.connect(self.pushButton_9ReleasedFunc)
		self.label_3.setText(_translate("Dialog", "J3"))
		self.pushButton_12.setText(_translate("Dialog", ">"))
		self.pushButton_12.clicked.connect(self.pushButton_12ClickedFunc)
		self.pushButton_12.pressed.connect(self.pushButton_12PressedFunc)
		self.pushButton_12.released.connect(self.pushButton_12ReleasedFunc)
		self.pushButton_13.setText(_translate("Dialog", "<"))
		self.pushButton_13.clicked.connect(self.pushButton_13ClickedFunc)
		self.pushButton_13.pressed.connect(self.pushButton_13PressedFunc)
		self.pushButton_13.released.connect(self.pushButton_13ReleasedFunc)
		self.label_4.setText(_translate("Dialog", "J4"))
		self.pushButton_14.setText(_translate("Dialog", ">"))
		self.pushButton_14.clicked.connect(self.pushButton_14ClickedFunc)
		self.pushButton_14.pressed.connect(self.pushButton_14PressedFunc)
		self.pushButton_14.released.connect(self.pushButton_14ReleasedFunc)
		self.pushButton_15.setText(_translate("Dialog", "<"))
		self.pushButton_15.clicked.connect(self.pushButton_15ClickedFunc)
		self.pushButton_15.pressed.connect(self.pushButton_15PressedFunc)
		self.pushButton_15.released.connect(self.pushButton_15ReleasedFunc)
		self.label_5.setText(_translate("Dialog", "J5"))
		self.pushButton_16.setText(_translate("Dialog", ">"))
		self.pushButton_16.clicked.connect(self.pushButton_16ClickedFunc)
		self.pushButton_16.pressed.connect(self.pushButton_16PressedFunc)
		self.pushButton_16.released.connect(self.pushButton_16ReleasedFunc)
		self.pushButton_17.setText(_translate("Dialog", "<"))
		self.pushButton_17.clicked.connect(self.pushButton_17ClickedFunc)
		self.pushButton_17.pressed.connect(self.pushButton_17PressedFunc)
		self.pushButton_17.released.connect(self.pushButton_17ReleasedFunc)
		self.label_6.setText(_translate("Dialog", "J6"))
		self.pushButton_18.setText(_translate("Dialog", ">"))
		self.pushButton_18.clicked.connect(self.pushButton_18ClickedFunc)
		self.pushButton_18.pressed.connect(self.pushButton_18PressedFunc)
		self.pushButton_18.released.connect(self.pushButton_18ReleasedFunc)
		self.pushButton_19.setText(_translate("Dialog", "<"))
		self.pushButton_19.clicked.connect(self.pushButton_19ClickedFunc)
		self.pushButton_19.pressed.connect(self.pushButton_19PressedFunc)
		self.pushButton_19.released.connect(self.pushButton_19ReleasedFunc)
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
		self.pushButton_20.clicked.connect(self.pushButton_20ClickedFunc)
		self.pushButton_21.setText(_translate("Dialog", "重置"))
		self.pushButton_21.clicked.connect(self.pushButton_21ClickedFunc)
		self.label_27.setText(_translate("Dialog", "步长:"))
		self.pushButton_21示教.setText(_translate("Dialog", "示教"))
		self.pushButton_21示教.clicked.connect(self.pushButton_21shijiaoClickedFunc)
		self.groupBox_3.setTitle(_translate("Dialog", "逆解"))
		self.label_18.setText(_translate("Dialog", "Z"))
		self.pushButton_23.setText(_translate("Dialog", "执行"))
		self.pushButton_23.clicked.connect(self.pushButton_23ClickedFunc)
		self.label_16.setText(_translate("Dialog", "X"))
		self.label_17.setText(_translate("Dialog", "i"))
		self.label_13.setText(_translate("Dialog", "k"))
		self.label_15.setText(_translate("Dialog", "j"))
		self.pushButton_22.setText(_translate("Dialog", "求解"))
		self.pushButton_22.clicked.connect(self.pushButton_22ClickedFunc)
		self.label_14.setText(_translate("Dialog", "Y"))
		self.label_24.setText(_translate("Dialog", "J4"))
		self.label_19.setText(_translate("Dialog", "J6"))
		self.label_20.setText(_translate("Dialog", "J2"))
		self.label_21.setText(_translate("Dialog", "J5"))
		self.label_23.setText(_translate("Dialog", "J3"))
		self.label_22.setText(_translate("Dialog", "J1"))
		self.pushButton_24.setText(_translate("Dialog", "重置"))
		self.pushButton_24.clicked.connect(self.pushButton_24ClickedFunc)
		# self.groupBox_5.setTitle(_translate("Dialog", "三维模拟区"))
		self.groupBox_5.setTitle(_translate("Dialog", ""))
		self.pushButton_2.setText(_translate("Dialog", "关机复位"))
		self.pushButton_2.clicked.connect(self.pushButton_2ClickedFunc)
		self.pushButton_a.setText(_translate("Dialog", "参数配置"))
		self.pushButton_a.clicked.connect(self.pushButton_aClickedFunc)
		self.pushButton_3.setText(_translate("Dialog", "归零复位"))
		self.pushButton_3.clicked.connect(self.pushButton_3ClickedFunc)
		self.pushButton.setText(_translate("Dialog", "TCP配置"))
		self.pushButton.clicked.connect(self.pushButtonClickedFunc)
		# self.label_51.setText(_translate("Dialog", "                                Port:"))
		# self.pushButton_4.setText(_translate("Dialog", "Open"))
		self.label_28.setText(_translate("Dialog", "调试信息"))
		self.receiveUpdateSignal.connect(self.updateReceivedDataDisplay)
		
		self.pushButtona1.setText(_translate("Widget", "添加"))
		self.pushButtona1.clicked.connect(self.pushButtona1ClickedFunc)
		self.pushButton_5a3.setText(_translate("Widget", "执行"))
		self.pushButton_5b3.setText(_translate("Widget", "停止"))
		self.pushButton_5a3.clicked.connect(self.pushButton_5a3ClickedFunc)
		self.pushButton_5b3.clicked.connect(self.pushButton_5b3ClickedFunc)
		self.pushButton_3a4.setText(_translate("Widget", "上移"))
		self.pushButton_3a4.clicked.connect(self.pushButton_3a4ClickedFunc)
		self.label_2a5.setText(_translate("Widget", "延时:"))
		self.lineEdita2.setText(_translate("Widget", "5"))
		self.labela6.setText(_translate("Widget", "标定位置"))
		self.pushButton_4a7.setText(_translate("Widget", "下移"))
		self.pushButton_4a7.clicked.connect(self.pushButton_4a7ClickedFunc)
		self.pushButton_2a8.setText(_translate("Widget", "删除"))
		self.pushButton_2a8.clicked.connect(self.pushButton_2a8ClickedFunc)


		
		self.initTool()
		self.initList()


	def initTool(self):
		print("call Ui_Dialog.initTool")
		#self.com = serial.Serial()
		self.com = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.5)
		receiveProcess = threading.Thread(target=self.receiveData)
		receiveProcess.setDaemon(True)
		receiveProcess.start()

		return
      

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
		print("call Ui_Dialog.pushButton_25ClickedFunc")
		#self.form.hide()            #如果没有self.form.show()这一句，关闭Demo1界面后就会关闭程序
		form1 = QtWidgets.QDialog()
		ui = Ui_Snapshot()
		ui.setupUi(form1)
		form1.show()
		form1.exec_()
		#self.form.show()


		return

	def updateReceivedDataDisplay(self,str1):
		print("call Ui_Dialog.showDebug")
		if len(str1)>=2:
			#self.textBrowser.setText(self.recvData.decode())
			#self.textBrowser.append(self.recvData.decode())
			J1pos = 0
			J2pos = 0
			J3pos = 0
			J4pos = 0
			J5pos = 0
			J6pos = 0

			self.textBrowser.append(str1)
			for i in range(len(str1)):
				if (str1[i] == 'J')and(str1[i+1] == '1'):
					J1pos = i+2
				if (str1[i] == 'J')and(str1[i+1] == '2'):
					J2pos = i+2
				if (str1[i] == 'J')and(str1[i+1] == '3'):
					J3pos = i+2
				if (str1[i] == 'J')and(str1[i+1] == '4'):
					J4pos = i+2
				if (str1[i] == 'J')and(str1[i+1] == '5'):
					J5pos = i+2
				if (str1[i] == 'J')and(str1[i+1] == '6'):
					J6pos = i+2
			if (str1[0]=='G')and(str1[1]=='0')and(str1[2]=='0')or(str1[0]=='J')and(str1[1]=='1'):
				# self.J1 = str1[J1pos+1:J2pos-3]
				# self.J2 = str1[J2pos+1:J3pos-3]
				# self.J3 = str1[J3pos+1:J4pos-3]
				# self.J4 = str1[J4pos+1:J5pos-3]
				# self.J5 = str1[J5pos+1:J6pos-3]
				# self.J6 = str1[J6pos+1:]
				global J1
				global J2
				global J3
				global J4
				global J5
				global J6
				J1 = str1[J1pos+1:J2pos-3]
				J2 = str1[J2pos+1:J3pos-3]
				J3 = str1[J3pos+1:J4pos-3]
				J4 = str1[J4pos+1:J5pos-3]
				J5 = str1[J5pos+1:J6pos-3]
				J6 = str1[J6pos+1:].strip('\r').strip('\n').strip('%')
				print("str1=",str1)
				print("str1[len(str1)-1]=",str1[len(str1)-1])
				# if(str1[len(str1)-1]=='%'):
				# 	J6 = str1[J6pos+1:J6pos+1+1]
				# else:
				# 	J6 = str1[J6pos+1:]

				# self.label_26.setText(self.J1[0:5])
				# self.label_30.setText(self.J2[0:5])
				# self.label_32.setText(self.J3[0:5])
				# self.label_34.setText(self.J4[0:5])
				# self.label_36.setText(self.J5[0:5])
				# self.label_38.setText(self.J6[0:5])
				# global J1
				# global J2
				# global J3
				# global J4
				# global J5
				# global J6
				self.label_26.setText(J1[0:5])
				self.label_30.setText(J2[0:5])
				self.label_32.setText(J3[0:5])
				self.label_34.setText(J4[0:5])
				self.label_36.setText(J5[0:5])
				self.label_38.setText(J6[0:5])
				# print("self.J1=",self.J1)
				# print("self.J2=",self.J2)
				# print("self.J3=",self.J3)
				# print("self.J4=",self.J4)
				# print("self.J5=",self.J5)
				# print("self.J6=",self.J6)
				# print("self.J1=",J1)
				# print("self.J2=",J2)
				# print("self.J3=",J3)
				# print("self.J4=",J4)
				# print("self.J5=",J5)
				# print("self.J6=",J6)
				# global J1
				# global J2
				# global J3
				# global J4
				# global J5
				# global J6
				print("J1=",J1)
				print("J2=",J2)
				print("J3=",J3)
				print("J4=",J4)
				print("J5=",J5)
				print("J6=",J6)
			#phi_angle_ary = [float(self.J1),float(self.J2),float(self.J3),float(self.J4),float(self.J5),float(self.J6)]
			#pdb.set_trace()
			# if (len(self.J1)!=0)and(len(self.J2)!=0)and(len(self.J3)!=0)and(len(self.J4)!=0)and(len(self.J5)!=0)and(len(self.J6)!=0):
			# 	phi_angle_ary = [np.float64(self.J1),np.float64(self.J2),np.float64(self.J3),np.float64(self.J4),np.float64(self.J5),np.float64(self.J6)]
			# global J1
			# global J2
			# global J3
			# global J4
			# global J5
			# global J6
			if (len(J1)!=0)and(len(J2)!=0)and(len(J3)!=0)and(len(J4)!=0)and(len(J5)!=0)and(len(J6)!=0):
				phi_angle_ary = [np.float64(J1),np.float64(J2),np.float64(J3),np.float64(J4),np.float64(J5),np.float64(J6)]
				
				ret = forward_kinematics(phi_angle_ary)
				self.label_49.setText(str(np.around(ret[0],1)))
				self.label_43.setText(str(np.around(ret[1],1)))
				self.label_50.setText(str(np.around(ret[2],1)))
				self.label_48.setText(str(np.around(ret[3],1)))
				self.label_41.setText(str(np.around(ret[4],1)))
				self.label_44.setText(str(np.around(ret[5],1)))
	def receiveData(self):
		while True:
			time.sleep(0.1)
			self.recvData = self.com.read(1024)
			# print("type(recvData.decode())=",type(recvData.decode()))
			# print("len(recvData.decode())=",len(recvData.decode()))
			# print(recvData.decode())

			if self.recvData == b'%':
				
				print("self.zeroingOperationFlag = 1")
				self.zeroingOperationFlag = 1
				self.receiveUpdateSignal.emit(self.recvData.decode())
			if self.recvData == '':
				continue
				
			else:
				if len(self.recvData)!=0:
					
					self.recvDataFlag = 1			
					print("type(self.recvData)=",type(self.recvData))
					print("len(self.recvData)=",len(self.recvData))
					print("self.recvData=",self.recvData)
					self.receiveUpdateSignal.emit(self.recvData.decode())
					
		
		
	def teach(self):
		sendData = bytes([0x30,0x10,0x14])
		self.com.write(sendData)

	
		print("type(sendData)=",type(sendData))
		print("len(sendData)=",len(sendData))
		print("sendData=",sendData)

	def pushButton_8ClickedFunc(self):
		print("type(self.lineEdit_19.text())=",type(self.lineEdit_19.text()))
		print("len(self.lineEdit_19.text())=",len(self.lineEdit_19.text()))
		print("self.lineEdit_19.text()=",self.lineEdit_19.text())
		if self.lineEdit_19.text() != '0':

			print("call Ui_Dialog.pushButton_8ClickedFunc")

			self.step = float(self.lineEdit_19.text())

			# sendData = bytes([0x30,0x10,0x14])
			# self.com.write(sendData)

		
			# print("type(sendData)=",type(sendData))
			# print("len(sendData)=",len(sendData))
			# print("sendData=",sendData)

			# time.sleep(self.step)

			# #serialPort1.Write("J1-" + "\r\n");
			# #bytes("python", 'ascii') # 字符串，编码
			sendData = bytes("J1-\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

			time.sleep(self.step)

			#serialPort1.Write("J10" + "\r\n");
			sendData = bytes("J10\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_8PressedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_8PressedFunc")

			sendData = bytes("J1-\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_8ReleasedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_8ReleasedFunc")

			sendData = bytes("J10\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)


			


	def pushButton_10ClickedFunc(self):
		if self.lineEdit_19.text() != '0':
			print("call Ui_Dialog.pushButton_10ClickedFunc")

			self.step = float(self.lineEdit_19.text())
			# #serialPort1.Write("J1+" + "\r\n");
			# #bytes("python", 'ascii') # 字符串，编码
			sendData = bytes("J1+\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

			time.sleep(self.step)

			#serialPort1.Write("J10" + "\r\n");
			sendData = bytes("J10\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_10PressedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_10PressedFunc")

			sendData = bytes("J1+\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_10ReleasedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_10ReleasedFunc")

			sendData = bytes("J10\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)


	def pushButton_9ClickedFunc(self):
		if self.lineEdit_19.text() != '0':
			print("call Ui_Dialog.pushButton_9ClickedFunc")

			self.step = float(self.lineEdit_19.text())

			sendData = bytes("J2-\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

			time.sleep(self.step)

			sendData = bytes("J20\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_9PressedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_9PressedFunc")

			sendData = bytes("J2-\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_9ReleasedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_9ReleasedFunc")

			sendData = bytes("J20\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_11ClickedFunc(self):
		if self.lineEdit_19.text() != '0':
			print("call Ui_Dialog.pushButton_11ClickedFunc")

			self.step = float(self.lineEdit_19.text())

			sendData = bytes("J2+\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

			time.sleep(self.step)

			sendData = bytes("J20\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_11PressedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_11PressedFunc")

			sendData = bytes("J2+\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_11ReleasedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_11ReleasedFunc")

			sendData = bytes("J20\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_13ClickedFunc(self):
		if self.lineEdit_19.text() != '0':
			print("call Ui_Dialog.pushButton_13ClickedFunc")

			self.step = float(self.lineEdit_19.text())

			sendData = bytes("J3-\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

			time.sleep(self.step)

			sendData = bytes("J30\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_13PressedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_13PressedFunc")

			sendData = bytes("J3-\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_13ReleasedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_13ReleasedFunc")

			sendData = bytes("J30\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_12ClickedFunc(self):
		if self.lineEdit_19.text() != '0':
			print("call Ui_Dialog.pushButton_12ClickedFunc")

			self.step = float(self.lineEdit_19.text())

			sendData = bytes("J3+\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

			time.sleep(self.step)

			sendData = bytes("J30\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_12PressedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_12PressedFunc")

			sendData = bytes("J3+\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_12ReleasedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_12ReleasedFunc")

			sendData = bytes("J30\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_15ClickedFunc(self):
		if self.lineEdit_19.text() != '0':
			print("call Ui_Dialog.pushButton_15ClickedFunc")

			self.step = float(self.lineEdit_19.text())

			sendData = bytes("J4-\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

			time.sleep(self.step)

			sendData = bytes("J40\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_15PressedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_15PressedFunc")

			sendData = bytes("J4-\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_15ReleasedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_15ReleasedFunc")

			sendData = bytes("J40\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)


	def pushButton_14ClickedFunc(self):
		if self.lineEdit_19.text() != '0':
			print("call Ui_Dialog.pushButton_14ClickedFunc")

			self.step = float(self.lineEdit_19.text())

			sendData = bytes("J4+\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

			time.sleep(self.step)

			sendData = bytes("J40\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_14PressedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_14PressedFunc")

			sendData = bytes("J4+\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_14ReleasedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_14ReleasedFunc")

			sendData = bytes("J40\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_17ClickedFunc(self):
		if self.lineEdit_19.text() != '0':
			print("call Ui_Dialog.pushButton_17ClickedFunc")

			self.step = float(self.lineEdit_19.text())

			sendData = bytes("J5-\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

			time.sleep(self.step)

			sendData = bytes("J50\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_17PressedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_17PressedFunc")

			sendData = bytes("J5-\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_17ReleasedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_17ReleasedFunc")

			sendData = bytes("J50\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)


	def pushButton_16ClickedFunc(self):
		if self.lineEdit_19.text() != '0':
			print("call Ui_Dialog.pushButton_16ClickedFunc")

			self.step = float(self.lineEdit_19.text())

			sendData = bytes("J5+\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

			time.sleep(self.step)

			sendData = bytes("J50\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_16PressedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_16PressedFunc")

			sendData = bytes("J5+\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_16ReleasedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_16ReleasedFunc")

			sendData = bytes("J50\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_19ClickedFunc(self):
		if self.lineEdit_19.text() != '0':
			print("call Ui_Dialog.pushButton_19ClickedFunc")

			self.step = float(self.lineEdit_19.text())

			sendData = bytes("J6-\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

			time.sleep(self.step)

			sendData = bytes("J60\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_19PressedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_19PressedFunc")

			sendData = bytes("J6-\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_19ReleasedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_19ReleasedFunc")

			sendData = bytes("J60\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_18ClickedFunc(self):
		if self.lineEdit_19.text() != '0':

			print("call Ui_Dialog.pushButton_18ClickedFunc")
			self.step = float(self.lineEdit_19.text())
			print(type(self.step))
			print("self.step=",self.step)

			sendData = bytes("J6+\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

			time.sleep(self.step)

			sendData = bytes("J60\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_18PressedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_18PressedFunc")

			sendData = bytes("J6+\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_18ReleasedFunc(self):
		if self.lineEdit_19.text() == '0':
			print("call Ui_Dialog.pushButton_18ReleasedFunc")

			sendData = bytes("J60\r\n",'ascii')
			#sendData = bytes([0x4a,0x31,0x30,0x0d,0x0a])
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

		
	def pushButton_3ClickedFunc(self):

		print("call Ui_Dialog.pushButton_3ClickedFunc")
		print("归零复位")

		sendData = bytes("G00 J1=0 J2=0 J3=0 J4=0 J5=0 J6=0\r\n",'ascii')
		self.com.write(sendData)
		print("type(sendData)=",type(sendData))
		print("len(sendData)=",len(sendData))
		print("sendData=",sendData)

		# time.sleep(self.step)

		# sendData = bytes("J60\r\n",'ascii')
		# self.com.write(sendData)
		# print("type(sendData)=",type(sendData))
		# print("len(sendData)=",len(sendData))
		# print("sendData=",sendData)

	def pushButton_2ClickedFunc(self):

		print("call Ui_Dialog.pushButton_2ClickedFunc")
		print("关机复位")

		sendData = bytes("G00 J1=0 J2=0 J3=0 J4=0 J5= J6=0\r\n",'ascii')
		self.com.write(sendData)
		print("type(sendData)=",type(sendData))
		print("len(sendData)=",len(sendData))
		print("sendData=",sendData)
		time.sleep(10)

		while True:
			time.sleep(1)
			if(self.zeroingOperationFlag==1):
				self.zeroingOperationFlag=0
				sendData = bytes("G00 J1=0 J2=73.0175 J3=-151.4839 J4=0 J5=-74.5222 J6=0\r\n",'ascii')
				self.com.write(sendData)
				print("type(sendData)=",type(sendData))
				print("len(sendData)=",len(sendData))
				print("sendData=",sendData)
				break


		# time.sleep(self.step)

		# sendData = bytes("J60\r\n",'ascii')
		# self.com.write(sendData)
		# print("type(sendData)=",type(sendData))
		# print("len(sendData)=",len(sendData))
		# print("sendData=",sendData)

	def pushButton_20ClickedFunc(self):

		print("call Ui_Dialog.pushButton_20ClickedFunc")
		print("点动")

		j1 = float(self.lineEdit.text())
		j2 = float(self.lineEdit_2.text())
		j3 = float(self.lineEdit_3.text())
		j4 = float(self.lineEdit_4.text())
		j5 = float(self.lineEdit_5.text())
		j6 = float(self.lineEdit_6.text())
		'''
		J1=177.4608 J1=-174.8433

J2范围
J2=66.5941 J2=-51.3983

J3范围
J3=-133.8578 J3=90.1282

J4范围
J4=-198.7518 J4=141.2906

J5范围
J5=-109.719 J5=91.3522

J6范围
J6=-142.1656 J6=不限
		'''

		if((-174.8433<j1<177.4608)and(-51.3983<j2<66.5941)and(-133.8578<j3<90.1282)and(-198.7518<j4<141.2906)and(-109.719<j5<81.3522)and(-142.1656<j6<842.1656)):
			pointCommand = "G00 J1="+str(j1)+" J2="+str(j2)+" J3="+str(j3)+" J4="+str(j4)+" J5="+str(j5)+" J6="+str(j6)+"\r\n"
			print("type(pointCommand)=",type(pointCommand))
			print("len(pointCommand)=",len(pointCommand))
			print(pointCommand)
			sendData = bytes(pointCommand,'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_21ClickedFunc(self):

		print("call Ui_Dialog.pushButton_21ClickedFunc")
		print("重置")

		self.lineEdit.setText("0")
		self.lineEdit_2.setText("0")
		self.lineEdit_3.setText("0")
		self.lineEdit_4.setText("0")
		self.lineEdit_5.setText("0")
		self.lineEdit_6.setText("0")

	def pushButton_bClickedFunc(self):
		print("call Ui_Dialog.pushButton_bClickedFunc")
		print("随机")
		#random.uniform(-11,10)
			
		self.lineEdit.setText(str(np.around(random.uniform(-174.8433,177.4608),1)))
		self.lineEdit_2.setText(str(np.around(random.uniform(-51.3983,66.5941),1)))
		self.lineEdit_3.setText(str(np.around(random.uniform(-133.8578,90.1282),1)))
		self.lineEdit_4.setText(str(np.around(random.uniform(-198.7518,141.2906),1)))
		self.lineEdit_5.setText(str(np.around(random.uniform(-109.719,81.3522),1)))
		self.lineEdit_6.setText(str(np.around(random.uniform(-142.1656,842.1656),1)))

	def pushButton_aClickedFunc(self):
		print("call Ui_Dialog.pushButton_aClickedFunc")
		print("参数配置")

		form1 = QtWidgets.QDialog()
		ui = Ui_ParameterConfiguration()
		ui.setupUi(form1)
		form1.show()
		form1.exec_()

	def pushButton_cClickedFunc(self):
		print("call Ui_Dialog.pushButton_cClickedFunc")
		print("关节输出")

		if self.G07GCMFlag == 0:
			self.G07GCMFlag = 1
			sendData = bytes("G07 GCM=0\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)
		else:
			self.G07GCMFlag = 0
			sendData = bytes("G07 GCM=1\r\n",'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_22ClickedFunc(self):
		print("call Ui_Dialog.pushButton_22ClickedFunc")
		print("求解")
		if (len(self.lineEdit_10.text())!=0)and(len(self.lineEdit_9.text())!=0)and(len(self.lineEdit_8.text())!=0)and(len(self.lineEdit_12.text())!=0)and(len(self.lineEdit_7.text())!=0)and(len(self.lineEdit_11.text())!=0):

			X = float(self.lineEdit_10.text())
			Y = float(self.lineEdit_9.text())
			Z = float(self.lineEdit_8.text())
			i = float(self.lineEdit_12.text())
			j = float(self.lineEdit_7.text())
			k = float(self.lineEdit_11.text())
			listXYZijk = [X,Y,Z,i,j,k]

			sol_list = inverse_kinematics(np.array(listXYZijk))
			
			self.lineEdit_16.setText(str(sol_list[0][0]))
			self.lineEdit_15.setText(str(sol_list[0][1]))
			self.lineEdit_14.setText(str(sol_list[0][2]))
			self.lineEdit_18.setText(str(sol_list[0][3]))
			self.lineEdit_13.setText(str(sol_list[0][4]))
			self.lineEdit_17.setText(str(sol_list[0][5]))

	def pushButton_23ClickedFunc(self):
		print("call Ui_Dialog.pushButton_23ClickedFunc")
		print("执行")

		j1 = float(self.lineEdit_16.text())
		j2 = float(self.lineEdit_15.text())
		j3 = float(self.lineEdit_14.text())
		j4 = float(self.lineEdit_18.text())
		j5 = float(self.lineEdit_13.text())
		j6 = float(self.lineEdit_17.text())
		'''
		J1=177.4608 J1=-174.8433

J2范围
J2=66.5941 J2=-51.3983

J3范围
J3=-133.8578 J3=90.1282

J4范围
J4=-198.7518 J4=141.2906

J5范围
J5=-109.719 J5=91.3522

J6范围
J6=-142.1656 J6=不限
		'''

		if((-174.8433<j1<177.4608)and(-51.3983<j2<66.5941)and(-133.8578<j3<90.1282)and(-198.7518<j4<141.2906)and(-109.719<j5<81.3522)and(-142.1656<j6<842.1656)):
			pointCommand = "G00 J1="+str(j1)+" J2="+str(j2)+" J3="+str(j3)+" J4="+str(j4)+" J5="+str(j5)+" J6="+str(j6)+"\r\n"
			print("type(pointCommand)=",type(pointCommand))
			print("len(pointCommand)=",len(pointCommand))
			print(pointCommand)
			sendData = bytes(pointCommand,'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)

	def pushButton_24ClickedFunc(self):
		print("call Ui_Dialog.pushButton_24ClickedFunc")
		print("重置")

		self.lineEdit_16.setText("0")
		self.lineEdit_15.setText("0")
		self.lineEdit_14.setText("0")
		self.lineEdit_18.setText("0")
		self.lineEdit_13.setText("0")
		self.lineEdit_17.setText("0")

	def pushButton_21shijiaoClickedFunc(self):
		print("call Ui_Dialog.pushButton_21shijiaoClickedFunc")
		print("示教")

		sendData = bytes([0x30,0x10,0x14])
		self.com.write(sendData)

	
		print("type(sendData)=",type(sendData))
		print("len(sendData)=",len(sendData))
		print("sendData=",sendData)

	def pushButtona1ClickedFunc(self):
		print("call Ui_Dialog.pushButton_21shijiaoClickedFunc")
		print("添加")

		# pointCommand = "G00 J1="+str(j1)+" J2="+str(j2)+" J3="+str(j3)+" J4="+str(j4)+" J5="+str(j5)+" J6="+str(j6)+"\r\n"
		# pointCommand = str(len(self.qList))+" :"+"G00 J1="+J1+" J2="+J2+" J3="+J3+" J4="+J4+" J5="+J5+" J6="+J6
		
		J = [J1, J2, J3, J4, J5, J6]
		J = [np.around(float(e), 1) for e in J]

		pointCommand = (',').join(["% 8.1f" % e for e in J])
		pointCommand1 = "G00 %s\r\n" % " ".join(["J%d=%f" % (i+1, e) for i, e in enumerate(J)])
		# pointCommand1 = "G00 J1="+J1+" J2="+J2+" J3="+J3+" J4="+J4+" J5="+J5+" J6="+J6
		# pointCommand = str(np.around(float(J1),1))+","+str(np.around(float(J2),1))+","+str(np.around(float(J3),1))+","+str(np.around(float(J4),1))+","+str(np.around(float(J5),1))+","+str(np.around(float(J6),1))+"\n"
		
		# self.qList[len(self.qList)+3]=pointCommand
		self.qList.append(pointCommand)
		self.qListCommand.append(pointCommand1)
		self.slm.setStringList(self.qList) #设置列表视图的模型 
		self.listViewa9.setModel(self.slm) #单击触发自定义的槽函数 
		self.updateFile()
		# slm=QStringListModel()
		

	def listViewa9ClickedFunc(self,qModelIndex):
		print("call Ui_Dialog.listViewa9ClickedFunc")
		print("listViewa9 onClicked")

		print("type(qModelIndex)=",type(qModelIndex))
		# print("len(qModelIndex)=",len(qModelIndex))
		print("qModelIndex=",qModelIndex)
		print("type(qModelIndex.row())=",type(qModelIndex.row()))
		# print("len(qModelIndex.row())=",len(qModelIndex.row()))
		print("qModelIndex.row()=",qModelIndex.row())
		self.itemNumber = qModelIndex.row()

		# QMessageBox.information(self,'ListWidget','你选择了：'+self.qList[qModelIndex.row()])

	def pushButton_2a8ClickedFunc(self):
		print("call Ui_Dialog.pushButton_2a8ClickedFunc")
		print("删除")
		print("type(self.itemNumber)=",type(self.itemNumber))
		# print("len(qModelIndex)=",len(qModelIndex))
		print("self.itemNumber=",self.itemNumber)
		del self.qList[self.itemNumber]
		del self.qListCommand[self.itemNumber]

		self.slm.setStringList(self.qList) #设置列表视图的模型 
		self.listViewa9.setModel(self.slm) #单击触发自定义的槽函数 
		self.updateFile()
		# QMessageBox.information(self,'ListWidget','你想删除：'+self.qList[qModelIndex.row()])

	def initList(self):
		print("call Ui_Dialog.initList")
		f = open("calibrationValueConfig.txt")  
		line = f.readline()
		# i = 0           # 返回一个文件对象  
		while len(line)!=0:
			# line = f.readline().strip('\n')
			line = line.strip('\n')
			print("type(line)=",type(line))
			print("len(line)=",len(line))
			print("line=",line)
			self.qList.append(line)
			print("type(line.split(','))=",type(line.split(',')))
			print("len(line.split(','))=",len(line.split(',')))
			print("line.split(',')=",line.split(','))

			J = [float(e.strip()) for e in line.split(',')]
			pointCommand1 = "G00 %s\r\n" % " ".join(["J%d=%f" % (i+1, e) for i, e in enumerate(J)])

			# pointCommand1 = "G00 J1="+line.split(',')[0]+" J2="+line.split(',')[1]+" J3="+line.split(',')[2]+" J4="+line.split(',')[3]+" J5="+line.split(',')[4]+" J6="+line.split(',')[5]
			self.qListCommand.append(pointCommand1)

			item = bytes(line,'ascii')
			print("item=",item)
			print("line=",line)
			line = f.readline()  
			# self.qList[i] =  str(i)+" :"+line
			# print("self.qList[i]=",self.qList[i]) 
			# i = i+1

		f.close()  
		# self.qList[len(self.qList)-1]=pointCommand#设置模型列表视图，加载数据列表 
		self.slm.setStringList(self.qList) #设置列表视图的模型 
		self.listViewa9.setModel(self.slm) #单击触发自定义的槽函数 

	def pushButton_3a4ClickedFunc(self):
		print("call Ui_Dialog.pushButton_3a4ClickedFunc")
		print("上移")

		item = self.qList[self.itemNumber-1]
		item1 = self.qListCommand[self.itemNumber-1]
		self.qList[self.itemNumber-1] = self.qList[self.itemNumber]
		self.qList[self.itemNumber] = item
		self.qListCommand[self.itemNumber-1] = self.qListCommand[self.itemNumber]
		self.qListCommand[self.itemNumber] = item1
		self.slm.setStringList(self.qList) #设置列表视图的模型 
		self.listViewa9.setModel(self.slm) #单击触发自定义的槽函数 
		self.updateFile()

	def pushButton_4a7ClickedFunc(self):
		print("call Ui_Dialog.pushButton_4a7ClickedFunc")
		print("下移")

		item = self.qList[self.itemNumber+1]
		item1 = self.qListCommand[self.itemNumber+1]
		self.qList[self.itemNumber+1] = self.qList[self.itemNumber]
		self.qList[self.itemNumber] = item
		self.qListCommand[self.itemNumber+1] = self.qListCommand[self.itemNumber]
		self.qListCommand[self.itemNumber] = item1
		self.slm.setStringList(self.qList) #设置列表视图的模型 
		self.listViewa9.setModel(self.slm) #单击触发自定义的槽函数 
		self.updateFile()

	def pushButton_5a3ClickedFunc(self):
		print("call Ui_Dialog.pushButton_5a3ClickedFunc")
		print("执行")

		self.receiveProcess = threading.Thread(target=self.cycleCommand)
		self.receiveProcess.setDaemon(True)
		self.receiveProcess.start()

	def updateFile(self):
		f = open("calibrationValueConfig.txt","w+")
		lists=[line+"\n" for line in self.qList]
		# f.writelines(self.qList)
		f.writelines(lists)
		f.close()
		print("calibrationValueConfig.txt update succeed")


	def pushButton_5b3ClickedFunc(self):
		print("call Ui_Dialog.pushButton_5b3ClickedFunc")
		print("停止")
		self.stopFlag = 1

	def cycleCommand(self):
		print("call Ui_Dialog.cycleCommand")

		
		# for i in range(len(self.qList)):
		time.sleep(2)
		for i in range(len(self.qListCommand)):
		# pointCommand = "G00 J1="+J1+" J2="+J2+" J3="+J3+" J4="+J4+" J5="+J5+" J6="+J6+"\r\n"
		# print("type(pointCommand)=",type(pointCommand))
		# print("len(pointCommand)=",len(pointCommand))
		# print(pointCommand)
			if self.stopFlag == 1:
				print("========self.stopFlag = 0")
				self.stopFlag = 2
				break
			sendData = bytes(self.qListCommand[i].strip('\n')+"\r\n",'ascii')
			# sendData = bytes(pointCommand,'ascii')
			self.com.write(sendData)
			print("type(sendData)=",type(sendData))
			print("len(sendData)=",len(sendData))
			print("sendData=",sendData)
			print("i1=",i)
			# if(i==(len(self.qListCommand)-1)):
			# 	i = 0
			# time.sleep(5)

			number = 0
			while True:
				if number == 20:
					break
				time.sleep(1)
				number = number + 1
				# print("i2=",i)
				# print("self.zeroingOperationFlag=", self.zeroingOperationFlag)
				print("############ %d" % number)
				if self.zeroingOperationFlag == 1:
					break

			self.zeroingOperationFlag = 0
			# time.sleep(5)
			print("int(self.lineEdita2.text())=",int(self.lineEdita2.text()))
			time.sleep(int(self.lineEdita2.text()))
			
			print("i3=",i)
		# print("========self.stopFlag = 1")
		# if self.stopFlag == 2:
		# 	self.stopFlag = 0
		# 	print("========self.stopFlag = 2")
		# 	break
			





		


		
			

		
		

