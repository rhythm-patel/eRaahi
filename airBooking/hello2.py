# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from backend import backend

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		MainWindow.setStyleSheet("background-color: rgb(78, 154, 6);")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(580, 70, 161, 61))
		self.pushButton.setStyleSheet("border-right-color: rgb(239, 41, 41);\n"
			"background-color: rgb(252, 175, 62);")
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.pushOutput)
		######################

		self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
		self.tableWidget.setGeometry(QtCore.QRect(100, 200, 1000, 192))
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setColumnCount(6)
		self.tableWidget.setRowCount(0)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(5, item)


		######################
		self.mybackend = backend()
		########################
		self.countryBox = QtWidgets.QComboBox(self.centralwidget)
		self.countryBox.setGeometry(QtCore.QRect(35, 60, 131, 41))
		self.countryBox.setStyleSheet("background-color: rgb(233, 185, 110);")
		self.countryBox.setObjectName("comboBox")
		self.countryBox.currentTextChanged.connect(self.printCountry)
		
		#####################

		self.cityBox = QtWidgets.QComboBox(self.centralwidget)
		self.cityBox.setGeometry(QtCore.QRect(185, 60, 131, 41))
		self.cityBox.setStyleSheet("background-color: rgb(233, 185, 110);")
		self.cityBox.setObjectName("comboBox")
		#self.cityBox.currentTextChanged.connect(self.printCountry)
		self.countryOptions()
		self.cityOptions()
		
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setAutoFillBackground(False)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		
		
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def printCountry(self):
		print(self.countryBox.currentText())
		if (self.countryBox.currentText() != "Country"):
			k = self.cityBox.count()
			print("k:", k)
			while(k>0):
				self.cityBox.removeItem(0)
				k-=1
			self.cityBox.addItems(self.mybackend.city4country(self.countryBox.currentText()))
		else:
			self.cityOptions()

	def countryOptions(self):
		
		self.countryBox.addItem("Country")
		self.countryBox.addItems(self.mybackend.countries)
	
	def cityOptions(self):
		k = self.cityBox.count()
		print("k:", k)
		while(k>0):
			self.cityBox.removeItem(0)
			k-=1
		self.cityBox.addItems(self.mybackend.cities)

		

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "PushButton"))
	def pushOutput(self):
		flights = self.mybackend.getFlights(self.cityBox.currentText())
		for i in flights:
			self.tableWidget.insertRow(0)
			for j in range(5):
				self.tableWidget.setItem(0,j,QtWidgets.QTableWidgetItem(str(i[j])))
			self.tableWidget.setItem(0,5,(QtWidgets.QPushButton(self.centralwidget)).setStyleSheet("border-right-color: rgb(239, 41, 41);\n"
			"background-color: rgb(252, 175, 62);"))
				

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
