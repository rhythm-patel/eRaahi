# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer_output.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
##########################################
from backend import backend

class QCustomQWidget (QtWidgets.QWidget):
	def __init__ (self, parent = None):
		super(QCustomQWidget, self).__init__(parent)

		self.textQVBoxRightLayout = QtWidgets.QVBoxLayout()
		self.averagePriceLabel = QtWidgets.QLabel()
		self.percentageBookedLabel = QtWidgets.QLabel()
		self.textQVBoxRightLayout.addWidget(self.averagePriceLabel,0)
		self.textQVBoxRightLayout.addWidget(self.percentageBookedLabel,1)
		self.textQVBoxRightLayout.setAlignment(QtCore.Qt.AlignRight)

		self.insideQHBoxLayout = QtWidgets.QHBoxLayout()
		self.averageRatingLabel = QtWidgets.QLabel()
		self.localityLabel = QtWidgets.QLabel()
		self.insideQHBoxLayout.addWidget(self.averageRatingLabel,0)
		self.insideQHBoxLayout.addWidget(self.localityLabel,1)


		self.textQVBoxLeftLayout = QtWidgets.QVBoxLayout()
		self.hotelNameLabel = QtWidgets.QLabel()
		self.textQVBoxLeftLayout.addWidget(self.hotelNameLabel,0)
		self.textQVBoxLeftLayout.addLayout(self.insideQHBoxLayout,1)

		self.allQHBoxLayout = QtWidgets.QHBoxLayout()
		self.allQHBoxLayout.addLayout(self.textQVBoxLeftLayout, 0)
		self.allQHBoxLayout.addLayout(self.textQVBoxRightLayout, 1)
		self.setLayout(self.allQHBoxLayout)

	def setTextOnAllLabel (self, hotelNameLabel,averageRatingLabel,localityLabel,averagePriceLabel,percentageBookedLabel):
		self.hotelNameLabel.setText(hotelNameLabel)
		self.averageRatingLabel.setText(averageRatingLabel)
		self.localityLabel.setText(localityLabel)
		self.averagePriceLabel.setText(averagePriceLabel)
		self.percentageBookedLabel.setText(percentageBookedLabel)

######################################################


class Ui_MainWindow(object):
	clicked=False;
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		self.Stack = QtWidgets.QStackedWidget(MainWindow)


		self.centralwidget1 = QtWidgets.QWidget(MainWindow)
		self.centralwidget1.setObjectName("centralwidget1")
		self.button = QtWidgets.QPushButton(self.centralwidget1)
		self.button.setGeometry(QtCore.QRect(360, 510, 75, 23))
		self.button.setObjectName("button")
		self.listWidget = QtWidgets.QListWidget(self.centralwidget1)
		self.listWidget.setGeometry(QtCore.QRect(0, 90, 801, 411))
		self.listWidget.setObjectName("listWidget")

		self.centralwidget2 = QtWidgets.QWidget(MainWindow)
		self.centralwidget2.setObjectName("centralwidget2")
		self.testLabel = QtWidgets.QLabel(self.centralwidget2)
		self.testLabel.setGeometry(QtCore.QRect(246, 152, 411, 201))
		self.testLabel.setObjectName("testLabel")
		
		print(self.Stack.addWidget(self.centralwidget1))
		print(self.Stack.addWidget(self.centralwidget2))
		MainWindow.setCentralWidget(self.Stack)


		# MainWindow.setCentralWidget(self.centralwidget1)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
###################################################
		self.mybackend = backend()
		self.button.clicked.connect(self.check)
		self.listWidget.itemClicked.connect(self.test)
		self.listWidget.itemSelectionChanged.connect(self.selectionChanged)


	def selectionChanged(self):
		tempCustomQWidget = self.listWidget.itemWidget(self.listWidget.selectedItems()[0])
		test = tempCustomQWidget.hotelNameLabel
		self.testLabel.setText(test.text())
		self.Stack.setCurrentWidget(self.centralwidget2)
		print(test.text())

	def test(self):
		if(self.clicked==False):
			print('clicked')
		self.clicked=True;

	def check(self):
		self.hotels = self.mybackend.getallhotel()
		for name,hid,loc,avg_price,booked,rating in self.hotels:
			myQCustomQWidget = QCustomQWidget()
			myQCustomQWidget.setTextOnAllLabel('Name : ' +name,'Avg. Rating : '+rating,'Locality : '+loc,'Avg. Price : '+avg_price,'Booked : '+booked)
			listWidgetItem = QtWidgets.QListWidgetItem(self.listWidget)
			listWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
			# self.listWidget.itemClicked.connect(self.test())
			self.listWidget.addItem(listWidgetItem)
			self.listWidget.setItemWidget(listWidgetItem, myQCustomQWidget)


########################################################

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.button.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
