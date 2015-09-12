__author__ = 'Defron'

import sys
from PyQt4 import QtCore, QtGui, uic


class MyWidget(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        uic.loadUi('mainWindow.ui', self)


if(__name__ == '__main__'):
    app = QtGui.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    app.exec_()