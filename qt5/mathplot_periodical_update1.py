"""
Matplotlib in QT5
Periodisches aktualisieren eines Graphen
Infos:
https://www.pythonguis.com/tutorials/plotting-matplotlib/

"""
import sys
import random
import psutil
from PyQt5 import QtWidgets, QtCore, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class CpuGraph():

    def __init__(self, container):
        #self.container = container
        self.canvas = MplCanvas(self, width=2, height=4, dpi=92)
        self.canvas.resize(500, 300)
        container.addWidget(self.canvas)

        n_data = 600
        self.xdata = list(range(n_data))
        self.ydata = [0] * n_data
        self.updateGraph()

    def updateGraph(self):
        # Auslastung der CPU holen
        cpuPercent = psutil.cpu_percent(interval=None,percpu=False)

        self.ydata = self.ydata[1:]  # Drop off the first y element
        self.ydata.append(cpuPercent)  # append a new one.
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.set_xlabel('time (s)')
        self.canvas.axes.plot(self.xdata, self.ydata, 'b')

        #xdata = list(range(50))
        #ydata = [random.randint(0, 100) for i in range(50)]
        #self.canvas.axes.plot(xdata, ydata, 'r')

        #_plot_ref.xlabel('x - axis')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('../ui/mathplot.ui', self)

        #
        self.cpuGraph = CpuGraph(self.graphContainer)

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):

        self.cpuGraph.updateGraph()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
sys.exit(app.exec_())


