from PyQt5 import QtCore, QtGui, QtWidgets
from backendHotel import backendHotel
from backendAttraction import backendAttraction


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


class QCustomQWidget2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(QCustomQWidget, self).__init__(parent)

        self.textQVBoxRightLayout = QtWidgets.QVBoxLayout()
        self.averagePriceLabel = QtWidgets.QLabel()
        self.percentageBookedLabel = QtWidgets.QLabel()
        self.textQVBoxRightLayout.addWidget(self.averagePriceLabel, 0)
        self.textQVBoxRightLayout.addWidget(self.percentageBookedLabel, 1)
        self.textQVBoxRightLayout.setAlignment(QtCore.Qt.AlignRight)

        self.insideQHBoxLayout = QtWidgets.QHBoxLayout()
        self.averageRatingLabel = QtWidgets.QLabel()
        self.localityLabel = QtWidgets.QLabel()
        self.insideQHBoxLayout.addWidget(self.averageRatingLabel, 0)
        self.insideQHBoxLayout.addWidget(self.localityLabel, 1)

        self.textQVBoxLeftLayout = QtWidgets.QVBoxLayout()
        self.hotelNameLabel = QtWidgets.QLabel()
        self.textQVBoxLeftLayout.addWidget(self.hotelNameLabel, 0)
        self.textQVBoxLeftLayout.addLayout(self.insideQHBoxLayout, 1)

        self.allQHBoxLayout = QtWidgets.QHBoxLayout()
        self.allQHBoxLayout.addLayout(self.textQVBoxLeftLayout, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxRightLayout, 1)
        self.setLayout(self.allQHBoxLayout)

    def setTextOnAllLabel(self, hotelNameLabel, averageRatingLabel, localityLabel, averagePriceLabel, percentageBookedLabel):
        self.hotelNameLabel.setText(hotelNameLabel)
        self.averageRatingLabel.setText(averageRatingLabel)
        self.localityLabel.setText(localityLabel)
        self.averagePriceLabel.setText(averagePriceLabel)
        self.percentageBookedLabel.setText(percentageBookedLabel)


