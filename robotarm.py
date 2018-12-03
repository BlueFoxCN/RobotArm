import sys  
from PyQt5.QtWidgets import QApplication, QWidget ,QMainWindow   #导入相应的包
from teach import *     
from mainwindow import *     

if __name__ == '__main__':  
      
	app = QApplication(sys.argv)       
	# w = QWidget()   
	w = QMainWindow()    

	#ui=Ui_Form()
	ui = Ui_MainWindow()
	ui.setupUi(w)
	w.show()         

	sys.exit( app.exec_() )
