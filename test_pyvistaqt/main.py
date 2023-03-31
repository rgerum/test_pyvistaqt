from qtpy import QtWidgets
from pyvistaqt import QtInteractor

app = QtWidgets.QApplication([])
window = QtWidgets.QMainWindow()
QtInteractor(window)
