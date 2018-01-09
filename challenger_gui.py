import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Science Fact Generator"
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    # function to initalize the content of our window
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

# main function that will instantiate our class
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
