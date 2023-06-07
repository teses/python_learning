from PyQt5 import QtWidgets, uic
import sys
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import matplotlib

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Ui(QtWidgets.QMainWindow):
    plotcontainer = ""
    plotwidget = ""

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('../ui/mathplot.ui', self)

        # pyqtgraph
        self.plotwidget = pg.PlotWidget()
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        self.plotwidget.plot(hour, temperature)
        # plot data: x, y values
        self.graphContainer2.addWidget(self.plotwidget)


        # matplotlib
        sc = MplCanvas(self, width=5, height=4, dpi=120)
        sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        sc.resize(100,100)
        self.graphContainer.addWidget(sc)







app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
sys.exit(app.exec_())

