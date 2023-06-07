from PyQt5 import QtWidgets, uic
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('../../ui/message_windows.ui', self)

        self.btnMessageBoxCritical.clicked.connect(self.btnMessageBoxCriticalClick)
        self.btnMessageBoxInformation.clicked.connect(self.btnMessageBoxInformationClick)
        self.btnMessageBoxWarning.clicked.connect(self.btnMessageBoxWarningClick)
        self.btnMessageBoxQuestion.clicked.connect(self.btnMessageBoxQuestionClick)

        self.btnMessageBoxCriticalShort.clicked.connect(self.btnMessageBoxCriticalShortClick)
        self.btnMessageBoxInformationShort.clicked.connect(self.btnMessageBoxInformationShortClick)
        self.btnMessageBoxWarningShort.clicked.connect(self.btnMessageBoxWarningShortClick)
        self.btnMessageBoxQuestionShort.clicked.connect(self.btnMessageBoxQuestionShortClick)

        self.btnMessageBoxDetailedText.clicked.connect(self.btnMessageBoxDetailedTextClick)
        self.btnMessageBoxAllButtons.clicked.connect(self.btnMessageBoxAllButtonsClick)
        self.btnMessageBoxTest.clicked.connect(self.btnMessageBoxTestClick)


    def btnMessageBoxTestClick(self):
        msg = QtWidgets.QMessageBox()
        msg.setText("Box mit OK, Abbrechen")
        msg.setWindowTitle("Test")
        msg.addButton("OK", QtWidgets.QMessageBox.AcceptRole)
        c = msg.addButton("Abbrechen", QtWidgets.QMessageBox.RejectRole)
        msg.setDefaultButton(c)
        ret = msg.exec()
        print(ret)
        if ret == 0:
            print("OK")
        elif ret == 1:
            print("Abbrechen")
        else:
            print("no button pressed")


    def btnMessageBoxAllButtonsClick(self):
        msg = QtWidgets.QMessageBox()
        msg.setText("Beispiel welche Button es alles gibt.")
        msg.setInformativeText("Beispiel welche Button es alles gibt.")
        msg.setWindowTitle("Alle Buttons")

        msg.setStandardButtons(
            QtWidgets.QMessageBox.Ok |
            QtWidgets.QMessageBox.Save |
            QtWidgets.QMessageBox.SaveAll |
            QtWidgets.QMessageBox.Yes |
            QtWidgets.QMessageBox.YesToAll |
            QtWidgets.QMessageBox.No |
            QtWidgets.QMessageBox.NoToAll |
            QtWidgets.QMessageBox.Discard |
            QtWidgets.QMessageBox.Cancel |
            QtWidgets.QMessageBox.Apply |
            QtWidgets.QMessageBox.Reset |
            QtWidgets.QMessageBox.Abort |
            QtWidgets.QMessageBox.Retry |
            QtWidgets.QMessageBox.Ignore
        )
        msg.addButton("My Button", QtWidgets.QMessageBox.NoRole)
        msg.buttonClicked.connect(self.msgBoxButtonClicked)
        ret = msg.exec()
        print(ret)


    def msgBoxButtonClicked(self, b):
        print("Button clicked", self, b.text())

    def btnMessageBoxDetailedTextClick(self):
        msg = QtWidgets.QMessageBox()
        msg.setText("Eine Messagebox mit Text für detaillierte Informationen")
        msg.setInformativeText("Hier kann weiterer Text stehen")
        msg.setDetailedText("Hier kann weiterer detaillierter Text stehen.\n\nZ.B. weitere Informationen über Fehler oder erweiterte Infos")
        msg.setWindowTitle("setDetailedText()")
        msg.exec()

    def btnMessageBoxCriticalShortClick(self):
        reply = QtWidgets.QMessageBox.critical(
            self,
            "Critical",
            'Ein Fehler',
            QtWidgets.QMessageBox.Ok,
            QtWidgets.QMessageBox.Ok
        )

    def btnMessageBoxInformationShortClick(self):
        reply = QtWidgets.QMessageBox.warning(
            self,
            'Information',
            "Eine Information?",
            QtWidgets.QMessageBox.Ok,
            QtWidgets.QMessageBox.Ok
        )

    def btnMessageBoxWarningShortClick(self):
        reply = QtWidgets.QMessageBox.warning(
            self,
            'Warning',
            "Achtung eine Warnung?",
            QtWidgets.QMessageBox.Ok,
            QtWidgets.QMessageBox.Ok
        )

    def btnMessageBoxQuestionShortClick(self):
        reply = QtWidgets.QMessageBox.question(
            self,
            'Message',
            "Sind sie sicher?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        if reply == QtWidgets.QMessageBox.Yes:
            print("Yes")
        else:
            print("No")

    def btnMessageBoxInformationClick(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Eine Messagebox mit Information Icon")
        msg.setInformativeText("Hier kann weiterer Text stehen")
        msg.setWindowTitle("Information")
        ret = msg.exec()
        if (ret == QtWidgets.QMessageBox.Ok):
            print("clicked OK or windows close Icon")

    def btnMessageBoxCriticalClick(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Eine Messagebox mit Critical Icon")
        msg.setInformativeText("Hier kann weiterer Text stehen")
        msg.setWindowTitle("Critical")
        ret = msg.exec()
        if (ret == QtWidgets.QMessageBox.Ok):
            print("clicked OK or windows close Icon")

    def btnMessageBoxWarningClick(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Eine Messagebox mit Warning Icon")
        msg.setInformativeText("Hier kann weiterer Text stehen")
        msg.setWindowTitle("Warning")
        ret = msg.exec()
        if (ret == QtWidgets.QMessageBox.Ok):
            print("clicked OK or windows close Icon")

    def btnMessageBoxQuestionClick(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setText("Eine Messagebox mit Question Icon")
        msg.setInformativeText("Hier kann weiterer Text stehen")
        msg.setWindowTitle("Question")
        ret = msg.exec()
        if (ret == QtWidgets.QMessageBox.Ok):
            print("clicked OK or windows close Icon")


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
