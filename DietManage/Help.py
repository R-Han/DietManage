from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

class HelpFrame(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        grid = QtWidgets.QGridLayout()
        self.noticeLabel = QtWidgets.QLabel('并没有什么帮助')

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.noticeLabel, 0, QtCore.Qt.AlignTop)
        self.setLayout(vbox)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainFrame = HelpFrame()
    mainFrame.show()
    app.exec_()