from PyQt5 import QtCore, QtGui, QtWidgets
from backendHotel import backendHotel
from backendAttraction import backendAttraction
from backendRestaurant import backendRestaurant, RSS
from backendFlight import backendFlight
from frontendMovie import ReviewScreen, runn
from PyQt5.QtWidgets import QApplication
from datetime import datetime
from adminMode import adminmovieRun
import os

class AttractionWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AttractionWidget, self).__init__(parent)

        self.box = QtWidgets.QVBoxLayout()
        self.nameLabel = QtWidgets.QLabel()
        self.typeLabel = QtWidgets.QLabel()
        self.durationLabel = QtWidgets.QLabel()
        self.startTimeLabel = QtWidgets.QLabel()
        self.costLabel = QtWidgets.QLabel()
        self.summaryLabel = QtWidgets.QLabel()

        self.box.addWidget(self.nameLabel)
        self.box.addWidget(self.typeLabel)
        self.box.addWidget(self.durationLabel)
        self.box.addWidget(self.startTimeLabel)
        self.box.addWidget(self.costLabel)
        self.box.addWidget(self.summaryLabel)

        self.setLayout(self.box)

    def setTextOnAllLabel(self, name, typeAttraction, duration, start, cost, summmary):
        self.nameLabel.setText(name)
        self.typeLabel.setText(typeAttraction)
        self.durationLabel.setText(duration)
        self.startTimeLabel.setText(start)
        self.costLabel.setText(cost)
        self.summaryLabel.setText(summmary)


class RestaurantWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(RestaurantWidget, self).__init__(parent)

        self.box = QtWidgets.QVBoxLayout()
        self.venueLabel = QtWidgets.QLabel()
        self.categoryLabel = QtWidgets.QLabel()
        self.costLabel = QtWidgets.QLabel()
        self.likeLabel = QtWidgets.QLabel()

        self.box.addWidget(self.venueLabel)
        self.box.addWidget(self.categoryLabel)
        self.box.addWidget(self.costLabel)
        self.box.addWidget(self.likeLabel)

        self.setLayout(self.box)

    def setTextOnAllLabel(self, venue, category, cost, like):
        self.venueLabel.setText(venue)
        self.categoryLabel.setText(category)
        self.costLabel.setText(cost)
        self.likeLabel.setText(like)



class QCustomQWidget2(QtWidgets.QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget2, self).__init__(parent)
        self.QHBoxLayout = QtWidgets.QHBoxLayout()
        self.customerNameLabel = QtWidgets.QLabel()
        self.starsLabel = QtWidgets.QLabel()
        self.reviewLabel = QtWidgets.QLabel()
        self.QHBoxLayout.addWidget(self.customerNameLabel,0)
        self.QHBoxLayout.addStretch()
        self.QHBoxLayout.addWidget(self.reviewLabel,1)
        self.reviewLabel.setAlignment(QtCore.Qt.AlignRight)
        self.setLayout(self.QHBoxLayout)

    def setTextOnAllLabel(self, customerName,review):
        self.customerNameLabel.setText(customerName)
        self.reviewLabel.setText(review)


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
class QCustomQWidget3 (QtWidgets.QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget3, self).__init__(parent)

        self.booktextQVBoxRightLayout = QtWidgets.QVBoxLayout()
        self.bookCapacityLabel = QtWidgets.QLabel()
        self.bookCostLabel = QtWidgets.QLabel()
        self.booktextQVBoxRightLayout.addWidget(self.bookCostLabel,1)
        self.booktextQVBoxRightLayout.addWidget(self.bookCapacityLabel,0)
        self.booktextQVBoxRightLayout.setAlignment(QtCore.Qt.AlignRight)
        self.booktextQVBoxLeftLayout = QtWidgets.QVBoxLayout()
        self.bookRoomIDLabel = QtWidgets.QLabel()
        self.booktextQVBoxLeftLayout.addWidget(self.bookRoomIDLabel,0)
        self.allQHBoxLayout = QtWidgets.QHBoxLayout()
        self.allQHBoxLayout.addLayout(self.booktextQVBoxLeftLayout, 0)
        self.allQHBoxLayout.addLayout(self.booktextQVBoxRightLayout, 1)
        self.setLayout(self.allQHBoxLayout)

    def setTextOnAllLabel (self, cost,cap,room_id):
        self.bookCostLabel.setText(cost)
        self.bookCapacityLabel.setText(cap)
        self.bookRoomIDLabel.setText(room_id)


