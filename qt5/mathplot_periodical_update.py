"""
Matplotlib in QT5
Periodisches aktualisieren eines GRaphen
Infos:
https://www.pythonguis.com/tutorials/plotting-matplotlib/

"""
import sys
import random
from PyQt5 import QtWidgets, QtCore, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('../ui/mathplot.ui', self)

        # matplotlib
        self.canvas = MplCanvas(self, width=5, height=4, dpi=120)
        self.graphContainer.addWidget(self.canvas)

        # Data
        n_data = 60
        self.xdata = list(range(n_data))
        #self.xdata = [0] * 50
        print(self.xdata)
        #self.ydata = [random.randint(0, 100) for i in range(n_data)]
        self.ydata = [0] * n_data
        print(self.ydata)
        self.update_plot()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):

        self.ydata = self.ydata[1:] # Drop off the first y element
        self.ydata.append(random.randint(0, 100)) # append a new one.
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()



app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
sys.exit(app.exec_())


