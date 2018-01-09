import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QCalendarWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Science Fact Generator"
        # location of window
        self.left = 100
        self.top = 100
        # dimenssions of window
        self.width = 640
        self.height = 480
        # function that initalizes the window
        self.initUI()

    # function to initalize the content of our window
    def initUI(self):
        # window frame attributes
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        #  Generate button
        button = QPushButton('Generate', self)
        button.setToolTip('generate fun fact')
        button.move(100,300)
        # calls onClick function when the button has been pressed
        # The button click (signal) is connected to the action (slot).
        # the method onClick will be called if the signal emits.
        button.clicked.connect(self.onClick)


        # calendar
        self.calendar = QCalendarWidget(self)


        self.show()

    # slot for button click
    @pyqtSlot()
    def onClick(self):
        date = self.calendar.selectedDate()
        print(date.month() ,date.day(),date.year())
# main function that will instantiate our class
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
