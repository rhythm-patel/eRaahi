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

		self.tableWidget = QtWidgets.QGridLayout(self.centralwidget)
		self.tableWidget.setGeometry(QtCore.QRect(100, 200, 1000, 192))
		self.tableWidget.setObjectName("tableWidget")


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
		self.pushButton.setText(_translate("MainWindow", "Search"))
	def pushOutput(self):
		print(self.tableWidget.rowCount())
		print(self.tableWidget.rowCount())
		#for i in range(self.tableWidget.rowCount()):
		#	for j in range(self.tableWidget.columnCount()):
		#		if (self.tableWidget.itemAtPosition(i,j) != None):
		#			self.tableWidget.removeWidget(self.tableWidget.itemAtPosition(i,j))
		#			self.tableWidget.itemAtPosition(i, j).deleteLater()
		for i in reversed(range(self.tableWidget.count())):
			if (self.tableWidget.itemAt(i)!= None):
				self.tableWidget.itemAt(i).widget().deleteLater()		
		flights = self.mybackend.getFlights(self.cityBox.currentText())
		print(flights)
		for i in range(len(flights)):
			
			for j in range(5):
				self.tableWidget.addWidget(QtWidgets.QLabel(str(flights[i][j])), i, j)
			btn = QtWidgets.QPushButton("Book Now", self.centralwidget)
			print(type(flights[i][0]))
			btn.clicked.connect(lambda : self.bookingWindow(str(flights[i][0]), flights[i][-1][0]))
			self.tableWidget.addWidget(btn, i, 5)
	
	""" 	def bookingWindow(self, flightNo, numSeats):
			choice = QtWidgets.QMessageBox.question(self.centralwidget, 'Confirm Booking',
												"Number of seats available = {}. Are you sure?".format(numSeats),
												QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
			spinbox = QtWidgets.QSpinBox(choice) """
	def bookingWindow(self, flightNo, numSeats):

		def confirmBooking():
			self.mybackend.bookSeats(flightNo, numSeats)
			window.close()
			print("Hello")
		window = QtWidgets.QDialog()
		window.setObjectName("Confirm Booking")
		layout = QtWidgets.QVBoxLayout()
		label = QtWidgets.QLabel("Please select number of seats to be booked.")
		layout.addWidget(label)
		submitButton = QtWidgets.QPushButton("Submit")
		submitButton.setObjectName("Submit")
		submitButton.clicked.connect(confirmBooking)
		spinbox = QtWidgets.QSpinBox(window)
		spinbox.setMaximum(numSeats)
		spinbox.setMinimum(1)
		layout.addWidget(spinbox)
		layout.addWidget(submitButton)
		window.setLayout(layout)
		window.setModal(True)
		window.exec()					

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
