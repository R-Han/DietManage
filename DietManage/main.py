from PyQt5 import QtWidgets
from PyQt5 import QtGui
from AddDiet import AddDietFrame
from AddFood import AddFoodFrame
from ManageDiet import ManageDietFrame
from Help import HelpFrame

class MainFrame(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle('饮食管理')
        self.setWindowIcon(QtGui.QIcon(':chrome.ico'))
        self.setGeometry(400, 200, 800, 500)
        self.tabs = QtWidgets.QTabWidget(self)
        self.tabs.setGeometry(20, 10, 760, 450)

        self.tab1 = AddDietFrame()
        self.tabs.addTab(self.tab1, '记录饮食')
        self.tab2 = AddFoodFrame()
        self.tabs.addTab(self.tab2, '添加食品')
        self.tab3 = ManageDietFrame()
        self.tabs.addTab(self.tab3, '管理饮食')
        self.tab4 = HelpFrame()
        self.tabs.addTab(self.tab4, '帮助')
        self.tabs.setCurrentIndex(0)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainFrame = MainFrame()
    mainFrame.show()
    app.exec_()