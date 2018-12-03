# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys  
from PyQt5.QtWidgets import QApplication, QWidget ,QMainWindow   #导入相应的包
from dialog import *     

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		#self.form = MainWindow
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(226, 319)
		self.centralWidget = QtWidgets.QWidget(MainWindow)
		self.centralWidget.setObjectName("centralWidget")
		self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 160, 231))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(11, 11, 11, 11)
		self.verticalLayout.setSpacing(6)
		self.verticalLayout.setObjectName("verticalLayout")
		self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(21)
		self.pushButton.setFont(font)
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.pushButtonClickedFunc)
		self.verticalLayout.addWidget(self.pushButton)
		self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(21)
		self.pushButton_3.setFont(font)
		self.pushButton_3.setObjectName("pushButton_3")
		self.verticalLayout.addWidget(self.pushButton_3)
		self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(21)
		self.pushButton_2.setFont(font)
		self.pushButton_2.setObjectName("pushButton_2")
		self.verticalLayout.addWidget(self.pushButton_2)
		MainWindow.setCentralWidget(self.centralWidget)
		self.menuBar = QtWidgets.QMenuBar(MainWindow)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 226, 31))
		self.menuBar.setObjectName("menuBar")
		MainWindow.setMenuBar(self.menuBar)
		self.mainToolBar = QtWidgets.QToolBar(MainWindow)
		self.mainToolBar.setObjectName("mainToolBar")
		MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
		self.statusBar = QtWidgets.QStatusBar(MainWindow)
		self.statusBar.setObjectName("statusBar")
		MainWindow.setStatusBar(self.statusBar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "机械臂测试"))
		self.pushButton.setText(_translate("MainWindow", "示教"))
		self.pushButton_3.setText(_translate("MainWindow", "仿真"))
		self.pushButton_2.setText(_translate("MainWindow", "标定"))
	def pushButtonClickedFunc(self):
		print("call Ui_MainWindow.pushButtonClickedFunc")
		#self.form.hide()            #如果没有self.form.show()这一句，关闭Demo1界面后就会关闭程序
		form1 = QtWidgets.QDialog()
		ui = Ui_Dialog()
		ui.setupUi(form1)
		form1.show()
		form1.exec_()
		#self.form.show()


		return



if __name__ == '__main__':  
      
	app = QApplication(sys.argv)       
	# w = QWidget()   
	w = QMainWindow()    

	#ui=Ui_Form()
	ui = Ui_MainWindow()
	ui.setupUi(w)
	w.show()         

	sys.exit( app.exec_() )


