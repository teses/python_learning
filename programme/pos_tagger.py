"""
POS-Tagger API
http://eses.name/api_v2/posTagger/?text=Hallo%20(Welt)

Module
    pip install requests

"""
from PyQt5 import QtWidgets, uic
import sys
import requests
import json

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('../ui/postagger.ui', self)

        self.inputText.setPlainText("Dazu gehören alle Prozessschritte, die weder einen freien Puffer noch einen Gesamtpuffer aufweisen.")
        self.btnAnalyzeText.clicked.connect(self.btnAnalyzeTextClick)




    def btnAnalyzeTextClick(self):
        print(self.inputText.toPlainText())
        data = self.callPosApi()
        if(data):
            self.fillTable(data)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Der Satz konnte nicht getaggt werden.")
            #msg.setInformativeText("bla")
            msg.setWindowTitle("Error")
            msg.exec_()


    def fillTable(self, data):
        self.resultTable.setColumnCount(4)
        self.resultTable.setColumnWidth(0, 150)
        self.resultTable.setColumnWidth(1, 50)
        self.resultTable.setColumnWidth(2, 250)
        self.resultTable.setColumnWidth(3, 150)


        #self.resultTable.setItem(0, 0, QtWidgets.QTableWidgetItem("bla"))
        # row cnt
        rowCnt = 0
        for sentence in data:
            for tags in sentence["tagged"]:
                rowCnt += 1
        self.resultTable.setRowCount(rowCnt)

        for sentence in data:
            print(sentence["tagged"])
            row = 0
            for tags in sentence["tagged"]:
                print(tags["token"])
                self.resultTable.setItem(row, 0, QtWidgets.QTableWidgetItem(tags["token"]))
                self.resultTable.setItem(row, 1, QtWidgets.QTableWidgetItem(tags["tag"]))
                self.resultTable.setItem(row, 2, QtWidgets.QTableWidgetItem(tags["tagTitle"]))
                self.resultTable.setItem(row, 3, QtWidgets.QTableWidgetItem(tags["tagExample"]))
                row += 1

        #
        self.resultTable.horizontalHeader().setStretchLastSection(True)
        #self.resultTable.horizontalHeader().setResizeMode(QtWidgets.QHeaderView.Stretch)


    def callPosApi(self):
        text = self.inputText.toPlainText()
        apiUrl = "http://eses.name/api_v2/posTagger/"
        params = {
            "text": text
        }
        response = requests.get(url=apiUrl, params=params)
        data = response.json()
        print(data)
        if data['success'] == 1:
            return data['data']
        return False




app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())