class QCustomQWidget (QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(QCustomQWidget, self).__init__(parent)

        self.textQVBoxRightLayout = QtWidgets.QVBoxLayout()
        self.averagePriceLabel = QtWidgets.QLabel()
        self.percentageBookedLabel = QtWidgets.QLabel()
        self.textQVBoxRightLayout.addWidget(self.averagePriceLabel, 0)
        self.textQVBoxRightLayout.addWidget(self.percentageBookedLabel, 1)
        self.textQVBoxRightLayout.setAlignment(QtCore.Qt.AlignRight)

        self.insideQHBoxLayout = QtWidgets.QHBoxLayout()
        self.averageRatingLabel = QtWidgets.QLabel()
        self.localityLabel = QtWidgets.QLabel()
        self.insideQHBoxLayout.addWidget(self.averageRatingLabel, 0)
        self.insideQHBoxLayout.addWidget(self.localityLabel, 1)

        self.textQVBoxLeftLayout = QtWidgets.QVBoxLayout()
        self.hotelNameLabel = QtWidgets.QLabel()
        self.textQVBoxLeftLayout.addWidget(self.hotelNameLabel, 0)
        self.textQVBoxLeftLayout.addLayout(self.insideQHBoxLayout, 1)

        self.allQHBoxLayout = QtWidgets.QHBoxLayout()
        self.allQHBoxLayout.addLayout(self.textQVBoxLeftLayout, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxRightLayout, 1)
        self.setLayout(self.allQHBoxLayout)

    def setTextOnAllLabel(self, hotelNameLabel, averageRatingLabel, localityLabel, averagePriceLabel, percentageBookedLabel):
        self.hotelNameLabel.setText(hotelNameLabel)
        self.averageRatingLabel.setText(averageRatingLabel)
        self.localityLabel.setText(localityLabel)
        self.averagePriceLabel.setText(averagePriceLabel)
        self.percentageBookedLabel.setText(percentageBookedLabel)
##############################################################


class Ui_MainWindow(object):
    ##################################
    clicked = False
    ##################################

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.Stack = QtWidgets.QStackedWidget(MainWindow)

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
        self.bookButton = QtWidgets.QPushButton(self.reviewcentralwidget)
        self.bookButton.setGeometry(QtCore.QRect(267, 130, 266, 25))
        self.bookButton.setObjectName("bookButton")
        self.reviewButton = QtWidgets.QPushButton(self.reviewcentralwidget)
        self.reviewButton.setGeometry(QtCore.QRect(532, 130, 267, 25))
        self.reviewButton.setObjectName("reviewButton")
        self.backButton = QtWidgets.QPushButton(self.reviewcentralwidget)
        self.backButton.setGeometry(QtCore.QRect(0, 100, 151, 31))
        self.backButton.setObjectName("backButton")
        self.listWidget = QtWidgets.QListWidget(self.reviewcentralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 180, 800, 420))
        self.listWidget.setObjectName("listWidget")
        self.custNameLabel = QtWidgets.QLabel(self.reviewcentralwidget)
        self.custNameLabel.setGeometry(QtCore.QRect(0, 155, 200, 25))
        self.custNameLabel.setObjectName("custNameLabel")
        self.label = QtWidgets.QLabel(self.reviewcentralwidget)
        self.label.setGeometry(QtCore.QRect(400, 155, 200, 25))
        self.label.setObjectName("label")
        self.sortReviewButton = QtWidgets.QToolButton(self.reviewcentralwidget)
        self.sortReviewButton.setGeometry(QtCore.QRect(650, 155, 150, 25))
        self.sortReviewButton.setObjectName("sortReviewButton")

        self.centralwidget1 = QtWidgets.QWidget(MainWindow)
        self.centralwidget1.setObjectName("centralwidget1")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget1)
        self.listWidget.setGeometry(QtCore.QRect(0, 130, 800, 370))
        self.listWidget.setObjectName("listWidget")

        self.logoLabel = QtWidgets.QLabel(self.centralwidget1)
        self.logoLabel.setGeometry(QtCore.QRect(0, 0, 800, 100))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap("E - Raahi.png"))
        self.logoLabel.setObjectName("logoLabel")

        self.hotelButton = QtWidgets.QPushButton(self.centralwidget1)
        self.hotelButton.setGeometry(QtCore.QRect(0, 500, 160, 60))
        self.hotelButton.setObjectName("hotelButton")

        self.airlinesButton = QtWidgets.QPushButton(self.centralwidget1)
        self.airlinesButton.setGeometry(QtCore.QRect(160, 500, 160, 60))
        self.airlinesButton.setObjectName("airlinesButton")

        self.movieButton = QtWidgets.QPushButton(self.centralwidget1)
        self.movieButton.setGeometry(QtCore.QRect(320, 500, 160, 60))
        self.movieButton.setObjectName("movieButton")

        self.attractionButton = QtWidgets.QPushButton(self.centralwidget1)
        self.attractionButton.setGeometry(QtCore.QRect(480, 500, 160, 60))
        self.attractionButton.setObjectName("attractionButton")

        self.RestaurantButton = QtWidgets.QPushButton(self.centralwidget1)
        self.RestaurantButton.setGeometry(QtCore.QRect(640, 500, 160, 60))
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

        self.centralwidget2 = QtWidgets.QWidget(MainWindow)
        self.centralwidget2.setObjectName("centralwidget2")
        self.testLabel = QtWidgets.QLabel(self.centralwidget2)
        self.testLabel.setGeometry(QtCore.QRect(246, 152, 411, 201))
        self.testLabel.setObjectName("testLabel")

        self.Stack.addWidget(self.centralwidget1)
        self.Stack.addWidget(self.centralwidget2)
        self.Stack.addWidget(self.reviewcentralwidget)
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
        #############################################

        self.mybackendHotel = backendHotel()
        self.mybackendAttraction = backendAttraction()

        self.sortButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)

        # UPDATED. DYNAMIC SORT MENU
        self.hotelButton.clicked.connect(self.bufferFuncHotel)
        self.attractionButton.clicked.connect(self.sortMenuItemsAttraction)

    def bufferFuncHotel(self):
        self.sortMenuItemsHotel()
        self.listWidget.itemClicked.connect(self.test)
        self.listWidget.itemSelectionChanged.connect(self.selectionChanged)

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
        sortMenu.addAction(durationAscAction)
        sortMenu.addAction(durationDescAction)
        sortMenu.addSeparator()
        sortMenu.addAction(startTimeAscAction)
        sortMenu.addAction(startTimeDescAction)
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
        print('In Overview')
        self.Stack.setCurrentWidget(self.centralwidget1)

    def selectionChanged(self):
        tempCustomQWidget = self.listWidget.itemWidget(
            self.listWidget.selectedItems()[0])
        test = tempCustomQWidget.hotelNameLabel
        self.testLabel.setText(test.text())
        self.Stack.setCurrentWidget(self.centralwidget2)
        print(test.text())

    def test(self):
        if(self.clicked == False):
            print('clicked')
        self.clicked = True

    def setHotel(self, rating=0):
        self.hotels = self.mybackendHotel.gethotelbyrating(rating)
        self.listWidget.clear()
        for name, hid, loc, avg_price, booked, rating in self.hotels:
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextOnAllLabel(
                'Name : ' + name, 'Avg. Rating : '+rating, 'Locality : '+loc, 'Avg. Price : '+avg_price, 'Booked : '+booked)
            listWidgetItem = QtWidgets.QListWidgetItem(self.listWidget)
            listWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # self.listWidget.itemClicked.connect(self.test())
            self.listWidget.addItem(listWidgetItem)
            self.listWidget.setItemWidget(listWidgetItem, myQCustomQWidget)

    def setHotelPrice(self, price):
        self.hotels = self.mybackendHotel.gethotelbyprice(price)
        self.listWidget.clear()
        for name, hid, loc, avg_price, booked, rating in self.hotels:
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextOnAllLabel(
                'Name : ' + name, 'Avg. Rating : '+rating, 'Locality : '+loc, 'Avg. Price : '+avg_price, 'Booked : '+booked)
            listWidgetItem = QtWidgets.QListWidgetItem(self.listWidget)
            listWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # self.listWidget.itemClicked.connect(self.test())
            self.listWidget.addItem(listWidgetItem)
            self.listWidget.setItemWidget(listWidgetItem, myQCustomQWidget)


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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
