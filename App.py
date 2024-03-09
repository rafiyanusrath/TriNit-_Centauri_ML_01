from PyQt5.QtWidgets import QApplication, QMainWindow
from Rtmui import Ui_RTM
 
class MyMainWindow(QMainWindow):
    def __init__(self):

        super(MyMainWindow, self).__init__()
        self.setWindowOpacity(0.95)
        self.ui = Ui_RTM()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    main_window = MyMainWindow()
    main_window.setStyleSheet(open("Styles/style.css").read())
    main_window.show()
    app.exec_()
