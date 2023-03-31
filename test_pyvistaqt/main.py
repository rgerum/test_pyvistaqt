print("start")
import sys
from qtpy import QtWidgets
from pyvistaqt import QtInteractor

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow(None)
QtInteractor(window)
print("success")
