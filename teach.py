# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1046, 583)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(430, 300, 120, 80))
        self.widget.setObjectName("widget")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 481, 121))
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
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(530, 400, 511, 171))
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
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 210, 481, 91))
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
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(530, 0, 511, 371))
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "示教"))
        self.groupBox.setTitle(_translate("Dialog", "手动"))
        self.groupBox_2.setTitle(_translate("Dialog", "状态"))
        self.groupBox_4.setTitle(_translate("Dialog", "点动"))
        self.groupBox_3.setTitle(_translate("Dialog", "逆解"))
        self.groupBox_5.setTitle(_translate("Dialog", "三维模拟区"))
        self.pushButton_2.setText(_translate("Dialog", "关机复位"))
        self.pushButton_3.setText(_translate("Dialog", "归零复位"))
        self.pushButton.setText(_translate("Dialog", "TCP配置"))

