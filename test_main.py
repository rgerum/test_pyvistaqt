print("start")
import sys
from qtpy import QtWidgets
from pyvistaqt import QtInteractor

def test_pyvista():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow(None)
    QtInteractor(window)
    print("success")
