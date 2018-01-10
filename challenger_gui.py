import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QCalendarWidget,QMessageBox,QLineEdit,QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import webscraper
from calendar import monthrange


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Science Fact Generator"
        # location of window
        self.left = 100
        self.top = 100
        # dimenssions of window
        self.width = 800
        self.height = 800
        # function that initalizes the window
        self.initUI()
        self.data = webscraper.webscraper()
        # print(self.data.genFactList(1,1))

    # function to initalize the content of our window
    def initUI(self):
        # window frame attributes
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        #  Generate button
        button = QPushButton('Generate', self)
        button.setToolTip('generate fun fact')
        button.setFixedSize(100,100)
        button.move(100,300)
        # calls onClick function when the button has been pressed
        # The button click (signal) is connected to the action (slot).
        # the method onClick will be called if the signal emits.
        button.clicked.connect(self.onClick)

        # Month Combo Box
        comboBox = QComboBox(self)
        comboBox.move(100,100)
        comboBox.addItem("January")
        comboBox.addItem("Febuary")
        comboBox.addItem("March")
        comboBox.addItem("April")
        comboBox.addItem("May")
        comboBox.addItem("June")
        comboBox.addItem("July")
        comboBox.addItem("August")
        comboBox.addItem("September")
        comboBox.addItem("October")
        comboBox.addItem("November")
        comboBox.addItem("December")
        comboBox.activated[str].connect(self.monthSelected)

        self.dayComboBox = QComboBox(self)
        self.dayComboBox.move(250,100)
        maxday = monthrange(2012,1)[1]
        days = [str(x) for x in range(1,maxday)]
        self.dayComboBox.addItems(days)

        self.show()

    # slot for button click
    @pyqtSlot()
    def onClick(self):
        date = self.calendar.selectedDate()
        print(date.month() ,date.day(),date.year())
        print(self.data.factList)

    def monthSelected(self,month):
        self.dayComboBox.clear()
        maxday = monthrange(2012,self.monthToInt(month))[1]
        days = [str(x) for x in range(1,maxday)]
        self.dayComboBox.clear()
        self.dayComboBox.addItems(days)
        print(month)


    # returns integer version of coresponding month
    def monthToInt(self, month):
        if month == "January":
            return 1
        elif month == "Febuary":
            return 2
        elif month == "March":
            return 3
        elif month == "April":
            return 4
        elif month == "May":
            return 5
        elif month == "June":
            return 6
        elif month == "July":
            return 7
        elif month == "August":
            return 8
        elif month == "September":
            return 9
        elif month == "October":
            return 10
        elif month == "November":
            return 11
        else:
            return 12

# main function that will instantiate our class
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
