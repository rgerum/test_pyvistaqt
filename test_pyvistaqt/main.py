from qtpy import QtCore, QtWidgets, QtGui
from pyvistaqt import QtInteractor

app = QtWidgets.QApplication([])
window = QtWidgets.QMainWindow()
print("ho")
import pyvista as pv
p = pv.Plotter(off_screen=True)
p.add_mesh(pv.Cylinder(), color="tan", show_edges=True)
p.show(screenshot="test.png")
print("hu")

#QtInteractor(window, auto_update=False)
