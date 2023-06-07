from PyQt5 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui/window_test.ui', self)

        self.btnTest.clicked.connect(self.btnTestClick)
        self.btnAlertBox.clicked.connect(self.btnAlertBoxClick)


    def btnTestClick(self):
        print("hallo")
        self.myLabel.setText("hello")


    def btnAlertBoxClick(self):
        alert = QtWidgets.QMessageBox()
        alert.setText("You clicked the button!")
        alert.exec_()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
sys.exit(app.exec_())