class Ui_MainWindow(object):
    ADMIN_MODE=False
    CUSTOMER_MODE=True
    USER_ID = 0
    BALANCE = 0

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.Stack = QtWidgets.QStackedWidget(MainWindow)
        self.mybackend = backendHotel()
        self.reviewcentralwidget = QtWidgets.QWidget(MainWindow)
        self.reviewcentralwidget.setObjectName("reviewcentralwidget")
        self.logoLabel = QtWidgets.QLabel(self.reviewcentralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(0, 0, 800, 100))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap("E - Raahi.png"))
        self.logoLabel.setObjectName("logoLabel")
        self.balanceLabel = QtWidgets.QLabel(self.reviewcentralwidget)
        self.balanceLabel.setGeometry(QtCore.QRect(600, 100, 200, 30))
        self.balanceLabel.setObjectName("balanceLabel")
        self.indetifierLabel = QtWidgets.QLabel(self.reviewcentralwidget)
        self.indetifierLabel.setGeometry(QtCore.QRect(350, 100, 100, 30))
        self.indetifierLabel.setTextFormat(QtCore.Qt.RichText)
        self.indetifierLabel.setScaledContents(True)
        self.indetifierLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.indetifierLabel.setObjectName("indetifierLabel")
        self.overviewButton = QtWidgets.QPushButton(self.reviewcentralwidget)
        self.overviewButton.setGeometry(QtCore.QRect(0, 130, 266, 25))
        self.overviewButton.setObjectName("overviewButton")
        self.overviewButton.clicked.connect(self.overviewClicked)
        self.reviewbookButton = QtWidgets.QPushButton(self.reviewcentralwidget)
        self.reviewbookButton.setGeometry(QtCore.QRect(267, 130, 266, 25))
        self.reviewbookButton.setObjectName("reviewbookButton")
        self.reviewButton = QtWidgets.QPushButton(self.reviewcentralwidget)
        self.reviewButton.setGeometry(QtCore.QRect(532, 130, 267, 25))
        self.reviewButton.setObjectName("reviewButton")
        self.backButton = QtWidgets.QPushButton(self.reviewcentralwidget)
        self.backButton.setGeometry(QtCore.QRect(0, 100, 151, 31))
        self.backButton.setObjectName("backButton")
        self.reviewlistWidget = QtWidgets.QListWidget(self.reviewcentralwidget)
        self.reviewlistWidget.setGeometry(QtCore.QRect(0, 180, 800, 399))
        self.reviewlistWidget.setObjectName("reviewlistWidget")
        self.rbalanceLabel = QtWidgets.QLabel(self.reviewcentralwidget)
        self.rbalanceLabel.setGeometry(QtCore.QRect(600, 100, 200, 30))
        self.rbalanceLabel.setObjectName("rbalanceLabel")
        self.custNameLabel = QtWidgets.QLabel(self.reviewcentralwidget)
        self.custNameLabel.setGeometry(QtCore.QRect(0, 155, 200, 25))
        self.custNameLabel.setObjectName("custNameLabel")
        self.label = QtWidgets.QLabel(self.reviewcentralwidget)
        self.label.setGeometry(QtCore.QRect(650, 155, 150, 25))
        self.label.setObjectName("label")
        self.sortReviewButton = QtWidgets.QToolButton(self.reviewcentralwidget)
        self.sortReviewButton.setGeometry(QtCore.QRect(305, 155, 200, 25))
        self.sortReviewButton.setObjectName("sortReviewButton")
        self.reviewbookButton.clicked.connect(self.reviewbookclick)
        self.centralwidget1 = QtWidgets.QWidget(MainWindow)
        self.centralwidget1.setObjectName("centralwidget1")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget1)
        self.listWidget.setGeometry(QtCore.QRect(0, 130, 800, 369))
        self.listWidget.setObjectName("listWidget")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget1)
        self.logoLabel.setGeometry(QtCore.QRect(0, 0, 800, 100))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap("E - Raahi.png"))
        self.logoLabel.setObjectName("logoLabel")
        self.hotelButton = QtWidgets.QPushButton(self.centralwidget1)
        self.hotelButton.setGeometry(QtCore.QRect(0, 499, 160, 60))
        self.hotelButton.setObjectName("hotelButton")
        self.airlinesButton = QtWidgets.QPushButton(self.centralwidget1)
        self.airlinesButton.setGeometry(QtCore.QRect(160, 499, 160, 60))
        self.airlinesButton.setStatusTip("")
        self.airlinesButton.setObjectName("airlinesButton")
        self.movieButton = QtWidgets.QPushButton(self.centralwidget1)
        self.movieButton.setGeometry(QtCore.QRect(320, 499, 160, 60))
        self.movieButton.setObjectName("movieButton")
        self.attractionButton = QtWidgets.QPushButton(self.centralwidget1)
        self.attractionButton.setGeometry(QtCore.QRect(480, 499, 160, 60))
        self.attractionButton.setObjectName("attractionButton")
        self.RestaurantButton = QtWidgets.QPushButton(self.centralwidget1)
        self.RestaurantButton.setGeometry(QtCore.QRect(640, 499, 160, 60))
        self.RestaurantButton.setObjectName("RestaurantButton")
        self.sortButton = QtWidgets.QToolButton(self.centralwidget1)
        self.sortButton.setGeometry(QtCore.QRect(600, 100, 200, 30))
        self.sortButton.setObjectName("sortButton")
        self.balanceLabel = QtWidgets.QLabel(self.centralwidget1)
        self.balanceLabel.setGeometry(QtCore.QRect(0, 100, 200, 30))
        self.balanceLabel.setObjectName("balanceLabel")
        self.indentifierLabel = QtWidgets.QLabel(self.centralwidget1)
        self.indentifierLabel.setGeometry(QtCore.QRect(350, 100, 100, 30))
        self.indentifierLabel.setTextFormat(QtCore.Qt.RichText)
        self.indentifierLabel.setScaledContents(True)
        self.indentifierLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.indentifierLabel.setObjectName("indentifierLabel")

        self.overviewcentralwidget = QtWidgets.QWidget(MainWindow)
        self.overviewcentralwidget.setObjectName("overviewcentralwidget")
        self.ovlogoLabel = QtWidgets.QLabel(self.overviewcentralwidget)
        self.ovlogoLabel.setGeometry(QtCore.QRect(0, 0, 800, 100))
        self.ovlogoLabel.setText("")
        self.ovlogoLabel.setPixmap(QtGui.QPixmap("E - Raahi.png"))
        self.ovlogoLabel.setObjectName("ovlogoLabel")
        self.ovbalanceLabel = QtWidgets.QLabel(self.overviewcentralwidget)
        self.ovbalanceLabel.setGeometry(QtCore.QRect(600, 100, 200, 30))
        self.ovbalanceLabel.setObjectName("ovbalanceLabel")
        self.ovindetifierLabel = QtWidgets.QLabel(self.overviewcentralwidget)
        self.ovindetifierLabel.setGeometry(QtCore.QRect(350, 100, 100, 30))
        self.ovindetifierLabel.setTextFormat(QtCore.Qt.RichText)
        self.ovindetifierLabel.setScaledContents(True)
        self.ovindetifierLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ovindetifierLabel.setObjectName("ovindetifierLabel")
        self.ovoverviewButton = QtWidgets.QPushButton(self.overviewcentralwidget)
        self.ovoverviewButton.setGeometry(QtCore.QRect(0, 130, 266, 25))
        self.ovoverviewButton.setObjectName("ovoverviewButton")
        self.ovbookButton = QtWidgets.QPushButton(self.overviewcentralwidget)
        self.ovbookButton.setGeometry(QtCore.QRect(267, 130, 266, 25))
        self.ovbookButton.setObjectName("ovbookButton")
        self.ovreviewButton = QtWidgets.QPushButton(self.overviewcentralwidget)
        self.ovreviewButton.setGeometry(QtCore.QRect(532, 130, 267, 25))
        self.ovreviewButton.setObjectName("ovreviewButton")
        self.ovbackButton = QtWidgets.QPushButton(self.overviewcentralwidget)
        self.ovbackButton.setGeometry(QtCore.QRect(0, 100, 151, 31))
        self.ovbackButton.setObjectName("ovbackButton")
        self.nLabel = QtWidgets.QLabel(self.overviewcentralwidget)
        self.nLabel.setGeometry(QtCore.QRect(10, 160, 541, 111))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.nLabel.setFont(font)
        self.nLabel.setObjectName("nLabel")
        self.pLabel = QtWidgets.QLabel(self.overviewcentralwidget)
        self.pLabel.setGeometry(QtCore.QRect(570, 160, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pLabel.setFont(font)
        self.pLabel.setObjectName("pLabel")
        self.lLabel = QtWidgets.QLabel(self.overviewcentralwidget)
        self.lLabel.setGeometry(QtCore.QRect(10, 280, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lLabel.setFont(font)
        self.lLabel.setObjectName("lLabel")
        self.rLabel = QtWidgets.QLabel(self.overviewcentralwidget)
        self.rLabel.setGeometry(QtCore.QRect(0, 370, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rLabel.setFont(font)
        self.rLabel.setObjectName("rLabel")
        self.bLabel = QtWidgets.QLabel(self.overviewcentralwidget)
        self.bLabel.setGeometry(QtCore.QRect(520, 370, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bLabel.setFont(font)
        self.bLabel.setObjectName("bLabel")
        self.ovbackButton.clicked.connect(self.backClick)
        self.ovreviewButton.clicked.connect(self.reviewtab)
        self.ovbookButton.clicked.connect(self.ovbookclick)
        self.bookcentralwidget = QtWidgets.QWidget(MainWindow)
        self.bookcentralwidget.setObjectName("bookcentralwidget")
        self.bookLogoLabel = QtWidgets.QLabel(self.bookcentralwidget)
        self.bookLogoLabel.setGeometry(QtCore.QRect(0, 0, 800, 100))
        self.bookLogoLabel.setText("")
        self.bookLogoLabel.setPixmap(QtGui.QPixmap("E - Raahi.png"))
        self.bookLogoLabel.setObjectName("bookLogoLabel")
        self.bookBalanceLabel = QtWidgets.QLabel(self.bookcentralwidget)
        self.bookBalanceLabel.setGeometry(QtCore.QRect(600, 100, 200, 30))
        self.bookBalanceLabel.setObjectName("bookBalanceLabel")
        self.bookIndetifierLabel = QtWidgets.QLabel(self.bookcentralwidget)
        self.bookIndetifierLabel.setGeometry(QtCore.QRect(350, 100, 100, 30))
        self.bookIndetifierLabel.setTextFormat(QtCore.Qt.RichText)
        self.bookIndetifierLabel.setScaledContents(True)
        self.bookIndetifierLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bookIndetifierLabel.setObjectName("bookIndetifierLabel")
        self.bookOverviewButton = QtWidgets.QPushButton(self.bookcentralwidget)
        self.bookOverviewButton.setGeometry(QtCore.QRect(0, 130, 266, 25))
        self.bookOverviewButton.setObjectName("bookOverviewButton")
        self.bookButton = QtWidgets.QPushButton(self.bookcentralwidget)
        self.bookButton.setGeometry(QtCore.QRect(267, 130, 266, 25))
        self.bookButton.setObjectName("bookButton")
        self.bookReviewButton = QtWidgets.QPushButton(self.bookcentralwidget)
        self.bookReviewButton.setGeometry(QtCore.QRect(532, 130, 267, 25))
        self.bookReviewButton.setObjectName("bookReviewButton")
        self.bookBackButton = QtWidgets.QPushButton(self.bookcentralwidget)
        self.bookBackButton.setGeometry(QtCore.QRect(0, 100, 151, 31))
        self.bookBackButton.setObjectName("bookBackButton")
        self.bookListWidget = QtWidgets.QListWidget(self.bookcentralwidget)
        self.bookListWidget.setGeometry(QtCore.QRect(0, 155, 600, 404))
        self.bookListWidget.setObjectName("bookListWidget")
        self.bookBookingButton = QtWidgets.QPushButton(self.bookcentralwidget)
        self.bookBookingButton.setGeometry(QtCore.QRect(610, 340, 181, 71))
        self.bookBookingButton.setObjectName("bookBookingButton")
        self.bookIDLabel = QtWidgets.QLabel(self.bookcentralwidget)
        self.bookIDLabel.setGeometry(QtCore.QRect(620, 170, 160, 35))
        self.bookIDLabel.setObjectName("bookIDLabel")
        self.bookCapacity = QtWidgets.QLabel(self.bookcentralwidget)
        self.bookCapacity.setGeometry(QtCore.QRect(620, 215, 160, 35))
        self.bookCapacity.setObjectName("bookCapacity")
        self.bookCostLabel = QtWidgets.QLabel(self.bookcentralwidget)
        self.bookCostLabel.setGeometry(QtCore.QRect(620, 270, 160, 35))
        self.bookCostLabel.setObjectName("bookCostLabel")
        self.bookBackButton.clicked.connect(self.bookbackclick)
        self.bookReviewButton.clicked.connect(self.bookreviewclick)
        self.bookOverviewButton.clicked.connect(self.bookoverviewclick)
        self.bookCostLabel.setText("Cost : ")
        self.bookCapacity.setText("Capacity : ")
        self.bookIDLabel.setText("Room ID : ")
        self.bookBookingButton.clicked.connect(self.bookRoomButtonClicked)
        self.logincentralwidget = QtWidgets.QWidget(MainWindow)
        self.logincentralwidget.setObjectName("logincentralwidget")
        self.loginModeLabel = QtWidgets.QLabel(self.logincentralwidget)
        self.loginModeLabel.setGeometry(QtCore.QRect(260, 160, 261, 101))
        font = QtGui.QFont()
        font.setFamily("Reem Kufi")
        font.setPointSize(28)
        self.loginModeLabel.setFont(font)
        self.loginModeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loginModeLabel.setObjectName("loginModeLabel")
        self.loginModeLabel.setText("e-Raahi")
        self.loginIDTextEdit = QtWidgets.QLineEdit(self.logincentralwidget)
        self.loginIDTextEdit.setGeometry(QtCore.QRect(320, 270, 201, 25))
        self.loginIDTextEdit.setObjectName("loginIDTextEdit")
        self.loginIDLabel = QtWidgets.QLabel(self.logincentralwidget)
        self.loginIDLabel.setGeometry(QtCore.QRect(270, 275, 47, 13))
        self.loginIDLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loginIDLabel.setObjectName("loginIDLabel")
        self.loginIDLabel.setText("ID")
        self.loginadminPushButton = QtWidgets.QPushButton(self.logincentralwidget)
        self.loginadminPushButton.setGeometry(QtCore.QRect(440, 370, 131, 31))
        self.loginadminPushButton.setObjectName("loginadminPushButton")
        self.loginadminPushButton.setText("Admin Login")
        self.logincustomerPushButton = QtWidgets.QPushButton(self.logincentralwidget)
        self.logincustomerPushButton.setGeometry(QtCore.QRect(230, 370, 121, 31))
        self.logincustomerPushButton.setObjectName("logincustomerPushButton")
        self.logincustomerPushButton.setText("Customer Login")
        # self.loginPushButton = QtWidgets.QPushButton(self.logincentralwidget)
        # self.loginPushButton.setGeometry(QtCore.QRect(360, 320, 111, 31))
        # self.loginPushButton.setObjectName("loginPushButton")
        # self.loginPushButton.setText("Login")
        self.loginadminPushButton.clicked.connect(self.adminPushButtonClicked)
        self.logincustomerPushButton.clicked.connect(self.customerPushButtonClicked)
        # self.loginPushButton.clicked.connect(self.loginPushButtonClicked)
        self.hoteleditcentralwidget = QtWidgets.QWidget(MainWindow)
        self.hoteleditcentralwidget.setObjectName("hoteleditcentralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.hoteleditcentralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 800, 559))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.hotelVerticalLayout1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.hotelVerticalLayout1.setContentsMargins(0, 0, 0, 0)
        self.hotelVerticalLayout1.setObjectName("hotelVerticalLayout1")
        self.hotelLogoLabel1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelLogoLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.hotelLogoLabel1.setObjectName("hotelLogoLabel1")
        self.hotelVerticalLayout1.addWidget(self.hotelLogoLabel1)
        self.hotelHorizontalLayout11 = QtWidgets.QHBoxLayout()
        self.hotelHorizontalLayout11.setObjectName("hotelHorizontalLayout11")
        self.hotelEditPushButton11 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hotelEditPushButton11.setObjectName("hotelEditPushButton11")
        self.hotelHorizontalLayout11.addWidget(self.hotelEditPushButton11)
        self.hotelIDLabel11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelIDLabel11.setObjectName("hotelIDLabel11")
        self.hotelHorizontalLayout11.addWidget(self.hotelIDLabel11)
        self.hotelIDLineEdit11 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelIDLineEdit11.setObjectName("hotelIDLineEdit11")
        self.hotelHorizontalLayout11.addWidget(self.hotelIDLineEdit11)
        self.hotelVerticalLayout1.addLayout(self.hotelHorizontalLayout11)
        self.hotelHorizontalLayout12 = QtWidgets.QHBoxLayout()
        self.hotelHorizontalLayout12.setObjectName("hotelHorizontalLayout12")
        self.hotelNameLabel12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelNameLabel12.setObjectName("hotelNameLabel12")
        self.hotelHorizontalLayout12.addWidget(self.hotelNameLabel12)
        self.hotelNameLineEdit12 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelNameLineEdit12.setObjectName("hotelNameLineEdit12")
        self.hotelHorizontalLayout12.addWidget(self.hotelNameLineEdit12)
        self.hotelLocIDLabel12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelLocIDLabel12.setObjectName("hotelLocIDLabel12")
        self.hotelHorizontalLayout12.addWidget(self.hotelLocIDLabel12)
        self.hotelLocIDLineEdit12 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelLocIDLineEdit12.setObjectName("hotelLocIDLineEdit12")
        self.hotelHorizontalLayout12.addWidget(self.hotelLocIDLineEdit12)
        self.hotelContactLabel12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelContactLabel12.setObjectName("hotelContactLabel12")
        self.hotelHorizontalLayout12.addWidget(self.hotelContactLabel12)
        self.hotelContactLineEdit12 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelContactLineEdit12.setObjectName("hotelContactLineEdit12")
        self.hotelHorizontalLayout12.addWidget(self.hotelContactLineEdit12)
        self.hotelVerticalLayout1.addLayout(self.hotelHorizontalLayout12)
        self.hotelUpdatePushButton12 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hotelUpdatePushButton12.setObjectName("hotelUpdatePushButton12")
        self.hotelHorizontalLayout12.addWidget(self.hotelUpdatePushButton12)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hotelVerticalLayout1.addItem(spacerItem)
        self.hotelAddPushButton1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hotelAddPushButton1.setObjectName("hotelAddPushButton1")
        self.hotelVerticalLayout1.addWidget(self.hotelAddPushButton1)
        self.hotelHorizontalLayout13 = QtWidgets.QHBoxLayout()
        self.hotelHorizontalLayout13.setObjectName("hotelHorizontalLayout13")
        self.hotelNameLabel13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelNameLabel13.setObjectName("hotelNameLabel13")
        self.hotelHorizontalLayout13.addWidget(self.hotelNameLabel13)
        self.hotelNameLineEdit13 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelNameLineEdit13.setObjectName("hotelNameLineEdit13")
        self.hotelHorizontalLayout13.addWidget(self.hotelNameLineEdit13)
        self.hotelLocIDLabel13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelLocIDLabel13.setObjectName("hotelLocIDLabel13")
        self.hotelHorizontalLayout13.addWidget(self.hotelLocIDLabel13)
        self.hotelLocIDLineEdit13 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelLocIDLineEdit13.setObjectName("hotelLocIDLineEdit13")
        self.hotelHorizontalLayout13.addWidget(self.hotelLocIDLineEdit13)
        self.hotelContactLabel13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelContactLabel13.setObjectName("hotelContactLabel13")
        self.hotelHorizontalLayout13.addWidget(self.hotelContactLabel13)
        self.hotelContactLineEdit13 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelContactLineEdit13.setObjectName("hotelContactLineEdit13")
        self.hotelHorizontalLayout13.addWidget(self.hotelContactLineEdit13)
        self.hotelGoPushButton13 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hotelGoPushButton13.setObjectName("hotelGoPushButton13")
        self.hotelHorizontalLayout13.addWidget(self.hotelGoPushButton13)
        self.hotelVerticalLayout1.addLayout(self.hotelHorizontalLayout13)
        self.hotelLogoLabel2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelLogoLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.hotelLogoLabel2.setObjectName("hotelLogoLabel2")
        self.hotelVerticalLayout1.addWidget(self.hotelLogoLabel2)
        self.hotelHorizontalLayout21 = QtWidgets.QHBoxLayout()
        self.hotelHorizontalLayout21.setObjectName("hotelHorizontalLayout21")
        self.hotelEditPushButton21 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hotelEditPushButton21.setObjectName("hotelEditPushButton21")
        self.hotelHorizontalLayout21.addWidget(self.hotelEditPushButton21)
        self.hotelIDLabel21 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelIDLabel21.setObjectName("hotelIDLabel21")
        self.hotelHorizontalLayout21.addWidget(self.hotelIDLabel21)
        self.hotelIDLineEdit21 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelIDLineEdit21.setObjectName("hotelIDLineEdit21")
        self.hotelHorizontalLayout21.addWidget(self.hotelIDLineEdit21)
        self.hotelVerticalLayout1.addLayout(self.hotelHorizontalLayout21)
        self.hotelHorizontalLayout22 = QtWidgets.QHBoxLayout()
        self.hotelHorizontalLayout22.setObjectName("hotelHorizontalLayout22")
        self.hotelNameLabel22 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelNameLabel22.setObjectName("hotelNameLabel22")
        self.hotelHorizontalLayout22.addWidget(self.hotelNameLabel22)
        self.hotelNameLineEdit22 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelNameLineEdit22.setObjectName("hotelNameLineEdit22")
        self.hotelHorizontalLayout22.addWidget(self.hotelNameLineEdit22)
        self.hotelLocIDLabel22 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelLocIDLabel22.setObjectName("hotelLocIDLabel22")
        self.hotelHorizontalLayout22.addWidget(self.hotelLocIDLabel22)
        self.hotelLocIDLineEdit22 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelLocIDLineEdit22.setObjectName("hotelLocIDLineEdit22")
        self.hotelHorizontalLayout22.addWidget(self.hotelLocIDLineEdit22)
        self.hotelContactLabel22 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelContactLabel22.setObjectName("hotelContactLabel22")
        self.hotelHorizontalLayout22.addWidget(self.hotelContactLabel22)
        self.hotelContactLineEdit22 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelContactLineEdit22.setObjectName("hotelContactLineEdit22")
        self.hotelHorizontalLayout22.addWidget(self.hotelContactLineEdit22)
        self.hotelVerticalLayout1.addLayout(self.hotelHorizontalLayout22)
        self.hotelUpdatePushButton22 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hotelUpdatePushButton22.setObjectName("hotelUpdatePushButton22")
        self.hotelHorizontalLayout22.addWidget(self.hotelUpdatePushButton22)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hotelVerticalLayout1.addItem(spacerItem1)
        self.hotelAddPushButton2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hotelAddPushButton2.setObjectName("hotelAddPushButton2")
        self.hotelVerticalLayout1.addWidget(self.hotelAddPushButton2)
        self.hotelHorizontalLayout23 = QtWidgets.QHBoxLayout()
        self.hotelHorizontalLayout23.setObjectName("hotelHorizontalLayout23")
        self.hotelNameLabel23 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelNameLabel23.setObjectName("hotelNameLabel23")
        self.hotelHorizontalLayout23.addWidget(self.hotelNameLabel23)
        self.hotelNameLineEdit23 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelNameLineEdit23.setObjectName("hotelNameLineEdit23")
        self.hotelHorizontalLayout23.addWidget(self.hotelNameLineEdit23)
        self.hotelLocIDLabel23 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelLocIDLabel23.setObjectName("hotelLocIDLabel23")
        self.hotelHorizontalLayout23.addWidget(self.hotelLocIDLabel23)
        self.hotelLocIDLineEdit23 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelLocIDLineEdit23.setObjectName("hotelLocIDLineEdit23")
        self.hotelHorizontalLayout23.addWidget(self.hotelLocIDLineEdit23)
        self.hotelContactLabel23 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelContactLabel23.setObjectName("hotelContactLabel23")
        self.hotelHorizontalLayout23.addWidget(self.hotelContactLabel23)
        self.hotelContactLineEdit23 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelContactLineEdit23.setObjectName("hotelContactLineEdit23")
        self.hotelHorizontalLayout23.addWidget(self.hotelContactLineEdit23)
        self.hotelGoPushButton23 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hotelGoPushButton23.setObjectName("hotelGoPushButton23")
        self.hotelHorizontalLayout23.addWidget(self.hotelGoPushButton23)
        self.hotelVerticalLayout1.addLayout(self.hotelHorizontalLayout23)
        self.hotelLogoLabel3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelLogoLabel3.setAlignment(QtCore.Qt.AlignCenter)
        self.hotelLogoLabel3.setObjectName("hotelLogoLabel3")
        self.hotelVerticalLayout1.addWidget(self.hotelLogoLabel3)
        self.hotelHorizontalLayout31 = QtWidgets.QHBoxLayout()
        self.hotelHorizontalLayout31.setObjectName("hotelHorizontalLayout31")
        self.hotelEditPushButton31 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hotelEditPushButton31.setObjectName("hotelEditPushButton31")
        self.hotelHorizontalLayout31.addWidget(self.hotelEditPushButton31)
        self.hotelIDLabel31 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelIDLabel31.setObjectName("hotelIDLabel31")
        self.hotelHorizontalLayout31.addWidget(self.hotelIDLabel31)
        self.hotelIDLineEdit31 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelIDLineEdit31.setObjectName("hotelIDLineEdit31")
        self.hotelHorizontalLayout31.addWidget(self.hotelIDLineEdit31)
        self.hotelVerticalLayout1.addLayout(self.hotelHorizontalLayout31)
        self.hotelHorizontalLayout32 = QtWidgets.QHBoxLayout()
        self.hotelHorizontalLayout32.setObjectName("hotelHorizontalLayout32")
        self.hotelNameLabel32 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelNameLabel32.setObjectName("hotelNameLabel32")
        self.hotelHorizontalLayout32.addWidget(self.hotelNameLabel32)
        self.hotelNameLineEdit32 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelNameLineEdit32.setObjectName("hotelNameLineEdit32")
        self.hotelHorizontalLayout32.addWidget(self.hotelNameLineEdit32)
        self.hotelLocIDLabel32 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelLocIDLabel32.setObjectName("hotelLocIDLabel32")
        self.hotelHorizontalLayout32.addWidget(self.hotelLocIDLabel32)
        self.hotelLocIDLineEdit32 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelLocIDLineEdit32.setObjectName("hotelLocIDLineEdit32")
        self.hotelHorizontalLayout32.addWidget(self.hotelLocIDLineEdit32)
        self.hotelContactLabel32 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelContactLabel32.setObjectName("hotelContactLabel32")
        self.hotelHorizontalLayout32.addWidget(self.hotelContactLabel32)
        self.hotelContactLineEdit32 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelContactLineEdit32.setObjectName("hotelContactLineEdit32")
        self.hotelHorizontalLayout32.addWidget(self.hotelContactLineEdit32)
        self.hotelVerticalLayout1.addLayout(self.hotelHorizontalLayout32)
        self.hotelBookedLabel32 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelBookedLabel32.setObjectName("hotelBookedLabel32")
        self.hotelHorizontalLayout32.addWidget(self.hotelBookedLabel32)
        self.hotelBookedLineEdit32 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelBookedLineEdit32.setObjectName("hotelBookedLineEdit32")
        self.hotelHorizontalLayout32.addWidget(self.hotelBookedLineEdit32)
        self.hotelUpdatePushButton32 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hotelUpdatePushButton32.setObjectName("hotelUpdatePushButton32")
        self.hotelHorizontalLayout32.addWidget(self.hotelUpdatePushButton32)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hotelVerticalLayout1.addItem(spacerItem2)
        self.hotelAddPushButton3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hotelAddPushButton3.setObjectName("hotelAddPushButton3")
        self.hotelVerticalLayout1.addWidget(self.hotelAddPushButton3)
        self.hotelHorizontalLayout33 = QtWidgets.QHBoxLayout()
        self.hotelHorizontalLayout33.setObjectName("hotelHorizontalLayout33")
        self.hotelNameLabel33 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelNameLabel33.setObjectName("hotelNameLabel33")
        self.hotelHorizontalLayout33.addWidget(self.hotelNameLabel33)
        self.hotelNameLineEdit33 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelNameLineEdit33.setObjectName("hotelNameLineEdit33")
        self.hotelHorizontalLayout33.addWidget(self.hotelNameLineEdit33)
        self.hotelLocIDLabel33 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelLocIDLabel33.setObjectName("hotelLocIDLabel33")
        self.hotelHorizontalLayout33.addWidget(self.hotelLocIDLabel33)
        self.hotelLocIDLineEdit33 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelLocIDLineEdit33.setObjectName("hotelLocIDLineEdit33")
        self.hotelHorizontalLayout33.addWidget(self.hotelLocIDLineEdit33)
        self.hotelContactLabel33 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelContactLabel33.setObjectName("hotelContactLabel33")
        self.hotelHorizontalLayout33.addWidget(self.hotelContactLabel33)
        self.hotelContactLineEdit33 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelContactLineEdit33.setObjectName("hotelContactLineEdit33")
        self.hotelHorizontalLayout33.addWidget(self.hotelContactLineEdit33)
        self.hotelBookedLabel33 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hotelBookedLabel33.setObjectName("hotelBookedLabel33")
        self.hotelHorizontalLayout33.addWidget(self.hotelBookedLabel33)
        self.hotelBookedLineEdit33 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hotelBookedLineEdit33.setObjectName("hotelBookedLineEdit33")
        self.hotelHorizontalLayout33.addWidget(self.hotelBookedLineEdit33)
        self.hotelGoPushButton33 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hotelGoPushButton33.setObjectName("hotelGoPushButton33")
        self.hotelHorizontalLayout33.addWidget(self.hotelGoPushButton33)
        self.hotelVerticalLayout1.addLayout(self.hotelHorizontalLayout33)
        self.hotelEditPushButton11.clicked.connect(self.func1)
        self.hotelEditPushButton21.clicked.connect(self.func4)
        self.hotelEditPushButton31.clicked.connect(self.func7)
        self.hotelUpdatePushButton12.clicked.connect(self.func2)
        self.hotelUpdatePushButton22.clicked.connect(self.func5)
        self.hotelUpdatePushButton32.clicked.connect(self.func8)
        self.hotelGoPushButton13.clicked.connect(self.func3)
        self.hotelGoPushButton23.clicked.connect(self.func6)
        self.hotelGoPushButton33.clicked.connect(self.func9)
        self.adminchoosemodecentralwidget = QtWidgets.QWidget(MainWindow)
        self.adminchoosemodecentralwidget.setObjectName("adminchoosemodecentralwidget")
        self.adminCustomerPushButton = QtWidgets.QPushButton(self.adminchoosemodecentralwidget)
        self.adminCustomerPushButton.setGeometry(QtCore.QRect(0, 260, 133, 80))
        self.adminCustomerPushButton.setObjectName("adminCustomerPushButton")
        self.adminHotelPushButton = QtWidgets.QPushButton(self.adminchoosemodecentralwidget)
        self.adminHotelPushButton.setGeometry(QtCore.QRect(133, 260, 133, 80))
        self.adminHotelPushButton.setObjectName("adminHotelPushButton")
        self.adminAttractionsPushButton = QtWidgets.QPushButton(self.adminchoosemodecentralwidget)
        self.adminAttractionsPushButton.setGeometry(QtCore.QRect(533, 260, 133, 80))
        self.adminAttractionsPushButton.setObjectName("adminAttractionsPushButton")
        self.adminMoviesPushButton = QtWidgets.QPushButton(self.adminchoosemodecentralwidget)
        self.adminMoviesPushButton.setGeometry(QtCore.QRect(400, 260, 133, 80))
        self.adminMoviesPushButton.setObjectName("adminMoviesPushButton")
        self.adminAirlinesPushButton = QtWidgets.QPushButton(self.adminchoosemodecentralwidget)
        self.adminAirlinesPushButton.setGeometry(QtCore.QRect(267, 260, 133, 80))
        self.adminAirlinesPushButton.setObjectName("adminAirlinesPushButton")

        ##flight edits
        self.adminAirlinesPushButton.clicked.connect(self.runAirlineAdminMode)

        ##flight edits end
        self.adminRestaurantsPushButton = QtWidgets.QPushButton(self.adminchoosemodecentralwidget)
        self.adminRestaurantsPushButton.setGeometry(QtCore.QRect(667, 260, 133, 80))
        self.adminRestaurantsPushButton.setObjectName("adminRestaurantsPushButton")
        self.adminChooseModeLabell = QtWidgets.QLabel(self.adminchoosemodecentralwidget)
        self.adminChooseModeLabell.setGeometry(QtCore.QRect(275, 100, 250, 100))
        font = QtGui.QFont()
        font.setFamily("KacstOffice")
        font.setPointSize(22)
        self.adminChooseModeLabell.setFont(font)
        self.adminChooseModeLabell.setAutoFillBackground(False)
        self.adminChooseModeLabell.setAlignment(QtCore.Qt.AlignCenter)
        self.adminChooseModeLabell.setObjectName("adminChooseModeLabell")
        self.adminHotelPushButton.clicked.connect(self.hoteledit)
        self.adminCustomerPushButton.clicked.connect(self.customeredit)
        self.adminAttractionsPushButton.clicked.connect(self.attractionEdit)
        self.adminRestaurantsPushButton.clicked.connect(self.restaurantEdit)
        self.adminMoviesPushButton.clicked.connect(self.movieEdit)
        self.customereditcentralwidget = QtWidgets.QWidget(MainWindow)
        self.customereditcentralwidget.setObjectName("customereditcentralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.customereditcentralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 120, 800, 250))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.customerVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.customerVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.customerVerticalLayout.setObjectName("customerVerticalLayout")
        self.customerLogoLabel1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.customerLogoLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.customerLogoLabel1.setObjectName("customerLogoLabel1")
        self.customerVerticalLayout.addWidget(self.customerLogoLabel1)
        self.customerHorizontalLayout1 = QtWidgets.QHBoxLayout()
        self.customerHorizontalLayout1.setObjectName("customerHorizontalLayout1")
        self.customerEditPushButton1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.customerEditPushButton1.setObjectName("customerEditPushButton1")
        self.customerHorizontalLayout1.addWidget(self.customerEditPushButton1)
        self.customerIDLabel1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.customerIDLabel1.setObjectName("customerIDLabel1")
        self.customerHorizontalLayout1.addWidget(self.customerIDLabel1)
        self.customerIDLineEdit1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.customerIDLineEdit1.setObjectName("customerIDLineEdit1")
        self.customerHorizontalLayout1.addWidget(self.customerIDLineEdit1)
        self.customerVerticalLayout.addLayout(self.customerHorizontalLayout1)
        self.customerHorizontalLayout2 = QtWidgets.QHBoxLayout()
        self.customerHorizontalLayout2.setObjectName("customerHorizontalLayout2")
        self.customerFirstNameLabel2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.customerFirstNameLabel2.setObjectName("customerFirstNameLabel2")
        self.customerHorizontalLayout2.addWidget(self.customerFirstNameLabel2)
        self.customerFirstNameLineEdit2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.customerFirstNameLineEdit2.setObjectName("customerFirstNameLineEdit2")
        self.customerHorizontalLayout2.addWidget(self.customerFirstNameLineEdit2)
        self.customerLastNameLabel2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.customerLastNameLabel2.setObjectName("customerLastNameLabel2")
        self.customerHorizontalLayout2.addWidget(self.customerLastNameLabel2)
        self.customerLastNameLineEdit2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.customerLastNameLineEdit2.setObjectName("customerLastNameLineEdit2")
        self.customerHorizontalLayout2.addWidget(self.customerLastNameLineEdit2)
        self.customerContactLabel2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.customerContactLabel2.setObjectName("customerContactLabel2")
        self.customerHorizontalLayout2.addWidget(self.customerContactLabel2)
        self.customerContactLineEdit2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.customerContactLineEdit2.setObjectName("customerContactLineEdit2")
        self.customerHorizontalLayout2.addWidget(self.customerContactLineEdit2)
        self.customerGenderLabel2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.customerGenderLabel2.setObjectName("customerGenderLabel2")
        self.customerHorizontalLayout2.addWidget(self.customerGenderLabel2)
        self.customerGenderLineEdit2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.customerGenderLineEdit2.setObjectName("customerGenderLineEdit2")
        self.customerHorizontalLayout2.addWidget(self.customerGenderLineEdit2)
        self.customerBalanceLabel2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.customerBalanceLabel2.setObjectName("customerBalanceLabel2")
        self.customerHorizontalLayout2.addWidget(self.customerBalanceLabel2)
        self.customerBalanceLineEdit2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.customerBalanceLineEdit2.setObjectName("customerBalanceLineEdit2")
        self.customerHorizontalLayout2.addWidget(self.customerBalanceLineEdit2)
        self.customerUpdatePushButton2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.customerUpdatePushButton2.setObjectName("customerUpdatePushButton2")
        self.customerHorizontalLayout2.addWidget(self.customerUpdatePushButton2)
        self.customerVerticalLayout.addLayout(self.customerHorizontalLayout2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.customerVerticalLayout.addItem(spacerItem)
        self.customerAddPushButton1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.customerAddPushButton1.setObjectName("customerAddPushButton1")
        self.customerVerticalLayout.addWidget(self.customerAddPushButton1)
        self.customerHorizontalLayout3 = QtWidgets.QHBoxLayout()
        self.customerHorizontalLayout3.setObjectName("customerHorizontalLayout3")
        self.customerFirstNameLabel3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.customerFirstNameLabel3.setObjectName("customerFirstNameLabel3")
        self.customerHorizontalLayout3.addWidget(self.customerFirstNameLabel3)
        self.customerFirstNameLineEdit3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.customerFirstNameLineEdit3.setObjectName("customerFirstNameLineEdit3")
        self.customerHorizontalLayout3.addWidget(self.customerFirstNameLineEdit3)
        self.customerLastNameLabel3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.customerLastNameLabel3.setObjectName("customerLastNameLabel3")
        self.customerHorizontalLayout3.addWidget(self.customerLastNameLabel3)
        self.customerLastNameLineEdit3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.customerLastNameLineEdit3.setObjectName("customerLastNameLineEdit3")
        self.customerHorizontalLayout3.addWidget(self.customerLastNameLineEdit3)
        self.customerContactLabel3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.customerContactLabel3.setObjectName("customerContactLabel3")
        self.customerHorizontalLayout3.addWidget(self.customerContactLabel3)
        self.customerContactLineEdit3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.customerContactLineEdit3.setObjectName("customerContactLineEdit3")
        self.customerHorizontalLayout3.addWidget(self.customerContactLineEdit3)
        self.customerGenderLabel3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.customerGenderLabel3.setObjectName("customerGenderLabel3")
        self.customerHorizontalLayout3.addWidget(self.customerGenderLabel3)
        self.customerGenderLineEdit3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.customerGenderLineEdit3.setObjectName("customerGenderLineEdit3")
        self.customerHorizontalLayout3.addWidget(self.customerGenderLineEdit3)
        self.customerBalanceLabel3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.customerBalanceLabel3.setObjectName("customerBalanceLabel3")
        self.customerHorizontalLayout3.addWidget(self.customerBalanceLabel3)
        self.customerBalanceLineEdit3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.customerBalanceLineEdit3.setObjectName("customerBalanceLineEdit3")
        self.customerHorizontalLayout3.addWidget(self.customerBalanceLineEdit3)
        self.customerGoPushButton3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.customerGoPushButton3.setObjectName("customerGoPushButton3")
        self.customerHorizontalLayout3.addWidget(self.customerGoPushButton3)
        self.customerVerticalLayout.addLayout(self.customerHorizontalLayout3)
        self.customerEditPushButton1.clicked.connect(self.func10)
        self.customerUpdatePushButton2.clicked.connect(self.func11)
        self.customerGoPushButton3.clicked.connect(self.func12)

        self.attractionsEditWidget = QtWidgets.QWidget(MainWindow)
        self.attractionsEditWidget.setObjectName("attractionsEditWidget")

        self.attractionLayout = QtWidgets.QVBoxLayout(self.attractionsEditWidget)
        self.attractionLayout.setContentsMargins(30, 30, 30, 30)
        self.attractionLayout.setObjectName("attractionLayout")

        # self.verticalLayoutWidgetAttr = QtWidgets.QWidget(self.attractionsEditWidget)
        # self.verticalLayoutWidgetAttr.setGeometry(QtCore.QRect(0, 120, 800, 250))
        # self.verticalLayoutWidgetAttr.setObjectName("verticalLayoutWidgetAttr")


        self.attractionLabel = QtWidgets.QLabel(self.attractionsEditWidget)
        self.attractionLabel.setObjectName("attractionLabel")
        self.attractionLayout.addWidget(self.attractionLabel)

        self.attractionIDLabel = QtWidgets.QLabel(self.attractionsEditWidget)
        self.attractionIDLabel.setObjectName("attractionIDLabel")
        self.attractionLayout.addWidget(self.attractionIDLabel)
        self.attractionIDInput = QtWidgets.QLineEdit(self.attractionsEditWidget)
        self.attractionIDInput.setObjectName("attractionIDInput")
        self.attractionLayout.addWidget(self.attractionIDInput)

        self.attractionNameLabel = QtWidgets.QLabel(self.attractionsEditWidget)
        self.attractionNameLabel.setObjectName("attractionNameLabel")
        self.attractionLayout.addWidget(self.attractionNameLabel)
        self.attractionNameInput = QtWidgets.QLineEdit(self.attractionsEditWidget)
        self.attractionNameInput.setObjectName("attractionNameInput")
        self.attractionLayout.addWidget(self.attractionNameInput)

        self.attractionSummaryLabel = QtWidgets.QLabel(self.attractionsEditWidget)
        self.attractionSummaryLabel.setObjectName("attractionSummaryLabel")
        self.attractionLayout.addWidget(self.attractionSummaryLabel)
        self.attractionSummaryInput = QtWidgets.QLineEdit(self.attractionsEditWidget)
        self.attractionSummaryInput.setObjectName("attractionSummaryInput")
        self.attractionLayout.addWidget(self.attractionSummaryInput)

        self.attractionDurationLabel = QtWidgets.QLabel(self.attractionsEditWidget)
        self.attractionDurationLabel.setObjectName("attractionDurationLabel")
        self.attractionLayout.addWidget(self.attractionDurationLabel)
        self.attractionDurationInput = QtWidgets.QLineEdit(self.attractionsEditWidget)
        self.attractionDurationInput.setObjectName("attractionDurationInput")
        self.attractionLayout.addWidget(self.attractionDurationInput)

        self.attractionStartLabel = QtWidgets.QLabel(self.attractionsEditWidget)
        self.attractionStartLabel.setObjectName("attractionStartLabel")
        self.attractionLayout.addWidget(self.attractionStartLabel)
        self.attractionStartInput = QtWidgets.QLineEdit(self.attractionsEditWidget)
        self.attractionStartInput.setObjectName("attractionStartInput")
        self.attractionLayout.addWidget(self.attractionStartInput)

        self.attractionCostLabel = QtWidgets.QLabel(self.attractionsEditWidget)
        self.attractionCostLabel.setObjectName("attractionCostLabel")
        self.attractionLayout.addWidget(self.attractionCostLabel)
        self.attractionCostInput = QtWidgets.QLineEdit(self.attractionsEditWidget)
        self.attractionCostInput.setObjectName("attractionCostInput")
        self.attractionLayout.addWidget(self.attractionCostInput)

        self.attractionTypeLabel = QtWidgets.QLabel(self.attractionsEditWidget)
        self.attractionTypeLabel.setObjectName("attractionTypeLabel")
        self.attractionLayout.addWidget(self.attractionTypeLabel)
        self.attractionTypeInput = QtWidgets.QLineEdit(self.attractionsEditWidget)
        self.attractionTypeInput.setObjectName("attractionTypeInput")
        self.attractionLayout.addWidget(self.attractionTypeInput)

        spacerItem = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.attractionLayout.addItem(spacerItem)

        # self.attractionUpdateLabel = QtWidgets.QLabel(self.attractionsEditWidget)
        # self.attractionUpdateLabel.setObjectName("attractionUpdateLabel")
        # self.attractionLayout.addWidget(self.attractionUpdateLabel)
        self.attractionUpdateButton = QtWidgets.QPushButton(self.attractionsEditWidget)
        self.attractionUpdateButton.setObjectName("attractionUpdateButton")
        self.attractionLayout.addWidget(self.attractionUpdateButton)

        # self.attractionAddLabel = QtWidgets.QLabel(self.attractionsEditWidget)
        # self.attractionAddLabel.setObjectName("attractionAddLabel")
        # self.attractionLayout.addWidget(self.attractionAddLabel)
        self.attractionAddButton = QtWidgets.QPushButton(self.attractionsEditWidget)
        self.attractionAddButton.setObjectName("attractionAddButton")
        self.attractionLayout.addWidget(self.attractionAddButton)

        self.attractionUpdateButton.clicked.connect(self.func007update)
        self.attractionAddButton.clicked.connect(self.func007add)

        self.restaurantEditWidget = QtWidgets.QWidget(MainWindow)
        self.restaurantEditWidget.setObjectName("restaurantEditWidget")

        self.restaurantLayout = QtWidgets.QVBoxLayout(self.restaurantEditWidget)
        self.restaurantLayout.setContentsMargins(30, 30, 30, 30)
        self.restaurantLayout.setObjectName("restaurantLayout")

        self.restaurantLabel = QtWidgets.QLabel(self.restaurantEditWidget)
        self.restaurantLabel.setObjectName("restaurantLabel")
        self.restaurantLayout.addWidget(self.restaurantLabel)

        self.restaurantIDLabel = QtWidgets.QLabel(self.restaurantEditWidget)
        self.restaurantIDLabel.setObjectName("restaurantIDLabel")
        self.restaurantLayout.addWidget(self.restaurantIDLabel)
        self.restaurantIDInput = QtWidgets.QLineEdit(self.restaurantEditWidget)
        self.restaurantIDInput.setObjectName("restaurantIDInput")
        self.restaurantLayout.addWidget(self.restaurantIDInput)

        self.restaurantNameLabel = QtWidgets.QLabel(self.restaurantEditWidget)
        self.restaurantNameLabel.setObjectName("restaurantNameLabel")
        self.restaurantLayout.addWidget(self.restaurantNameLabel)
        self.restaurantNameInput = QtWidgets.QLineEdit(self.restaurantEditWidget)
        self.restaurantNameInput.setObjectName("restaurantNameInput")
        self.restaurantLayout.addWidget(self.restaurantNameInput)

        self.restaurantCostLabel = QtWidgets.QLabel(self.restaurantEditWidget)
        self.restaurantCostLabel.setObjectName("restaurantCostLabel")
        self.restaurantLayout.addWidget(self.restaurantCostLabel)
        self.restaurantCostInput = QtWidgets.QLineEdit(self.restaurantEditWidget)
        self.restaurantCostInput.setObjectName("restaurantCostInput")
        self.restaurantLayout.addWidget(self.restaurantCostInput)

        self.restaurantCategoryLabel = QtWidgets.QLabel(self.restaurantEditWidget)
        self.restaurantCategoryLabel.setObjectName("restaurantCategoryLabel")
        self.restaurantLayout.addWidget(self.restaurantCategoryLabel)
        self.restaurantCategoryInput = QtWidgets.QLineEdit(self.restaurantEditWidget)
        self.restaurantCategoryInput.setObjectName("restaurantCategoryInput")
        self.restaurantLayout.addWidget(self.restaurantCategoryInput)

        self.restaurantLikesLabel = QtWidgets.QLabel(self.restaurantEditWidget)
        self.restaurantLikesLabel.setObjectName("restaurantLikesLabel")
        self.restaurantLayout.addWidget(self.restaurantLikesLabel)
        self.restaurantLikesInput = QtWidgets.QLineEdit(self.restaurantEditWidget)
        self.restaurantLikesInput.setObjectName("restaurantLikesInput")
        self.restaurantLayout.addWidget(self.restaurantLikesInput)

        self.restaurantLatLabel = QtWidgets.QLabel(self.restaurantEditWidget)
        self.restaurantLatLabel.setObjectName("restaurantLatLabel")
        self.restaurantLayout.addWidget(self.restaurantLatLabel)
        self.restaurantLatInput = QtWidgets.QLineEdit(self.restaurantEditWidget)
        self.restaurantLatInput.setObjectName("restaurantLatInput")
        self.restaurantLayout.addWidget(self.restaurantLatInput)

        self.restaurantLongLabel = QtWidgets.QLabel(self.restaurantEditWidget)
        self.restaurantLongLabel.setObjectName("restaurantLongLabel")
        self.restaurantLayout.addWidget(self.restaurantLongLabel)
        self.restaurantLongInput = QtWidgets.QLineEdit(self.restaurantEditWidget)
        self.restaurantLongInput.setObjectName("restaurantLongInput")
        self.restaurantLayout.addWidget(self.restaurantLongInput)

        self.restaurantNeighbourhoodLabel = QtWidgets.QLabel(self.restaurantEditWidget)
        self.restaurantNeighbourhoodLabel.setObjectName("restaurantNeighbourhoodLabel")
        self.restaurantLayout.addWidget(self.restaurantNeighbourhoodLabel)
        self.restaurantNeighbourhoodInput = QtWidgets.QLineEdit(self.restaurantEditWidget)
        self.restaurantNeighbourhoodInput.setObjectName("restaurantNeighbourhoodInput")
        self.restaurantLayout.addWidget(self.restaurantNeighbourhoodInput)


        spacerItem = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.restaurantLayout.addItem(spacerItem)

        self.restaurantUpdateButton = QtWidgets.QPushButton(self.restaurantEditWidget)
        self.restaurantUpdateButton.setObjectName("restaurantUpdateButton")
        self.restaurantLayout.addWidget(self.restaurantUpdateButton)

        # self.attractionAddLabel = QtWidgets.QLabel(self.attractionsEditWidget)
        # self.attractionAddLabel.setObjectName("attractionAddLabel")
        # self.attractionLayout.addWidget(self.attractionAddLabel)
        self.restaurantAddButton = QtWidgets.QPushButton(self.restaurantEditWidget)
        self.restaurantAddButton.setObjectName("restaurantAddButton")
        self.restaurantLayout.addWidget(self.restaurantAddButton)


        self.restaurantUpdateButton.clicked.connect(self.func009update)
        self.restaurantAddButton.clicked.connect(self.func009add)


        self.Stack.addWidget(self.logincentralwidget)
        self.Stack.addWidget(self.centralwidget1)
        self.Stack.addWidget(self.reviewcentralwidget)
        self.Stack.addWidget(self.overviewcentralwidget)
        self.Stack.addWidget(self.bookcentralwidget)
        self.Stack.addWidget(self.adminchoosemodecentralwidget)
        self.Stack.addWidget(self.hoteleditcentralwidget)
        self.Stack.addWidget(self.customereditcentralwidget)
        self.Stack.addWidget(self.attractionsEditWidget)
        self.Stack.addWidget(self.restaurantEditWidget)

        ####flight edits
        self.mybackendFlight = backendFlight()
        aAM = self.airlineAdminMode(self)

        #######flight edits end


        MainWindow.setCentralWidget(self.Stack)




        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuMode = QtWidgets.QMenu(self.menubar)
        self.menuMode.setObjectName("menuMode")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionChangeMode = QtWidgets.QAction(MainWindow)
        self.actionChangeMode.setObjectName("actionChangeMode")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMode.addAction(self.actionChangeMode)
        self.menuMode.addAction(self.actionExit)
        self.menubar.addAction(self.menuMode.menuAction())
        self.actionChangeMode.triggered.connect(self.changemodeclick)
        self.actionExit.triggered.connect(self.exitclick)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #############################################

        self.mybackendHotel = backendHotel()
        self.mybackendAttraction = backendAttraction()
        self.mybackendRestaurant = backendRestaurant()

        self.sortButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)

        # UPDATED. DYNAMIC SORT MENU
        self.hotelButton.clicked.connect(self.bufferFuncHotel)
        self.attractionButton.clicked.connect(self.sortMenuItemsAttraction)
        self.RestaurantButton.clicked.connect(self.sortMenuItemsRestaurant)
        self.airlinesButton.clicked.connect(self.airlineInitializer)
        self.movieButton.clicked.connect(self.startMoviesDisplay) #############


    ######## Flights Part Starts Here ################

    class FlightWidget(QtWidgets.QWidget):
        def __init__(self, outer, parent=None):
            super(outer.FlightWidget, self).__init__(parent)
            self.outer = outer
            self.box = QtWidgets.QVBoxLayout()

            self.id = QtWidgets.QLabel()
            self.airline = QtWidgets.QLabel()
            self.airport = QtWidgets.QLabel()
            self.departure = QtWidgets.QLabel()
            self.arrival = QtWidgets.QLabel()
            self.duration = QtWidgets.QLabel()
            self.numseats = QtWidgets.QLabel()
            self.cost = QtWidgets.QLabel()
            self.bookbutton = QtWidgets.QPushButton()
            self.bookbutton.setText("Book Now")

            self.h1 = QtWidgets.QHBoxLayout()
            self.h1.addWidget(self.id)
            self.h1.addWidget(self.airline)
            self.box.addLayout(self.h1)
            self.box.addWidget(self.airport)
            self.h2 = QtWidgets.QHBoxLayout()
            self.h2.addWidget(self.departure)
            self.h2.addWidget(self.arrival)
            self.box.addLayout(self.h2)
            self.box.addWidget(self.duration)
            self.h3 = QtWidgets.QHBoxLayout()
            self.h3.addWidget(self.numseats)
            self.h3.addWidget(self.cost)
            self.box.addLayout(self.h3)
            self.box.addWidget(self.bookbutton)


            self.setLayout(self.box)

        def setTextOnAllLabel(self, flight):
            self.id.setText("Flight No : " + str(flight['id']))
            self.airline.setText("Airline : " + flight['airline'])
            self.airport.setText("Destination Airport: " + flight['airport'])
            self.departure.setText("Departure Time: " + str(flight['departure']))
            self.arrival.setText("Arrival Time: " + str(flight['arrival']))
            self.duration.setText("Flight Duration: " + str(flight['duration']))
            self.numseats.setText("Available Seats: " + str(flight['numseats']))
            self.cost.setText("Cost per seat: " + str(flight['avgCost']))
            self.bookbutton.clicked.connect(lambda : self.bookingWindow(flight['id'], flight['numseats']))


        def bookingWindow(self, flightNo, numSeats):

            def confirmBooking():
                def addBal():
                    self.outer.mybackendFlight.addBalance(int(self.outer.USER_ID), int(self.outer.BALANCE))
                    self.outer.BALANCE = str(int(self.outer.BALANCE) + 10000)
                    self.outer.balanceLabel.setText("Balance : " + self.outer.BALANCE)
                    window.reject()
                    return
                selectedSeats = spinbox.value()

                print("You attempted to book {} seats in Flight No: {}".format(selectedSeats, flightNo))
                seats = self.outer.mybackendFlight.bookSeats(flightNo, selectedSeats, int(self.outer.USER_ID), int(self.outer.BALANCE))
                if (seats[0]==-1):
                    label1 = QtWidgets.QLabel("Not enough balance !!!")
                    label.deleteLater()
                    layout.removeWidget(label)
                    spinbox.deleteLater()
                    layout.removeWidget(spinbox)
                    layout.addWidget(label)
                    submitButton.deleteLater()
                    layout.removeWidget(submitButton)
                    addBalBtn = QtWidgets.QPushButton("Add 10k Rupees")
                    addBalBtn.clicked.connect(addBal)
                    layout.addWidget(label1)
                    layout.addWidget(addBalBtn)
                else:
                    self.outer.BALANCE = str(seats[0])
                    self.outer.balanceLabel.setText("Balance : " + self.outer.BALANCE)
                    label1 = QtWidgets.QLabel("Your seat bumbers are as follows :")
                    label2 = QtWidgets.QLabel(str(seats[1:]))
                    label.deleteLater()
                    layout.removeWidget(label)
                    spinbox.deleteLater()
                    layout.removeWidget(spinbox)
                    layout.addWidget(label)
                    submitButton.deleteLater()
                    layout.removeWidget(submitButton)
                    layout.addWidget(label1)
                    layout.addWidget(label2)

            window = QtWidgets.QDialog()
            window.rejected.connect(lambda: self.outer.airlineInitializer())
            window.setObjectName("Confirm Booking")
            window.setWindowTitle("Confirm Booking")
            layout = QtWidgets.QVBoxLayout()
            label = QtWidgets.QLabel("Please select number of seats to be booked.")
            layout.addWidget(label)
            submitButton = QtWidgets.QPushButton("Submit")
            submitButton.setObjectName("Submit")
            submitButton.clicked.connect(lambda:confirmBooking())
            spinbox = QtWidgets.QSpinBox(window)
            spinbox.setMaximum(numSeats)
            spinbox.setMinimum(1)
            spinbox.valueChanged.connect(lambda : print(spinbox.value()))

            # print("Selected number of seats: ", selectedSeats)
            layout.addWidget(spinbox)
            layout.addWidget(submitButton)
            window.setLayout(layout)
            window.setModal(True)
            window.exec()

    class SearchBoxWidget(QtWidgets.QWidget):
        def __init__(self,outer, countrybox, citybox, searchbutton, parent=None):
            super(outer.SearchBoxWidget, self).__init__(parent)

            self.box = QtWidgets.QHBoxLayout()
            self.box.addWidget(countrybox)
            self.box.addWidget(citybox)
            self.box.addWidget(searchbutton)
            self.setLayout(self.box)


    class airlineAdminMode:
        def __init__(self, outer):
            outer.flightAdminWindow = QtWidgets.QWidget(outer.MainWindow)
            self.outer = outer
            mainVertLayout = QtWidgets.QVBoxLayout()

            ## add airline ##
            airlineAdder = QtWidgets.QVBoxLayout()
            airlineAdder.addWidget(QtWidgets.QLabel("Add Airline"))
            airlineAdderH = QtWidgets.QHBoxLayout()
            airlineAdder.addLayout(airlineAdderH)
            self.addAirlineName = QtWidgets.QLineEdit()
            self.addAirlineName.setPlaceholderText("Airline Name")
            self.addAirlineMail = QtWidgets.QLineEdit()
            self.addAirlineMail.setPlaceholderText("Airline Contact")

            self.airlineBtn = QtWidgets.QPushButton()
            self.airlineBtn.clicked.connect(lambda: self.addAirline())
            self.airlineBtn.setText('ADD')
            airlineAdderH.addWidget(self.addAirlineName)
            airlineAdderH.addWidget(self.addAirlineMail)
            airlineAdderH.addWidget(self.airlineBtn)

            ## add airport ##
            airportAdder = QtWidgets.QVBoxLayout()
            airportAdder.addWidget(QtWidgets.QLabel("Add Airport"))
            airportAdderH = QtWidgets.QHBoxLayout()
            airportAdder.addLayout(airportAdderH)
            self.addAirportName = QtWidgets.QLineEdit()
            self.addAirportName.setPlaceholderText("Airport Name")
            self.addAirportCountry = QtWidgets.QLineEdit()
            self.addAirportCountry.setPlaceholderText("Country Name")
            self.addAirportCity = QtWidgets.QLineEdit()
            self.addAirportCity.setPlaceholderText("City Name")
            airportBtn = QtWidgets.QPushButton()
            airportBtn.clicked.connect(lambda: self.addAirport())
            airportBtn.setText('ADD')
            airportAdderH.addWidget(self.addAirportName)
            airportAdderH.addWidget(self.addAirportCountry)
            airportAdderH.addWidget(self.addAirportCity)
            airportAdderH.addWidget(airportBtn)

            ## add flight ##
            flightAdder = QtWidgets.QVBoxLayout()
            flightAdder.addWidget(QtWidgets.QLabel("Add FLight"))
            flightAdderH = QtWidgets.QHBoxLayout()
            flightAdderH2 = QtWidgets.QHBoxLayout()

            self.addFlightAirline = QtWidgets.QComboBox()
            self.addFlightAirline.addItems(outer.mybackendFlight.getAirlines())
            self.addFlightAirport = QtWidgets.QComboBox()
            self.addFlightAirport.addItems(outer.mybackendFlight.getAllAirports())
            currTime = QtCore.QDateTime.currentDateTime()
            self.addFlightDeparture = QtWidgets.QDateTimeEdit(currTime)
            self.addFlightArrival = QtWidgets.QDateTimeEdit(currTime)
            self.addFlightDeparture.setMinimumDateTime(currTime)
            self.addFlightArrival.setMinimumDateTime(currTime)
            self.addFlightResult = QtWidgets.QLineEdit()
            self.addFlightResult.setReadOnly(True)
            addFlightBtn = QtWidgets.QPushButton()
            addFlightBtn.clicked.connect(lambda: self.addFlight())
            addFlightBtn.setText('ADD')
            flightAdderH.addWidget(self.addFlightAirline)
            flightAdderH.addWidget(self.addFlightAirport)
            flightAdderH2.addWidget(QtWidgets.QLabel("Departure Time: "))
            flightAdderH2.addWidget(self.addFlightDeparture)
            flightAdderH2.addWidget(QtWidgets.QLabel("Arrival Time: "))
            flightAdderH2.addWidget(self.addFlightArrival)
            flightAdderH2.addWidget(addFlightBtn)
            flightAdderH2.addWidget(QtWidgets.QLabel("Flight Id: "))
            flightAdderH2.addWidget(self.addFlightResult)

            flightAdder.addLayout(flightAdderH)
            flightAdder.addLayout(flightAdderH2)


            ## add tickets ##
            ticketAdder = QtWidgets.QVBoxLayout()
            ticketAdder.addWidget(QtWidgets.QLabel("Add Tickets"))
            ticketAdderH = QtWidgets.QHBoxLayout()
            self.addTicketFlightId = QtWidgets.QComboBox()
            self.addTicketFlightId.addItems(self.outer.mybackendFlight.getFlightIDs())
            val1 = QtGui.QIntValidator()
            val1.setBottom(1)
            self.addTicketFlightId.setValidator(val1)

            self.addTicketNumSeats = QtWidgets.QLineEdit()
            self.addTicketNumSeats.setValidator(QtGui.QIntValidator(1,500))
            self.addTicketNumSeats.setPlaceholderText("Number of Seats")
            self.addTicketPrice = QtWidgets.QLineEdit()
            self.addTicketPrice.setPlaceholderText("Ticket Price")
            self.addTicketPrice.setValidator(QtGui.QIntValidator(1, 100000))
            addTicketBtn = QtWidgets.QPushButton()
            addTicketBtn.clicked.connect(lambda: self.addTickets())
            addTicketBtn.setText("ADD")
            ticketAdderH.addWidget(QtWidgets.QLabel("Flight ID:"))
            ticketAdderH.addWidget(self.addTicketFlightId)
            ticketAdderH.addWidget(self.addTicketNumSeats)
            ticketAdderH.addWidget(self.addTicketPrice)
            ticketAdderH.addWidget(addTicketBtn)
            ticketAdder.addLayout(ticketAdderH)

            ## get passengers ##
            ## remove airline ##
            airlineRemover = QtWidgets.QVBoxLayout()
            airlineRemover.addWidget(QtWidgets.QLabel("Remove Airline"))
            airlineRemoverH = QtWidgets.QHBoxLayout()
            self.airlineRemoveName = QtWidgets.QComboBox()
            self.airlineRemoveName.addItems(self.outer.mybackendFlight.getAirlines())
            removeAirlineBtn = QtWidgets.QPushButton()
            removeAirlineBtn.setText("Remove")
            removeAirlineBtn.clicked.connect(lambda : self.removeAirline())
            airlineRemoverH.addWidget(self.airlineRemoveName)
            airlineRemoverH.addWidget(removeAirlineBtn)
            airlineRemover.addLayout(airlineRemoverH)

            ## remove flight ##
            flightRemover = QtWidgets.QVBoxLayout()
            flightRemover.addWidget(QtWidgets.QLabel("Remove Flight"))
            flightRemoverH = QtWidgets.QHBoxLayout()
            self.removeFlightId = QtWidgets.QComboBox()
            self.removeFlightId.addItems(self.outer.mybackendFlight.getFlightIDs())

            removeFlightBtn = QtWidgets.QPushButton()
            removeFlightBtn.setText("Remove")
            removeFlightBtn.clicked.connect(lambda : self.removeFlight())
            flightRemoverH.addWidget(QtWidgets.QLabel("Flight Id: "))
            flightRemoverH.addWidget(self.removeFlightId)
            flightRemoverH.addWidget(removeFlightBtn)
            flightRemover.addLayout(flightRemoverH)
            ##add all widgets
            mainVertLayout.addLayout(airlineAdder)
            mainVertLayout.addLayout(airportAdder)
            mainVertLayout.addLayout(flightAdder)
            mainVertLayout.addLayout(ticketAdder)
            mainVertLayout.addLayout(airlineRemover)
            mainVertLayout.addLayout(flightRemover)
            outer.Stack.addWidget(outer.flightAdminWindow)
            outer.flightAdminWindow.setLayout(mainVertLayout)
        def addAirline(self):
            #print("function called")
            name = self.addAirlineName.text()
            mail = self.addAirlineMail.text()
            if (len(name)==0 or len(mail)==0):
                choice = QtWidgets.QMessageBox.information(self.outer.flightAdminWindow, 'Empty Fields',"Fields cannot be Empty!",QtWidgets.QMessageBox.Ok)
                return
            self.outer.mybackendFlight.addAirline(name, mail)
            k = self.airlineRemoveName.count()
            while(k>0):
                self.airlineRemoveName.removeItem(0)
                self.addFlightAirline.removeItem(0)
                k-=1
            self.airlineRemoveName.addItems(self.outer.mybackendFlight.getAirlines())
            self.addFlightAirline.addItems(self.outer.mybackendFlight.getAirlines())

        def addAirport(self):
            name = self.addAirportName.text()
            country = self.addAirportCountry.text()
            city = self.addAirportCity.text()
            if (len(name)==0 or len(country)==0 or len(city)==0):
                choice = QtWidgets.QMessageBox.information(self.outer.flightAdminWindow, 'Empty Fields',"Fields cannot be Empty!",QtWidgets.QMessageBox.Ok)
                return
            if not(self.outer.mybackendFlight.validateAirport(name)):
                choice = QtWidgets.QMessageBox.information(self.outer.flightAdminWindow, 'Repeated Entry',"Airport Name cannot repeat!",QtWidgets.QMessageBox.Yes)
                return
            self.outer.mybackendFlight.addAirport(name, country, city)
            k = self.addFlightAirport.count()
            while(k>0):
                self.addFlightAirport.removeItem(0)
                k-=1
            self.addFlightAirport.addItems(self.outer.mybackendFlight.getAllAirports())

        def addFlight(self):
            airline = self.addFlightAirline.currentText()
            airport = self.addFlightAirport.currentText()
            departure = self.addFlightDeparture.dateTime().toPyDateTime()
            arrival = self.addFlightArrival.dateTime().toPyDateTime()
            if not(arrival > departure):
                choice = QtWidgets.QMessageBox.information(self.outer.flightAdminWindow, 'Wrong DateTime',"Arrival DateTime should be after Departure DateTime",QtWidgets.QMessageBox.Ok)
                return
            idx = self.outer.mybackendFlight.addFlight(airline, airport, departure, arrival)

            self.addFlightResult.setText(str(idx))
            k = self.addTicketFlightId.count()
            while(k>0):
                self.addTicketFlightId.removeItem(0)
                self.removeFlightId.removeItem(0)
                k-=1
            self.addTicketFlightId.addItems(self.outer.mybackendFlight.getFlightIDs())
            self.removeFlightId.addItems(self.outer.mybackendFlight.getFlightIDs())

        def addTickets(self):
            flightid = self.addTicketFlightId.currentText()
            numtickets = int(self.addTicketNumSeats.text()) if len(self.addTicketNumSeats.text())>0 else 0
            price = int(self.addTicketPrice.text()) if len(self.addTicketPrice.text())>0 else 0
            if not(numtickets>0 and price>0):
                choice = QtWidgets.QMessageBox.information(self.outer.flightAdminWindow, 'Non Positive Value',"Only Positive Values are Allowed",QtWidgets.QMessageBox.Ok)
                return

            self.outer.mybackendFlight.addTickets(int(flightid), numtickets, price)

        def removeFlight(self):
            id = int(self.removeFlightId.currentText())
            choice = QtWidgets.QMessageBox.information(self.outer.flightAdminWindow, 'Confirmaton',"Are you sure, you want to remove the chosen flight",QtWidgets.QMessageBox.Yes  |QtWidgets.QMessageBox.No)
            if (choice == 16384):
                self.outer.mybackendFlight.removeFlight(id)
            k = self.addTicketFlightId.count()
            while(k>0):
                self.addTicketFlightId.removeItem(0)
                self.removeFlightId.removeItem(0)
                k-=1
            self.addTicketFlightId.addItems(self.outer.mybackendFlight.getFlightIDs())
            self.removeFlightId.addItems(self.outer.mybackendFlight.getFlightIDs())

        def removeAirline(self):
            name = self.airlineRemoveName.currentText()
            choice = QtWidgets.QMessageBox.information(self.outer.flightAdminWindow, 'Confirmaton',"Are you sure, you want to remove the chosen airline",QtWidgets.QMessageBox.Yes  |QtWidgets.QMessageBox.No)
            if (choice == 16384):
                self.outer.mybackendFlight.removeAirline(name)
            k = self.airlineRemoveName.count()
            while(k>0):
                self.airlineRemoveName.removeItem(0)
                self.addFlightAirline.removeItem(0)
                k-=1
            self.airlineRemoveName.addItems(self.outer.mybackendFlight.getAirlines())
            self.addFlightAirline.addItems(self.outer.mybackendFlight.getAirlines())
            k = self.addTicketFlightId.count()
            while(k>0):
                self.addTicketFlightId.removeItem(0)
                self.removeFlightId.removeItem(0)
                k-=1
            self.addTicketFlightId.addItems(self.outer.mybackendFlight.getFlightIDs())
            self.removeFlightId.addItems(self.outer.mybackendFlight.getFlightIDs())



    def runAirlineAdminMode(self):
        self.Stack.setCurrentWidget(self.flightAdminWindow)
    def airlineInitializer(self):
        print("Hello")
        self.searchResults = []

        def sorter(flag):
            if (flag==0):
                self.searchResults = sorted(self.searchResults, key = lambda i : i['duration'])
            elif (flag == 1):
                self.searchResults = sorted(self.searchResults, key = lambda i : i['duration'], reverse = True)
            elif (flag==2):
                self.searchResults = sorted(self.searchResults, key = lambda i : i['departure'])
            elif (flag == 3):
                self.searchResults = sorted(self.searchResults, key = lambda i : i['departure'], reverse = True)
            elif (flag== 4):
                self.searchResults = sorted(self.searchResults, key = lambda i : i['arrival'])
            elif (flag == 5):
                self.searchResults = sorted(self.searchResults, key = lambda i : i['arrival'], reverse = True)
            viewResults()

        def sortMenuInitializer():
            print()
            sortMenu = QtWidgets.QMenu()


            durationAscAction = QtWidgets.QWidgetAction(sortMenu)
            self.durationAscButton = QtWidgets.QPushButton(self.centralwidget1)
            self.durationAscButton.setText("Duration Ascending")
            self.durationAscButton.clicked.connect(lambda : sorter(0))
            durationAscAction.setDefaultWidget(self.durationAscButton)

            durationDescAction = QtWidgets.QWidgetAction(sortMenu)
            self.durationDescButton = QtWidgets.QPushButton(self.centralwidget1)
            self.durationDescButton.setText("Duration Descending")
            self.durationDescButton.clicked.connect(lambda : sorter(1))
            durationDescAction.setDefaultWidget(self.durationDescButton)

            startTimeAscAction = QtWidgets.QWidgetAction(sortMenu)
            self.startTimeAscButton = QtWidgets.QPushButton(self.centralwidget1)
            self.startTimeAscButton.setText("Departure Time Ascending")
            self.startTimeAscButton.clicked.connect(lambda : sorter(2))
            startTimeAscAction.setDefaultWidget(self.startTimeAscButton)

            startTimeDescAction = QtWidgets.QWidgetAction(sortMenu)
            self.startTimeDescButton = QtWidgets.QPushButton(self.centralwidget1)
            self.startTimeDescButton.setText("Departure Time Descending")
            self.startTimeDescButton.clicked.connect(lambda : sorter(3))
            startTimeDescAction.setDefaultWidget(self.startTimeDescButton)

            arrivalAscAction = QtWidgets.QWidgetAction(sortMenu)
            self.arrivalAscButton = QtWidgets.QPushButton(self.centralwidget1)
            self.arrivalAscButton.setText("Arrival Time Ascending")
            self.arrivalAscButton.clicked.connect(lambda : sorter(4))
            arrivalAscAction.setDefaultWidget(self.arrivalAscButton)

            arrivalDescAction = QtWidgets.QWidgetAction(sortMenu)
            self.arrivalDescButton = QtWidgets.QPushButton(self.centralwidget1)
            self.arrivalDescButton.setText("Arrival Time Descending")
            self.arrivalDescButton.clicked.connect(lambda : sorter(5))
            arrivalDescAction.setDefaultWidget(self.arrivalDescButton)


            sortMenu.addSeparator()
            sortMenu.addAction(durationAscAction)
            sortMenu.addAction(durationDescAction)
            sortMenu.addSeparator()
            sortMenu.addAction(startTimeAscAction)
            sortMenu.addAction(startTimeDescAction)
            sortMenu.addSeparator()
            sortMenu.addAction(arrivalAscAction)
            sortMenu.addAction(arrivalDescAction)

            self.sortButton.setMenu(sortMenu)

        def countryOptions():
            countryBox.addItem("Country")
            self.mybackendFlight.getAirport()
            countryBox.addItems(self.mybackendFlight.countries)

        def cityOptions():
            self.mybackendFlight.getAirport()
            k = cityBox.count()
            while(k>0):
                cityBox.removeItem(0)
                k-=1
            cityBox.addItems(self.mybackendFlight.cities)

        def printCountry():
            print(countryBox.currentText())
            if (countryBox.currentText() != "Country"):
                k = cityBox.count()
                while(k>0):
                    cityBox.removeItem(0)
                    k-=1
                cityBox.addItems(self.mybackendFlight.city4country(countryBox.currentText()))
            else:
                cityOptions()

        def viewResults():
            print(self.searchResults)
            self.listWidget.clear()
            sb = self.SearchBoxWidget(self, countryBox, cityBox, searchButton)
            listWidgetItem = QtWidgets.QListWidgetItem(self.listWidget)
            listWidgetItem.setSizeHint(sb.sizeHint())
            self.listWidget.addItem(listWidgetItem)
            self.listWidget.setItemWidget(listWidgetItem, sb)

            for i in self.searchResults:
                print(i)
                fw = self.FlightWidget(self)
                fw.setTextOnAllLabel(i)
                listWidgetItem = QtWidgets.QListWidgetItem(self.listWidget)
                listWidgetItem.setSizeHint(fw.sizeHint())
                self.listWidget.addItem(listWidgetItem)
                self.listWidget.setItemWidget(listWidgetItem, fw)


        def pushOutput():

            self.searchResults = self.mybackendFlight.getFlights(cityBox.currentText())
            print(self.searchResults)
            viewResults()

        def displayFlightItems():
            self.listWidget.clear()


            #searchButton.setGeometry(QtCore.QRect(580, 70, 161, 61))
            searchButton.setStyleSheet("border-right-color: rgb(239, 41, 41);\n")
            searchButton.setObjectName("pushButton")
            searchButton.clicked.connect(pushOutput)
            ###########################
            #countryBox.setGeometry(QtCore.QRect(35, 60, 131, 41))
            countryBox.setStyleSheet("background-color: rgb(233, 185, 110);")
            countryBox.setObjectName("comboBox")
            countryBox.currentTextChanged.connect(printCountry)

            ###########################

            #cityBox = QtWidgets.QComboBox()
            #cityBox.setGeometry(QtCore.QRect(185, 60, 131, 41))
            cityBox.setStyleSheet("background-color: rgb(233, 185, 110);")
            cityBox.setObjectName("comboBox")
            countryOptions()
            cityOptions()
            listWidgetItem = QtWidgets.QListWidgetItem(self.listWidget)
            listWidgetItem.setSizeHint(sb.sizeHint())
            self.listWidget.addItem(listWidgetItem)
            self.listWidget.setItemWidget(listWidgetItem, sb)


        ##########################

        sortMenuInitializer()
        searchButton = QtWidgets.QPushButton()
        searchButton.setText("Search")
        countryBox = QtWidgets.QComboBox()
        cityBox = QtWidgets.QComboBox()
        try:
            self.listWidget.itemClicked.disconnect()
        except:
            pass
        #self.listWidget.itemClicked.connect(lambda: print())
        sb = self.SearchBoxWidget(self,countryBox, cityBox, searchButton)
        displayFlightItems()
    ##### flight ends here ######


    def customeredit(self):
        self.Stack.setCurrentWidget(self.customereditcentralwidget)

    def attractionEdit(self):
        self.Stack.setCurrentWidget(self.attractionsEditWidget)

    def restaurantEdit(self):
        self.Stack.setCurrentWidget(self.restaurantEditWidget)

    def movieEdit(self):
        adminmovieRun(self)

    def exitclick(self):
        os._exit(1)
    def changemodeclick(self):
        self.Stack.setCurrentWidget(self.logincentralwidget)
    def func1(self):
        hid = self.hotelIDLineEdit11.text()
        lower,upper = self.mybackend.gethotelbounds()
        if(len(hid)==0 or not hid.isdigit() or int(hid)<lower or int(hid)>upper):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Inorrect Input',"Enter a valid ID(int only)",QtWidgets.QMessageBox.Ok)
            self.hotelIDLineEdit11.setText("")
        else:
            a,b,c = self.mybackend.getinfohotel(hid)
            self.hotelNameLineEdit12.setText(a)
            self.hotelLocIDLineEdit12.setText(b)
            self.hotelContactLineEdit12.setText(c)
    def func2(self):
        hid = self.hotelIDLineEdit11.text()
        a = self.hotelNameLineEdit12.text()
        b = self.hotelLocIDLineEdit12.text()
        c = self.hotelContactLineEdit12.text()
        lower,upper = self.mybackend.getlocationbounds()
        if(len(a)==0 or len(b)==0 or len(c)==0 or len(hid)==0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Empty Fields',"Fields cannot be Empty!",QtWidgets.QMessageBox.Ok)
        elif(a.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Name cannot be a number!",QtWidgets.QMessageBox.Ok)
        elif(int(b)<lower or int(b)>upper):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Loc_id out of Range",QtWidgets.QMessageBox.Ok)
        elif(not c.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"contact must be a number",QtWidgets.QMessageBox.Ok)
        elif(len(c)!=10):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"contact must be of 10 digits",QtWidgets.QMessageBox.Ok)
        else:
            self.mybackend.updatehotelinfo(hid,a,b,c)
    def func3(self):
        a = self.hotelNameLineEdit13.text()
        b = self.hotelLocIDLineEdit13.text()
        c = self.hotelContactLineEdit13.text()
        lower,upper = self.mybackend.getlocationbounds()
        if(len(a)==0 or len(b)==0 or len(c)==0 ):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Empty Fields',"Fields cannot be Empty!",QtWidgets.QMessageBox.Ok)
        elif(a.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Name cannot be a number!",QtWidgets.QMessageBox.Ok)
        elif(int(b)<lower or int(b)>upper):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Loc_id out of Range",QtWidgets.QMessageBox.Ok)
        elif(not c.isdigit):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"contact must be a number",QtWidgets.QMessageBox.Ok)
        elif(len(c)!=10):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"contact must be of 10 digits",QtWidgets.QMessageBox.Ok)
        else:
            self.mybackend.addintohotel(a,b,c)
            self.hotelNameLineEdit13.setText("")
            self.hotelLocIDLineEdit13.setText("")
            self.hotelContactLineEdit13.setText("")
    def func4(self):
        lid = self.hotelIDLineEdit21.text()
        lower,upper = self.mybackend.getlocationbounds()
        if(len(lid)==0 or not lid.isdigit() or int(lid)<lower or int(lid)>upper):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Enter a valid ID(int only)",QtWidgets.QMessageBox.Ok)
            self.hotelIDLineEdit21.setText("")
        else:
            a,b,c = self.mybackend.getinfolocation(lid)
            self.hotelNameLineEdit22.setText(a)
            self.hotelLocIDLineEdit22.setText(b)
            self.hotelContactLineEdit22.setText(c)
    def func5(self):
        lid = self.hotelIDLineEdit21.text()
        a = self.hotelNameLineEdit22.text()
        b = self.hotelLocIDLineEdit22.text()
        c = self.hotelContactLineEdit22.text()
        if(len(a)==0 or len(b)==0 or len(c)==0 or len(lid)==0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Empty Fields',"Fields cannot be Empty!",QtWidgets.QMessageBox.Ok)
        elif(a.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Name cannot be a number!",QtWidgets.QMessageBox.Ok)
        elif(not c.isdigit() or not b.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"X and Y must be a number",QtWidgets.QMessageBox.Ok)
        elif(int(c)>1000 or int(c)<-1000 or int(b)>1000 or int(b)<-1000):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"X and Y must be between -1000 and 1000",QtWidgets.QMessageBox.Ok)
        else:
            self.mybackend.updatelocationinfo(lid,a,b,c)
    def func6(self):
        a = self.hotelNameLineEdit23.text()
        b = self.hotelLocIDLineEdit23.text()
        c = self.hotelContactLineEdit23.text()
        if(len(a)==0 or len(b)==0 or len(c)==0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Empty Fields',"Fields cannot be Empty!",QtWidgets.QMessageBox.Ok)
        elif(a.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Name cannot be a number!",QtWidgets.QMessageBox.Ok)
        elif(not c.isdigit() or not b.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"X and Y must be a number",QtWidgets.QMessageBox.Ok)
        elif(int(c)>1000 or int(c)<-1000 or int(b)>1000 or int(b)<-1000):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"X and Y must be between -1000 and 1000",QtWidgets.QMessageBox.Ok)
        else:
            self.mybackend.addintolocation(a,b,c)
            self.hotelNameLineEdit23.setText("")
            self.hotelLocIDLineEdit23.setText("")
            self.hotelContactLineEdit23.setText("")
    def reviewtab(self):
        tempCustomQWidget = self.listWidget.itemWidget(self.listWidget.selectedItems()[0])
        test = tempCustomQWidget.hotelNameLabel
        self.Stack.setCurrentWidget(self.reviewcentralwidget)
        self.clicked=False
        self.sortReviewButton.setText('View:')
        self.setReview(test.text())
    def func7(self):
        rid = self.hotelIDLineEdit31.text()
        lower,upper = self.mybackend.getroombounds()
        if(len(rid)==0 or not rid.isdigit() or int(rid)<lower or int(rid)>upper):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Enter a valid ID(int only)",QtWidgets.QMessageBox.Ok)
            self.hotelIDLineEdit31.setText("")
        else:
            a,b,c,d = self.mybackend.getinforoom(rid)
            self.hotelNameLineEdit32.setText(a)
            self.hotelLocIDLineEdit32.setText(b)
            self.hotelContactLineEdit32.setText(c)
            self.hotelBookedLineEdit32.setText(d)
    def func8(self):
        rid = self.hotelIDLineEdit31.text()
        a = self.hotelNameLineEdit32.text()
        b = self.hotelLocIDLineEdit32.text()
        c = self.hotelContactLineEdit32.text()
        d = self.hotelBookedLineEdit32.text()
        lower,upper = self.mybackend.gethotelbounds()
        if(len(a)==0 or len(b)==0 or len(c)==0 or len(rid)==0 or len(d)==0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Empty Fields',"Fields cannot be Empty!",QtWidgets.QMessageBox.Ok)
        elif(int(b)<lower or int(b)>upper):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Hotel_id out of Range",QtWidgets.QMessageBox.Ok)
        elif(not c.isdigit() or not a.isdigit() or not b.isdigit() or not d.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Capacity, Hotel_id, Cost, Booked must be a number",QtWidgets.QMessageBox.Ok)
        elif(int(a)<1 or int(a)>5):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Capacity must be between 1 and 5",QtWidgets.QMessageBox.Ok)
        elif(int(c)<0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Cost cannot be negative",QtWidgets.QMessageBox.Ok)
        elif(not (int(d)==0 or int(d)==1)):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Booked must be 1(True) or 0(False)",QtWidgets.QMessageBox.Ok)
        else:
            self.mybackend.updateroominfo(rid,a,b,c,d)
    def func9(self):
        a = self.hotelNameLineEdit33.text()
        b = self.hotelLocIDLineEdit33.text()
        c = self.hotelContactLineEdit33.text()
        d = self.hotelBookedLineEdit33.text()
        lower,upper = self.mybackend.gethotelbounds()
        if(len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Empty Fields',"Fields cannot be Empty!",QtWidgets.QMessageBox.Ok)
        elif(int(b)<lower or int(b)>upper):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Hotel_id out of Range",QtWidgets.QMessageBox.Ok)
        elif(not c.isdigit() or not a.isdigit() or not b.isdigit() or not d.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Capacity, Hotel_id, Cost, Booked must be a number",QtWidgets.QMessageBox.Ok)
        elif(int(a)<1 or int(a)>5):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Capacity must be between 1 and 5",QtWidgets.QMessageBox.Ok)
        elif(int(c)<0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Cost cannot be negative",QtWidgets.QMessageBox.Ok)
        elif(not (int(d)==0 or int(d)==1)):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Booked must be 1(True) or 0(False)",QtWidgets.QMessageBox.Ok)
        else:
            self.mybackend.addintoroom(a,b,c,d)
            self.hotelNameLineEdit33.setText("")
            self.hotelLocIDLineEdit33.setText("")
            self.hotelContactLineEdit33.setText("")
            self.hotelBookedLineEdit33.setText("")
    def func10(self):
        cid = self.customerIDLineEdit1.text()
        lower,upper = self.mybackend.getcustomerbounds()
        if(len(cid)==0 or not cid.isdigit() or int(cid)<lower or int(cid)>upper):
            choice = QtWidgets.QMessageBox.information(self.customereditcentralwidget, 'Inorrect Input',"Enter a valid ID(int only)",QtWidgets.QMessageBox.Ok)
            self.customerIDLineEdit1.setText("")
        else:
            a,b,c,d,e = self.mybackend.getinfocustomer(cid)
            self.customerFirstNameLineEdit2.setText(a)
            self.customerLastNameLineEdit2.setText(b)
            self.customerContactLineEdit2.setText(c)
            self.customerGenderLineEdit2.setText(d)
            self.customerBalanceLineEdit2.setText(e)
    def func11(self):
        cid = self.customerIDLineEdit1.text()
        a = self.customerFirstNameLineEdit2.text()
        b = self.customerLastNameLineEdit2.text()
        c = self.customerContactLineEdit2.text()
        d = self.customerGenderLineEdit2.text()
        e = self.customerBalanceLineEdit2.text()
        if(len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0 or len(cid)==0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Empty Fields',"Fields cannot be Empty!",QtWidgets.QMessageBox.Ok)
        elif(a.isdigit() or b.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Name cannot be a number!",QtWidgets.QMessageBox.Ok)
        elif(c.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"contact must be an email",QtWidgets.QMessageBox.Ok)
        elif(not(d=="M" or d=="F")):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Gender must be 'M' or 'F'",QtWidgets.QMessageBox.Ok)
        elif(not e.isdigit() or int(e)<0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Balance must be a (positive)number",QtWidgets.QMessageBox.Ok)
        else:
            self.mybackend.updatecustomerinfo(cid,a,b,c,d,e)
    def func12(self):
        a = self.customerFirstNameLineEdit3.text()
        b = self.customerLastNameLineEdit3.text()
        c = self.customerContactLineEdit3.text()
        d = self.customerGenderLineEdit3.text()
        e = self.customerBalanceLineEdit3.text()
        if(len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Empty Fields',"Fields cannot be Empty!",QtWidgets.QMessageBox.Ok)
        elif(a.isdigit() or b.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Name cannot be a number!",QtWidgets.QMessageBox.Ok)
        elif(c.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"contact must be an email",QtWidgets.QMessageBox.Ok)
        elif(not(d=="M" or d=="F")):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Gender must be 'M' or 'F'",QtWidgets.QMessageBox.Ok)
        elif(not e.isdigit() or int(e)<0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Balance must be a (positive)number",QtWidgets.QMessageBox.Ok)
        else:
            self.mybackend.addintocustomer(a,b,c,d,e)
            self.customerFirstNameLineEdit3.setText("")
            self.customerLastNameLineEdit3.setText("")
            self.customerContactLineEdit3.setText("")
            self.customerGenderLineEdit3.setText("")
            self.customerBalanceLineEdit3.setText("")

    def timeCheck(self,t):
        try:
            datetime.strptime(t,'%H:%M:%S')
            return True
        except:
            return False

    def IDpresent(self,attrID):
        IDs = self.mybackendAttraction.getIDs()

        for ids in IDs:
            ID = ids[0]
            if (int(attrID) == ID):
                return True

        return False

    def func007update(self):
        attrID = self.attractionIDInput.text()
        attrName = self.attractionNameInput.text()
        summary = self.attractionSummaryInput.text()
        duration = self.attractionDurationInput.text()
        start = self.attractionStartInput.text()
        cost = self.attractionCostInput.text()
        typeAttr = self.attractionTypeInput.text()


        if (len(attrID)==0 or len(attrName)==0 or len(summary)==0 or len(duration)==0 or len(start)==0 or len(cost)==0 or len(typeAttr)==0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Empty Fields',"Fields cannot be Empty!",QtWidgets.QMessageBox.Ok)
        elif (not attrID.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"ID cannot be alphabetic!",QtWidgets.QMessageBox.Ok)
        # elif(attrName.isdigit()):
            # choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Name cannot be a number!",QtWidgets.QMessageBox.Ok)
        elif(not duration.isdigit() or int(duration) < 0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Duration must be a (positive) number",QtWidgets.QMessageBox.Ok)
        elif(not self.timeCheck(start)):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Time must me in HH:MM:SS format",QtWidgets.QMessageBox.Ok)
        elif(not cost.isdigit() or int(cost) < 0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Cost must be a (positive) number",QtWidgets.QMessageBox.Ok)
        elif (not self.IDpresent(attrID)):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Invalid ID. ID doesn't exist in table. Please enter correct ID to update fields.",QtWidgets.QMessageBox.Ok)
        else:
            self.mybackendAttraction.updateAttractions(attrID,attrName,summary,duration,start,cost,typeAttr)
            self.attractionIDInput.setText("")
            self.attractionNameInput.setText("")
            self.attractionSummaryInput.setText("")
            self.attractionDurationInput.setText("")
            self.attractionStartInput.setText("")
            self.attractionCostInput.setText("")
            self.attractionTypeInput.setText("")

    def func007add(self):
        attrID = self.attractionIDInput.text()
        attrName = self.attractionNameInput.text()
        summary = self.attractionSummaryInput.text()
        duration = self.attractionDurationInput.text()
        start = self.attractionStartInput.text()
        cost = self.attractionCostInput.text()
        typeAttr = self.attractionTypeInput.text()


        if (len(attrID)==0 or len(attrName)==0 or len(summary)==0 or len(duration)==0 or len(start)==0 or len(cost)==0 or len(typeAttr)==0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Empty Fields',"Fields cannot be Empty!",QtWidgets.QMessageBox.Ok)
        elif (not attrID.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"ID cannot be alphabetic!",QtWidgets.QMessageBox.Ok)
        # elif(attrName.isdigit()):
            # choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Name cannot be a number!",QtWidgets.QMessageBox.Ok)
        elif(not duration.isdigit() or int(duration) < 0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Duration must be a (positive) number",QtWidgets.QMessageBox.Ok)
        elif(not self.timeCheck(start)):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Time must me in HH:MM:SS format",QtWidgets.QMessageBox.Ok)
        elif(not cost.isdigit() or int(cost) < 0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Cost must be a (positive) number",QtWidgets.QMessageBox.Ok)
        elif (self.IDpresent(attrID)):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"ID already exists in table. Cannot add new fields with this ID. Please enter new ID to add fields.",QtWidgets.QMessageBox.Ok)
        else:
            self.mybackendAttraction.addAttractions(attrID,attrName,summary,duration,start,cost,typeAttr)
            self.attractionIDInput.setText("")
            self.attractionNameInput.setText("")
            self.attractionSummaryInput.setText("")
            self.attractionDurationInput.setText("")
            self.attractionStartInput.setText("")
            self.attractionCostInput.setText("")
            self.attractionTypeInput.setText("")




    def func009update(self):
        attrID = self.restaurantIDInput.text()
        attrName = self.restaurantNameInput.text()
        cost = self.restaurantCostInput.text()
        typeAttr = self.restaurantCategoryInput.text()
        Lat = self.restaurantLatInput.text()
        Long = self.restaurantLongInput.text()
        Likes = self.restaurantLikesInput.text()
        Neighbourhood = self.restaurantNeighbourhoodInput.text()


        if (len(attrID)==0 and len(attrName)==0 and len(cost)==0 and len(typeAttr)==0 and len(Lat)==0 and len(Long)==0 and len(Likes)==0 and len(Neighbourhood) == 0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Empty Fields',"Fields cannot be Empty!",QtWidgets.QMessageBox.Ok)

        elif(len(attrID) != 0 and not attrID.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"ID cannot be alphabetic",QtWidgets.QMessageBox.Ok)

        elif(len(cost) != 0 and (not cost.isdigit() or int(cost) < 0)):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Incorrect cost",QtWidgets.QMessageBox.Ok)
        elif(len(Likes) != 0) and (not Likes.isdigit() or int(Likes) < 0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Incorrect likes",QtWidgets.QMessageBox.Ok)

        elif len(typeAttr)!= 0 and (typeAttr.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Incorrect Category",QtWidgets.QMessageBox.Ok)
# <<<<<<< HEAD
#         elif len(Lat) != 0 and (not Lat.isdigit()):
#             choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Incorrect Latitude",QtWidgets.QMessageBox.Ok)
#         elif len(Long) != 0 and (not Long.isdigit()):
# =======
        elif len(Lat) is not 0 and (not Lat.replace('.', '', 1).isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Incorrect Latitude",QtWidgets.QMessageBox.Ok)
        elif len(Long) is not 0 and (not Long.replace('.', '', 1).isdigit()):
# >>>>>>> f89cecae8f7d11b88564107b1ef1afca091a26f8
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Incorrect Longitude",QtWidgets.QMessageBox.Ok)

        elif len(Neighbourhood) != 0 and (Neighbourhood.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Incorrect Neighbourhood",QtWidgets.QMessageBox.Ok)

        elif(not self.mybackendRestaurant.getIDs(attrID)):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Incorrect ID/ ID not present",QtWidgets.QMessageBox.Ok)
        else:
            self.mybackendRestaurant.updateRestaurants(attrName,Lat, Long,typeAttr,attrID, Likes, cost, Neighbourhood)

    def func009add(self):
        attrID = self.restaurantIDInput.text()
        attrName = self.restaurantNameInput.text()
        cost = self.restaurantCostInput.text()
        typeAttr = self.restaurantCategoryInput.text()
        Lat = self.restaurantLatInput.text()
        Long = self.restaurantLongInput.text()
        Likes = self.restaurantLikesInput.text()
        Neighbourhood = self.restaurantNeighbourhoodInput.text()


        if (len(attrID)==0 or len(attrName)==0 or len(cost)==0 or len(typeAttr)==0 or len(Lat)==0 or len(Long)==0 or len(Likes)==0 or len(Neighbourhood) == 0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Empty Fields',"Fields cannot be Empty!",QtWidgets.QMessageBox.Ok)

        elif(not attrID.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"ID cannot be alphabetic",QtWidgets.QMessageBox.Ok)

        elif(not cost.isdigit() or int(cost) < 0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Incorrect cost",QtWidgets.QMessageBox.Ok)
        elif(not Likes.isdigit() or int(Likes) < 0):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Incorrect cost",QtWidgets.QMessageBox.Ok)

        elif(typeAttr.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Incorrect Category",QtWidgets.QMessageBox.Ok)
        elif(not Lat.replace('.', '', 1).isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Incorrect Latitude",QtWidgets.QMessageBox.Ok)
        elif(not Long.replace('.', '', 1).isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Incorrect Longitude",QtWidgets.QMessageBox.Ok)

        elif(Neighbourhood.isdigit()):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Incorrect Neighbourhood",QtWidgets.QMessageBox.Ok)
        elif(self.mybackendRestaurant.getIDs(attrID)):
            choice = QtWidgets.QMessageBox.information(self.hoteleditcentralwidget, 'Incorrect Input',"Incorrect ID/ ID present",QtWidgets.QMessageBox.Ok)
        else:
            self.mybackendRestaurant.addRestaurants(attrName,Lat, Long,typeAttr,attrID, Likes, cost, Neighbourhood)


    def adminmodeclicked(self):
        self.Stack.setCurrentWidget(self.adminchoosemodecentralwidget)
    def bookRoomButtonClicked(self):
        if self.clicked:
            self.clicked=False
            money = self.rbalanceLabel.text()
            money = int(money[10:])
            cost = self.bookCostLabel.text()
            cost = int(cost[7:])
            money = money - cost
            if(money>=0):
                choice = QtWidgets.QMessageBox.question(self.bookcentralwidget, 'Confirmation',"Confirm Purchase?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                if choice == QtWidgets.QMessageBox.Yes:
                    self.BALANCE = str(money)
                    self.mybackend.setBalance(str(self.BALANCE),str(self.USER_ID))
                    self.rbalanceLabel.setText("Balance : " + self.BALANCE)
                    self.balanceLabel.setText("Balance : " + self.BALANCE)
                    self.ovbalanceLabel.setText("Balance : " + self.BALANCE)
                    self.bookBalanceLabel.setText("Balance : " + self.BALANCE)
                    tempCustomQWidget = self.bookListWidget.itemWidget(self.bookListWidget.selectedItems()[0])
                    x = tempCustomQWidget.bookRoomIDLabel.text()
                    self.bookListWidget.takeItem(self.bookListWidget.row(self.bookListWidget.selectedItems()[0]))
                    self.mybackend.updateroom(x[10:])

                else:
                    pass
            else:
                choice = QtWidgets.QMessageBox.question(self.bookcentralwidget, 'Confirmation',"Add 5000?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                if choice == QtWidgets.QMessageBox.Yes:
                    money = money + cost + 5000
                    self.BALANCE = str(money)
                    self.mybackend.setBalance(self.BALANCE,self.USER_ID)
                    self.rbalanceLabel.setText("Balance : " + self.BALANCE)
                    self.balanceLabel.setText("Balance : " + self.BALANCE)
                    self.ovbalanceLabel.setText("Balance : " + self.BALANCE)
                    self.bookBalanceLabel.setText("Balance : " + self.BALANCE)
                else:
                    pass
    def hoteledit(self):
        self.Stack.setCurrentWidget(self.hoteleditcentralwidget)
    def backClick(self):
        self.Stack.setCurrentWidget(self.centralwidget1)
        self.clicked=False
        self.setHotel(0)
        self.sortButton.setText("Sort By:")
    def ovbackClick(self):
        self.Stack.setCurrentWidget(self.centralwidget1)
        self.clicked=False
        self.setHotel(0)
        self.sortButton.setText("Sort By:")
    def loginPushButtonClicked(self):
        self.USER_ID = self.loginIDTextEdit.text()
        lower,upper = self.mybackend.getcustomerbounds()
        if(len(self.USER_ID)==0 or not self.USER_ID.isdigit() or int(self.USER_ID)<lower or int(self.USER_ID)>upper):
            choice = QtWidgets.QMessageBox.information(self.logincentralwidget, 'Incorrect Input',"Enter a valid ID(int only)",QtWidgets.QMessageBox.Ok)
            self.loginIDTextEdit.setText("")
        else:
            self.BALANCE = str(self.mybackend.getBalance(self.USER_ID))
            if(self.ADMIN_MODE):
                self.Stack.setCurrentWidget(self.adminchoosemodecentralwidget)
            else:
                self.Stack.setCurrentWidget(self.centralwidget1)
            self.rbalanceLabel.setText("Balance : " + self.BALANCE)
            self.balanceLabel.setText("Balance : " + self.BALANCE)
            self.ovbalanceLabel.setText("Balance : " + self.BALANCE)
            self.bookBalanceLabel.setText("Balance : " + self.BALANCE)
    def adminPushButtonClicked(self):
        self.ADMIN_MODE=True
        self.CUSTOMER_MODE=False
        print('ADMIN_MODE')
        # self.loginModeLabel.setText("Admin Login")
        self.loginPushButtonClicked()
    def customerPushButtonClicked(self):
        self.ADMIN_MODE=False
        self.CUSTOMER_MODE=True
        print('CUSTOMER_MODE')
        # self.loginModeLabel.setText("Customer Login")
        self.loginPushButtonClicked()

    def startMoviesDisplay(self):

        runn(self, self.USER_ID)
        #self.cams = ReviewScreen(self.USER_ID)
        #ex=ReviewScreen(self.USER_ID)
        #self.cams.show()


        #os._exit(1)
        #self.close()



    def bufferFuncHotel(self):
        self.sortMenuItemsHotel()
        # self.listWidget.itemClicked.connect(self.test)
        # self.listWidget.itemSelectionChanged.connect(self.selectionChanged)
        # self.sortMenuItems()
        self.sortButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.hotelButton.clicked.connect(self.setHotel)
        self.bookListWidget.itemClicked.connect(self.test)
        self.listWidget.itemClicked.connect(self.selectionChanged)
        self.sortReviewItems()
        self.sortReviewButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.backButton.clicked.connect(self.backClick)




    def sortMenuItemsAttraction(self):
        sortMenu = QtWidgets.QMenu()

        allAction = QtWidgets.QWidgetAction(sortMenu)
        self.allButton = QtWidgets.QPushButton(self.centralwidget1)
        self.allButton.setText("All")
        self.allButton.clicked.connect(self.displayAttractions)
        allAction.setDefaultWidget(self.allButton)

        durationAscAction = QtWidgets.QWidgetAction(sortMenu)
        self.durationAscButton = QtWidgets.QPushButton(self.centralwidget1)
        self.durationAscButton.setText("Duration Ascending")
        self.durationAscButton.clicked.connect(self.durationAsc)
        durationAscAction.setDefaultWidget(self.durationAscButton)

        durationDescAction = QtWidgets.QWidgetAction(sortMenu)
        self.durationDescButton = QtWidgets.QPushButton(self.centralwidget1)
        self.durationDescButton.setText("Duration Descending")
        self.durationDescButton.clicked.connect(self.durationDesc)
        durationDescAction.setDefaultWidget(self.durationDescButton)

        startTimeAscAction = QtWidgets.QWidgetAction(sortMenu)
        self.startTimeAscButton = QtWidgets.QPushButton(self.centralwidget1)
        self.startTimeAscButton.setText("Start Time Ascending")
        self.startTimeAscButton.clicked.connect(self.startTimeAsc)
        startTimeAscAction.setDefaultWidget(self.startTimeAscButton)

        startTimeDescAction = QtWidgets.QWidgetAction(sortMenu)
        self.startTimeDescButton = QtWidgets.QPushButton(self.centralwidget1)
        self.startTimeDescButton.setText("Start Time Descending")
        self.startTimeDescButton.clicked.connect(self.startTimeDesc)
        startTimeDescAction.setDefaultWidget(self.startTimeDescButton)

        costAscAction = QtWidgets.QWidgetAction(sortMenu)
        self.costAscButton = QtWidgets.QPushButton(self.centralwidget1)
        self.costAscButton.setText("Cost Ascending")
        self.costAscButton.clicked.connect(self.costAsc)
        costAscAction.setDefaultWidget(self.costAscButton)

        costDescAction = QtWidgets.QWidgetAction(sortMenu)
        self.costDescButton = QtWidgets.QPushButton(self.centralwidget1)
        self.costDescButton.setText("Cost Descending")
        self.costDescButton.clicked.connect(self.costDesc)
        costDescAction.setDefaultWidget(self.costDescButton)

        sortMenu.addAction(allAction)
        sortMenu.addSeparator()
        sortMenu.addSeparator()
        sortMenu.addSeparator()
        sortMenu.addAction(durationAscAction)
        sortMenu.addAction(durationDescAction)
        sortMenu.addSeparator()
        sortMenu.addSeparator()
        sortMenu.addSeparator()
        sortMenu.addAction(startTimeAscAction)
        sortMenu.addAction(startTimeDescAction)
        sortMenu.addSeparator()
        sortMenu.addSeparator()
        sortMenu.addSeparator()
        sortMenu.addAction(costAscAction)
        sortMenu.addAction(costDescAction)

        self.sortButton.setMenu(sortMenu)
        self.displayAttractions()

    def displayAttractions(self):
        self.sortButton.setText("Sort By:")
        self.attractions = self.mybackendAttraction.getAttractions()
        self.displayToScreen(self.attractions)

    def durationAsc(self):
        self.sortButton.setText("Duration Ascending")
        self.attractions = self.mybackendAttraction.durationAsc()
        self.displayToScreen(self.attractions)

    def durationDesc(self):
        self.sortButton.setText("Duration Descending")
        self.attractions = self.mybackendAttraction.durationDesc()
        self.displayToScreen(self.attractions)

    def startTimeAsc(self):
        self.sortButton.setText("Start Time Ascending")
        self.attractions = self.mybackendAttraction.startTimeAsc()
        self.displayToScreen(self.attractions)

    def startTimeDesc(self):
        self.sortButton.setText("Start Time Descending")
        self.attractions = self.mybackendAttraction.startTimeDesc()
        self.displayToScreen(self.attractions)

    def costAsc(self):
        self.sortButton.setText("Cost Ascending")
        self.attractions = self.mybackendAttraction.costAsc()
        self.displayToScreen(self.attractions)

    def costDesc(self):
        self.sortButton.setText("Cost Descending")
        self.attractions = self.mybackendAttraction.costDesc()
        self.displayToScreen(self.attractions)

    def displayToScreen(self, data):
        self.listWidget.clear()
        for name, typeAttraction, summary, duration, start, cost in data:
            attractionWidget = AttractionWidget()
            attractionWidget.setTextOnAllLabel('Name :          ' + name, 'Type :           '+typeAttraction, 'Duration  :    '+str(
                duration)+' min', 'Start time :   '+str(start)+' hrs', 'Cost :            '+str(cost), 'Summary :    '+summary)
            listWidgetItem = QtWidgets.QListWidgetItem(self.listWidget)
            listWidgetItem.setSizeHint(attractionWidget.sizeHint())
            # self.listWidget.itemClicked.connect(self.test())
            self.listWidget.addItem(listWidgetItem)
            self.listWidget.setItemWidget(listWidgetItem, attractionWidget)

    def sortMenuItemsRestaurant(self):
        sortMenu = QtWidgets.QMenu()

        allRestAction = QtWidgets.QWidgetAction(sortMenu)
        self.allButton = QtWidgets.QPushButton(self.centralwidget1)
        self.allButton.setText("All")
        self.allButton.clicked.connect(self.displayRestaurants)
        allRestAction.setDefaultWidget(self.allButton)

        costAscRestAction = QtWidgets.QWidgetAction(sortMenu)
        self.costAscRestButton = QtWidgets.QPushButton(self.centralwidget1)
        self.costAscRestButton.setText("Cost Ascending")
        self.costAscRestButton.clicked.connect(self.costAscRest)
        costAscRestAction.setDefaultWidget(self.costAscRestButton)

        costDescRestAction = QtWidgets.QWidgetAction(sortMenu)
        self.costDescRestButton = QtWidgets.QPushButton(self.centralwidget1)
        self.costDescRestButton.setText("Cost Descending")
        self.costDescRestButton.clicked.connect(self.costDescRest)
        costDescRestAction.setDefaultWidget(self.costDescRestButton)

        likeDescRestAction = QtWidgets.QWidgetAction(sortMenu)
        self.likeDescRestButton = QtWidgets.QPushButton(self.centralwidget1)
        self.likeDescRestButton.setText("Likes Descending")
        self.likeDescRestButton.clicked.connect(self.likeDescRest)
        likeDescRestAction.setDefaultWidget(self.likeDescRestButton)

        likeDescRestAction = QtWidgets.QWidgetAction(sortMenu)
        self.ReviewButton = QtWidgets.QPushButton(self.centralwidget1)
        self.ReviewButton.setText("Reviews")
        self.ReviewButton.clicked.connect(self.showRRS)
        likeDescRestAction.setDefaultWidget(self.ReviewButton)

        sortMenu.addAction(allRestAction)
        sortMenu.addSeparator()
        sortMenu.addAction(costAscRestAction)
        sortMenu.addAction(costDescRestAction)
        sortMenu.addSeparator()
        sortMenu.addAction(likeDescRestAction)

        self.sortButton.setMenu(sortMenu)
        self.displayRestaurants()

    def showRRS(self):
        self.ui = RSS()


    def displayRestaurants(self):
        self.sortButton.setText("Sort By:")
        self.restaurants = self.mybackendRestaurant.getRestaurant()
        self.displayToScreenRest(self.restaurants)

    def costAscRest(self):
        self.sortButton.setText("Cost Ascending")
        self.restaurants = self.mybackendRestaurant.costAscRest()
        self.displayToScreenRest(self.restaurants)

    def costDescRest(self):
        self.sortButton.setText("Cost Descending")
        self.restaurants = self.mybackendRestaurant.costDescRest()
        self.displayToScreenRest(self.restaurants)

    def likeDescRest(self):
        self.sortButton.setText("Likes Descending")
        self.restaurants = self.mybackendRestaurant.likeDescRest()
        self.displayToScreenRest(self.restaurants)

    def displayToScreenRest(self, data):
        self.listWidget.clear()
        for venue, category, cost, likes in data:
            restaurantWidget = RestaurantWidget()
            restaurantWidget.setTextOnAllLabel('Name :          ' + venue, 'Type :           '+category, 'Cost :            '+str(cost), 'Likes :            '+str(likes))
            listWidgetItem = QtWidgets.QListWidgetItem(self.listWidget)
            listWidgetItem.setSizeHint(restaurantWidget.sizeHint())
            # self.listWidget.itemClicked.connect(self.test())
            self.listWidget.addItem(listWidgetItem)
            self.listWidget.setItemWidget(listWidgetItem, restaurantWidget)

    def sortReviewItems(self):
        sortReviewMenu = QtWidgets.QMenu()
        positiveAction = QtWidgets.QWidgetAction(sortReviewMenu)
        self.positiveButton = QtWidgets.QPushButton(self.reviewcentralwidget)
        self.positiveButton.setText("Positive Reviews")
        self.positiveButton.clicked.connect(self.positiveclick)
        positiveAction.setDefaultWidget(self.positiveButton)
        negativeAction = QtWidgets.QWidgetAction(sortReviewMenu)
        self.negativeButton = QtWidgets.QPushButton(self.reviewcentralwidget)
        self.negativeButton.setText("Negative Reviews")
        self.negativeButton.clicked.connect(self.negativeclick)
        negativeAction.setDefaultWidget(self.negativeButton)
        neutralAction = QtWidgets.QWidgetAction(sortReviewMenu)
        self.neutralButton = QtWidgets.QPushButton(self.reviewcentralwidget)
        self.neutralButton.setText("Neutral Reviews")
        self.neutralButton.clicked.connect(self.neutralclick)
        neutralAction.setDefaultWidget(self.neutralButton)
        allReviewsAction = QtWidgets.QWidgetAction(sortReviewMenu)
        self.allReviewsButton = QtWidgets.QPushButton(self.reviewcentralwidget)
        self.allReviewsButton.setText("All")
        self.allReviewsButton.clicked.connect(self.allreviewsclick)
        allReviewsAction.setDefaultWidget(self.allReviewsButton)
        sortReviewMenu.addAction(positiveAction)
        sortReviewMenu.addAction(negativeAction)
        sortReviewMenu.addAction(neutralAction)
        sortReviewMenu.addSeparator()
        sortReviewMenu.addAction(allReviewsAction)
        self.sortReviewButton.setMenu(sortReviewMenu)
    def positiveclick(self):
        self.sortReviewButton.setText("Positive Reviews:")
        self.setReviewMood(3)
    def negativeclick(self):
        self.sortReviewButton.setText("Negative Reviews:")
        self.setReviewMood(1)
    def neutralclick(self):
        self.sortReviewButton.setText("Neutral Reviews:")
        self.setReviewMood(2)
    def allreviewsclick(self):
        self.sortReviewButton.setText("View:")
        self.setReviewMood(4)
    def sortMenuItemsHotel(self):
        sortMenu = QtWidgets.QMenu()

        fourAction = QtWidgets.QWidgetAction(sortMenu)
        self.fourButton = QtWidgets.QPushButton(self.centralwidget1)
        self.fourButton.setText("Rating 4 and above")
        self.fourButton.clicked.connect(self.fourstarsandabove)
        fourAction.setDefaultWidget(self.fourButton)

        threeAction = QtWidgets.QWidgetAction(sortMenu)
        self.threeButton = QtWidgets.QPushButton(self.centralwidget1)
        self.threeButton.setText("Rating 3 and above")
        self.threeButton.clicked.connect(self.threestarsandabove)
        threeAction.setDefaultWidget(self.threeButton)

        twoAction = QtWidgets.QWidgetAction(sortMenu)
        self.twoButton = QtWidgets.QPushButton(self.centralwidget1)
        self.twoButton.setText("Rating 2 and above")
        self.twoButton.clicked.connect(self.twostarsandabove)
        twoAction.setDefaultWidget(self.twoButton)

        oneAction = QtWidgets.QWidgetAction(sortMenu)
        self.oneButton = QtWidgets.QPushButton(self.centralwidget1)
        self.oneButton.setText("Rating 1 and above")
        self.oneButton.clicked.connect(self.onestarsandabove)
        oneAction.setDefaultWidget(self.oneButton)

        zeroAction = QtWidgets.QWidgetAction(sortMenu)
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget1)
        self.zeroButton.setText("All")
        self.zeroButton.clicked.connect(self.zerostarsandabove)
        zeroAction.setDefaultWidget(self.zeroButton)

        sixthouAction = QtWidgets.QWidgetAction(sortMenu)
        self.sixthouButton = QtWidgets.QPushButton(self.centralwidget1)
        self.sixthouButton.setText("Price: 6000 and below")
        self.sixthouButton.clicked.connect(self.sixthouandbelow)
        sixthouAction.setDefaultWidget(self.sixthouButton)

        fivethouAction = QtWidgets.QWidgetAction(sortMenu)
        self.fivethouButton = QtWidgets.QPushButton(self.centralwidget1)
        self.fivethouButton.setText("Price: 5000 and below")
        self.fivethouButton.clicked.connect(self.fivethouandbelow)
        fivethouAction.setDefaultWidget(self.fivethouButton)

        fourthouAction = QtWidgets.QWidgetAction(sortMenu)
        self.fourthouButton = QtWidgets.QPushButton(self.centralwidget1)
        self.fourthouButton.setText("Price: 4000 and below")
        self.fourthouButton.clicked.connect(self.fourthouandbelow)
        fourthouAction.setDefaultWidget(self.fourthouButton)

        threethouAction = QtWidgets.QWidgetAction(sortMenu)
        self.threethouButton = QtWidgets.QPushButton(self.centralwidget1)
        self.threethouButton.setText("Price: 3000 and below")
        self.threethouButton.clicked.connect(self.threethouandbelow)
        threethouAction.setDefaultWidget(self.threethouButton)

        twothouAction = QtWidgets.QWidgetAction(sortMenu)
        self.twothouButton = QtWidgets.QPushButton(self.centralwidget1)
        self.twothouButton.setText("Price: 2000 and below")
        self.twothouButton.clicked.connect(self.twothouandbelow)
        twothouAction.setDefaultWidget(self.twothouButton)

        sortMenu.addAction(zeroAction)
        sortMenu.addSeparator()
        sortMenu.addAction(fourAction)
        sortMenu.addAction(threeAction)
        sortMenu.addAction(twoAction)
        sortMenu.addAction(oneAction)
        sortMenu.addSeparator()
        sortMenu.addAction(sixthouAction)
        sortMenu.addAction(fivethouAction)
        sortMenu.addAction(fourthouAction)
        sortMenu.addAction(threethouAction)
        sortMenu.addAction(twothouAction)

        self.sortButton.setMenu(sortMenu)
        self.setHotel()

    def fourstarsandabove(self):
        self.sortButton.setText("Rating: 4+")
        self.setHotel(4)

    def threestarsandabove(self):
        self.sortButton.setText("Rating: 3+")
        self.setHotel(3)

    def twostarsandabove(self):
        self.sortButton.setText("Rating: 2+")
        self.setHotel(2)

    def onestarsandabove(self):
        self.sortButton.setText("Rating: 1+")
        self.setHotel(1)

    def zerostarsandabove(self):
        self.sortButton.setText("Sort By:")
        self.setHotel(0)

    def sixthouandbelow(self):
        self.sortButton.setText("Price: Below 6000")
        self.setHotelPrice(6000)

    def fivethouandbelow(self):
        self.sortButton.setText("Price: Below 5000")
        self.setHotelPrice(5000)

    def fourthouandbelow(self):
        self.sortButton.setText("Price: Below 4000")
        self.setHotelPrice(4000)

    def threethouandbelow(self):
        self.sortButton.setText("Price: Below 3000")
        self.setHotelPrice(3000)

    def twothouandbelow(self):
        self.sortButton.setText("Price: Below 2000")
        self.setHotelPrice(2000)

    def overviewClicked(self):
        self.Stack.setCurrentWidget(self.overviewcentralwidget)

    def test(self):
        if(self.clicked == False):
            print('clicked')
        self.clicked = True

    def selectionChanged(self):
        tempCustomQWidget = self.listWidget.itemWidget(self.listWidget.selectedItems()[0])
        name = tempCustomQWidget.hotelNameLabel.text()
        locality = tempCustomQWidget.localityLabel.text()
        rating = tempCustomQWidget.averageRatingLabel.text()
        price = tempCustomQWidget.averagePriceLabel.text()
        booked = tempCustomQWidget.percentageBookedLabel.text()
        self.nLabel.setText("Name : "+ name[7:])
        self.pLabel.setText("Average Price : "+ price[13:])
        self.lLabel.setText("Locality : "+ locality[11:])
        self.rLabel.setText("Average Rating : "+ rating[13:])
        self.bLabel.setText("Booked Percent : "+ booked[8:])
        self.Stack.setCurrentWidget(self.overviewcentralwidget)
        self.clicked=False
    def test(self):
        if(self.clicked==False):
            print('clicked')
        tempCustomQWidget = self.bookListWidget.itemWidget(self.bookListWidget.selectedItems()[0])
        self.bookCapacity.setText(tempCustomQWidget.bookCapacityLabel.text())
        self.bookCostLabel.setText(tempCustomQWidget.bookCostLabel.text())
        self.bookIDLabel.setText(tempCustomQWidget.bookRoomIDLabel.text())
        self.clicked=True;
    def bookbackclick(self):
        self.Stack.setCurrentWidget(self.centralwidget1)
        self.clicked=False
        self.setHotel(0)
        self.sortButton.setText("Sort By:")
    def bookreviewclick(self):
        tempCustomQWidget = self.listWidget.itemWidget(self.listWidget.selectedItems()[0])
        test = tempCustomQWidget.hotelNameLabel
        self.Stack.setCurrentWidget(self.reviewcentralwidget)
        self.clicked=False
        self.sortReviewButton.setText('View:')
        self.setReview(test.text())
    def bookoverviewclick(self):
        self.Stack.setCurrentWidget(self.overviewcentralwidget)
        self.clicked=False
    def ovbookclick(self):
        tempCustomQWidget = self.listWidget.itemWidget(self.listWidget.selectedItems()[0])
        test = tempCustomQWidget.hotelNameLabel
        self.Stack.setCurrentWidget(self.bookcentralwidget)
        self.bookCapacity.setText("Capacity : ")
        self.bookCostLabel.setText("Cost : ")
        self.bookIDLabel.setText("Room ID : ")
        self.clicked=False
        self.setRooms(test.text())
    def reviewbookclick(self):
        tempCustomQWidget = self.listWidget.itemWidget(self.listWidget.selectedItems()[0])
        test = tempCustomQWidget.hotelNameLabel
        self.Stack.setCurrentWidget(self.bookcentralwidget)
        # self.bookCapacity.setText("")
        self.clicked=False
        # self.bookCostLabel.setText("")
        # self.bookIDLabel.setText("")
        self.setRooms(test.text())
    def setHotel(self,rating=0):
        self.hotels = self.mybackend.gethotelbyrating(rating)
        self.listWidget.clear()
        for name,hid,loc,avg_price,booked,rating in self.hotels:
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextOnAllLabel('Name : ' + name,'Avg. Rating : '+rating,'Locality : '+loc,'Avg. Price : '+avg_price,'Booked : '+booked)
            listWidgetItem = QtWidgets.QListWidgetItem(self.listWidget)
            listWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            self.listWidget.addItem(listWidgetItem)
            self.listWidget.setItemWidget(listWidgetItem, myQCustomQWidget)
    def setHotelPrice(self,price):
        self.hotels = self.mybackend.gethotelbyprice(price)
        self.listWidget.clear()
        for name,hid,loc,avg_price,booked,rating in self.hotels:
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextOnAllLabel('Name : ' + name,'Avg. Rating : '+rating,'Locality : '+loc,'Avg. Price : '+avg_price,'Booked : '+booked)
            listWidgetItem = QtWidgets.QListWidgetItem(self.listWidget)
            listWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            self.listWidget.addItem(listWidgetItem)
            self.listWidget.setItemWidget(listWidgetItem, myQCustomQWidget)
    def setReview(self,hotel_name):
        self.reviewlist = self.mybackend.getReview(hotel_name)
        self.reviewlistWidget.clear()
        for rid,stars,desc,cid,hid,name,hotel_name in self.reviewlist:
            myQCustomQWidget = QCustomQWidget2()
            myQCustomQWidget.setTextOnAllLabel(name+" - "+stars+" Stars",desc)
            listWidgetItem = QtWidgets.QListWidgetItem(self.reviewlistWidget)
            listWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            self.reviewlistWidget.addItem(listWidgetItem)
            self.reviewlistWidget.setItemWidget(listWidgetItem, myQCustomQWidget)
    def setReviewMood(self,mood):
        if(mood==1):
            self.reviewlistWidget.clear()
            for rid,stars,desc,cid,hid,name,hotel_name in self.reviewlist:
                if(desc=='Bad' or desc=='Very Bad'):
                    myQCustomQWidget = QCustomQWidget2()
                    myQCustomQWidget.setTextOnAllLabel(name+" - "+stars+" Stars",desc)
                    listWidgetItem = QtWidgets.QListWidgetItem(self.reviewlistWidget)
                    listWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
                    self.reviewlistWidget.addItem(listWidgetItem)
                    self.reviewlistWidget.setItemWidget(listWidgetItem, myQCustomQWidget)
        elif(mood==2):
            self.reviewlistWidget.clear()
            for rid,stars,desc,cid,hid,name,hotel_name in self.reviewlist:
                if(desc=='Average'):
                    myQCustomQWidget = QCustomQWidget2()
                    myQCustomQWidget.setTextOnAllLabel(name+" - "+stars+" Stars",desc)
                    listWidgetItem = QtWidgets.QListWidgetItem(self.reviewlistWidget)
                    listWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
                    self.reviewlistWidget.addItem(listWidgetItem)
                    self.reviewlistWidget.setItemWidget(listWidgetItem, myQCustomQWidget)
        elif(mood==3):
            self.reviewlistWidget.clear()
            for rid,stars,desc,cid,hid,name,hotel_name in self.reviewlist:
                if(desc=='Good' or desc=='Very Good' or desc=='Excellent'):
                    myQCustomQWidget = QCustomQWidget2()
                    myQCustomQWidget.setTextOnAllLabel(name+" - "+stars+" Stars",desc)
                    listWidgetItem = QtWidgets.QListWidgetItem(self.reviewlistWidget)
                    listWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
                    self.reviewlistWidget.addItem(listWidgetItem)
                    self.reviewlistWidget.setItemWidget(listWidgetItem, myQCustomQWidget)
        else:
            self.reviewlistWidget.clear()
            for rid,stars,desc,cid,hid,name,hotel_name in self.reviewlist:
                myQCustomQWidget = QCustomQWidget2()
                myQCustomQWidget.setTextOnAllLabel(name+" - "+stars+" Stars",desc)
                listWidgetItem = QtWidgets.QListWidgetItem(self.reviewlistWidget)
                listWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
                self.reviewlistWidget.addItem(listWidgetItem)
                self.reviewlistWidget.setItemWidget(listWidgetItem, myQCustomQWidget)
    def setRooms(self,hotel_name):
        self.roomlist = self.mybackend.getrooms(hotel_name)
        self.bookListWidget.clear()
        for rid,cap,hid,cost,booked,hotel_name in self.roomlist:
            myQCustomQWidget = QCustomQWidget3()
            myQCustomQWidget.setTextOnAllLabel("Cost : "+cost,"Capacity : "+cap,"Room ID : "+rid)
            listWidgetItem = QtWidgets.QListWidgetItem(self.bookListWidget)
            listWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            self.bookListWidget.addItem(listWidgetItem)
            self.bookListWidget.setItemWidget(listWidgetItem, myQCustomQWidget)
################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hotelButton.setStatusTip(
            _translate("MainWindow", "Search for Hotels"))
        self.hotelButton.setText(_translate("MainWindow", "Hotels"))
        self.airlinesButton.setText(_translate("MainWindow", "Airlines"))
        self.airlinesButton.setStatusTip(
            _translate("MainWindow", "Search for Airlines"))
        self.movieButton.setText(_translate("MainWindow", "Movies"))
        self.movieButton.setStatusTip(
            _translate("MainWindow", "Search for Movies"))
        self.attractionButton.setText(_translate("MainWindow", "Attractions"))
        self.attractionButton.setStatusTip(
            _translate("MainWindow", "Search for Attractions"))
        self.RestaurantButton.setText(_translate("MainWindow", "Restaurants"))
        self.RestaurantButton.setStatusTip(
            _translate("MainWindow", "Search for Restaurants"))
        self.sortButton.setText(_translate("MainWindow", "Sort By:"))
        self.balanceLabel.setText(_translate("MainWindow", "Balance : "))
        self.indentifierLabel.setText(_translate("MainWindow", "e-Raahi"))
        self.balanceLabel.setText(_translate("MainWindow", "Balance : "))
        self.indetifierLabel.setText(_translate("MainWindow", "e-Raahi"))
        self.overviewButton.setText(_translate("MainWindow", "Overview"))
        self.bookButton.setText(_translate("MainWindow", "Book"))
        self.reviewButton.setText(_translate("MainWindow", "Reviews"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.custNameLabel.setText(_translate("MainWindow", "Customer Name"))
        self.label.setText(_translate("MainWindow", "Review"))
        self.sortReviewButton.setText(_translate("MainWindow", "View :"))
        self.menuMode.setTitle(_translate("MainWindow", "Option"))
        self.actionChangeMode.setText(_translate("MainWindow", "Change Mode"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.hotelButton.setStatusTip(_translate("MainWindow", "Search for Hotels"))
        self.hotelButton.setText(_translate("MainWindow", "Hotels"))
        self.airlinesButton.setText(_translate("MainWindow", "Airlines"))
        self.movieButton.setText(_translate("MainWindow", "Movies"))
        self.attractionButton.setText(_translate("MainWindow", "Attractions"))
        self.RestaurantButton.setText(_translate("MainWindow", "Restaurants"))
        self.sortButton.setText(_translate("MainWindow", "Sort By:"))
        self.balanceLabel.setText(_translate("MainWindow", "Balance : "))
        # self.indentifierLabel.setText(_translate("MainWindow", "Hotels"))
        self.balanceLabel.setText(_translate("MainWindow", "Balance : "))
        self.indetifierLabel.setText(_translate("MainWindow", "Hotels"))
        self.overviewButton.setText(_translate("MainWindow", "Overview"))
        self.reviewbookButton.setText(_translate("MainWindow", "Book"))
        self.reviewButton.setText(_translate("MainWindow", "Reviews"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.custNameLabel.setText(_translate("MainWindow", "Customer Name"))
        self.label.setText(_translate("MainWindow", "Review"))
        self.sortReviewButton.setText(_translate("MainWindow", "View:"))
        self.nLabel.setText(_translate("MainWindow", "Name : "))
        self.pLabel.setText(_translate("MainWindow", "Average Price :"))
        self.lLabel.setText(_translate("MainWindow", "Locality : "))
        self.rLabel.setText(_translate("MainWindow", "Average Rating : "))
        self.bLabel.setText(_translate("MainWindow", "Booked Percent : "))
        self.ovbalanceLabel.setText(_translate("MainWindow", "Balance : "))
        self.ovindetifierLabel.setText(_translate("MainWindow", "Hotels"))
        self.ovoverviewButton.setText(_translate("MainWindow", "Overview"))
        self.ovbookButton.setText(_translate("MainWindow", "Book"))
        self.ovreviewButton.setText(_translate("MainWindow", "Reviews"))
        self.ovbackButton.setText(_translate("MainWindow", "Back"))
        self.rbalanceLabel.setText(_translate("MainWindow",'Balance :'))
        self.bookBalanceLabel.setText(_translate("MainWindow", "Balance : "))
        self.bookIndetifierLabel.setText(_translate("MainWindow", "Hotels"))
        self.bookOverviewButton.setText(_translate("MainWindow", "Overview"))
        self.bookButton.setText(_translate("MainWindow", "Book"))
        self.bookReviewButton.setText(_translate("MainWindow", "Reviews"))
        self.bookBackButton.setText(_translate("MainWindow", "Back"))
        self.bookBookingButton.setText(_translate("MainWindow", "BOOK"))
        self.bookIDLabel.setText(_translate("MainWindow", "Room ID : "))
        self.bookCapacity.setText(_translate("MainWindow", "Capacity :"))
        self.bookCostLabel.setText(_translate("MainWindow", "Cost : "))
        self.adminCustomerPushButton.setStatusTip(_translate("MainWindow", "Customer Settings"))
        self.adminCustomerPushButton.setText(_translate("MainWindow", "Customer"))
        self.adminHotelPushButton.setStatusTip(_translate("MainWindow", "Hotel Settings"))
        self.adminHotelPushButton.setText(_translate("MainWindow", "Hotel"))
        self.adminAttractionsPushButton.setStatusTip(_translate("MainWindow", "Attractions Settings"))
        self.adminAttractionsPushButton.setText(_translate("MainWindow", "Attractions"))
        self.adminMoviesPushButton.setStatusTip(_translate("MainWindow", "Movies Settings"))
        self.adminMoviesPushButton.setText(_translate("MainWindow", "Movies"))
        self.adminAirlinesPushButton.setStatusTip(_translate("MainWindow", "Airlines Settings"))
        self.adminAirlinesPushButton.setText(_translate("MainWindow", "Airlines"))
        self.adminRestaurantsPushButton.setStatusTip(_translate("MainWindow", "Restaurants Settings"))
        self.adminRestaurantsPushButton.setText(_translate("MainWindow", "Restaurants"))
        self.adminChooseModeLabell.setText(_translate("MainWindow", "CHOOSE MODE"))
        self.hotelLogoLabel1.setText(_translate("MainWindow", "HOTEL"))
        self.hotelEditPushButton11.setText(_translate("MainWindow", "Edit"))
        self.hotelIDLabel11.setText(_translate("MainWindow", "ID : "))
        self.hotelNameLabel12.setText(_translate("MainWindow", "Name : "))
        self.hotelLocIDLabel12.setText(_translate("MainWindow", "Loc_id : "))
        self.hotelContactLabel12.setText(_translate("MainWindow", "Contact : "))
        self.hotelAddPushButton1.setText(_translate("MainWindow", "Add"))
        self.hotelNameLabel13.setText(_translate("MainWindow", "Name : "))
        self.hotelLocIDLabel13.setText(_translate("MainWindow", "Loc_id : "))
        self.hotelContactLabel13.setText(_translate("MainWindow", "Contact : "))
        self.hotelGoPushButton13.setText(_translate("MainWindow","Go"))
        self.hotelUpdatePushButton12.setText(_translate("MainWindow","Update"))
        self.hotelLogoLabel2.setText(_translate("MainWindow", "LOCATIONS"))
        self.hotelEditPushButton21.setText(_translate("MainWindow", "Edit"))
        self.hotelIDLabel21.setText(_translate("MainWindow", "ID : "))
        self.hotelNameLabel22.setText(_translate("MainWindow", "Name : "))
        self.hotelLocIDLabel22.setText(_translate("MainWindow", "X : "))
        self.hotelContactLabel22.setText(_translate("MainWindow", "Y : "))
        self.hotelAddPushButton2.setText(_translate("MainWindow", "Add"))
        self.hotelNameLabel23.setText(_translate("MainWindow", "Name : "))
        self.hotelLocIDLabel23.setText(_translate("MainWindow", "X : "))
        self.hotelContactLabel23.setText(_translate("MainWindow", "Y : "))
        self.hotelGoPushButton23.setText(_translate("MainWindow","Go"))
        self.hotelUpdatePushButton22.setText(_translate("MainWindow","Update"))
        self.hotelLogoLabel3.setText(_translate("MainWindow", "ROOM"))
        self.hotelEditPushButton31.setText(_translate("MainWindow", "Edit"))
        self.hotelIDLabel31.setText(_translate("MainWindow", "ID : "))
        self.hotelNameLabel32.setText(_translate("MainWindow", "Capacity : "))
        self.hotelLocIDLabel32.setText(_translate("MainWindow", "Hotel_id : "))
        self.hotelContactLabel32.setText(_translate("MainWindow", "Cost : "))
        self.hotelBookedLabel32.setText(_translate("MainWindow","Booked : "))
        self.hotelAddPushButton3.setText(_translate("MainWindow", "Add"))
        self.hotelNameLabel33.setText(_translate("MainWindow", "Capacity : "))
        self.hotelLocIDLabel33.setText(_translate("MainWindow", "Hotel_id : "))
        self.hotelContactLabel33.setText(_translate("MainWindow", "Cost : "))
        self.hotelBookedLabel33.setText(_translate("MainWindow","Booked : "))
        self.hotelGoPushButton33.setText(_translate("MainWindow","Go"))
        self.hotelUpdatePushButton32.setText(_translate("MainWindow","Update"))
        self.customerLogoLabel1.setText(_translate("MainWindow", "CUSTOMER"))
        self.customerEditPushButton1.setText(_translate("MainWindow", "Edit"))
        self.customerIDLabel1.setText(_translate("MainWindow", "ID : "))
        self.customerFirstNameLabel2.setText(_translate("MainWindow", "firstName : "))
        self.customerLastNameLabel2.setText(_translate("MainWindow", "lastName : "))
        self.customerContactLabel2.setText(_translate("MainWindow", "Contact : "))
        self.customerGenderLabel2.setText(_translate("MainWindow", "Gender : "))
        self.customerBalanceLabel2.setText(_translate("MainWindow", "Balance : "))
        self.customerUpdatePushButton2.setText(_translate("MainWindow", "Update"))
        self.customerAddPushButton1.setText(_translate("MainWindow", "Add"))
        self.customerFirstNameLabel3.setText(_translate("MainWindow", "firstName : "))
        self.customerLastNameLabel3.setText(_translate("MainWindow", "lastName : "))
        self.customerContactLabel3.setText(_translate("MainWindow", "Contact : "))
        self.customerGenderLabel3.setText(_translate("MainWindow", "Gender : "))
        self.customerBalanceLabel3.setText(_translate("MainWindow", "Balance : "))
        self.customerGoPushButton3.setText(_translate("MainWindow", "Go"))

        self.attractionLabel.setText(_translate("MainWindow", "You are editing the Attraction table. Please note Attraction_ID is the primary key."))
        self.attractionIDLabel.setText(_translate("MainWindow", "Attraction ID : "))
        self.attractionNameLabel.setText(_translate("MainWindow", "Name Of Attraction : "))
        self.attractionSummaryLabel.setText(_translate("MainWindow", "Summary : "))
        self.attractionDurationLabel.setText(_translate("MainWindow", "Duration : "))
        self.attractionStartLabel.setText(_translate("MainWindow", "Start Time : "))
        self.attractionCostLabel.setText(_translate("MainWindow", "Cost : "))
        self.attractionTypeLabel.setText(_translate("MainWindow", "Type :"))

        self.attractionUpdateButton.setText(_translate("MainWindow", "Update"))
        self.attractionAddButton.setText(_translate("MainWindow", "Add"))


        self.restaurantLabel.setText(_translate("MainWindow", "You are editing the Restaurant table. Please note Venue_ID is the primary key."))
        self.restaurantIDLabel.setText(_translate("MainWindow", "Restaurant ID : "))
        self.restaurantNameLabel.setText(_translate("MainWindow", "Name Of Restaurant : "))
        self.restaurantLatLabel.setText(_translate("MainWindow", "Latitude : "))
        self.restaurantLongLabel.setText(_translate("MainWindow", "Longitude : "))
        self.restaurantCategoryLabel.setText(_translate("MainWindow", "Category : "))
        self.restaurantCostLabel.setText(_translate("MainWindow", "Cost : "))
        self.restaurantLikesLabel.setText(_translate("MainWindow", "Likes :"))
        self.restaurantNeighbourhoodLabel.setText(_translate("MainWindow", "Neighbourhood :"))

        self.restaurantUpdateButton.setText(_translate("MainWindow", "Update"))
        self.restaurantAddButton.setText(_translate("MainWindow", "Add"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
