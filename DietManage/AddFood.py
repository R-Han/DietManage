from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from FoodEntry import FoodEntry
from FileManage import *

class AddFoodFrame(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        grid = QtWidgets.QGridLayout()
        labelNames = ['名称*:', '每百克能量(kCal)*:', '每百克蛋白质*:', '每百克脂肪*:', '每百克碳水*:', '每百克价格:',
                      '一份重量(g):', '能量:', '蛋白质:', '脂肪:', '碳水:', '价格:']
        pos = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2)]
        self.texts = {}
        for i in range(len(labelNames)):
            grid.addWidget(QtWidgets.QLabel(labelNames[i]), pos[i][0], pos[i][1], QtCore.Qt.AlignRight)
            self.texts[i] = QtWidgets.QLineEdit()
            grid.addWidget(self.texts[i], pos[i][0], pos[i][1]+1, QtCore.Qt.AlignLeft)
        self.button1 = QtWidgets.QPushButton('反向计算')
        self.button2 = QtWidgets.QPushButton('计算')
        self.button1.clicked.connect(self.button1Clicked)
        self.button2.clicked.connect(self.button2Clicked)
        grid.addWidget(self.button1, 6, 1, QtCore.Qt.AlignLeft)
        grid.addWidget(self.button2, 6, 3, QtCore.Qt.AlignLeft)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(grid)
        self.addButton = QtWidgets.QPushButton('添加')
        self.addButton.clicked.connect(self.addButtonClicked)
        vbox.addWidget(self.addButton, 0, QtCore.Qt.AlignHCenter)
        self.noticeLabel = QtWidgets.QLabel('')
        vbox.addWidget(self.noticeLabel, 0, QtCore.Qt.AlignLeft)
        self.setLayout(vbox)

    def button1Clicked(self):
        try:
            gram = float(self.texts[6].text())
        except:
            self.noticeLabel.setText('每份重量错误')
            return
        try:
            energy = float(self.texts[7].text())
            protein = float(self.texts[8].text())
            fat = float(self.texts[9].text())
            hc = float(self.texts[10].text())
            if len(self.texts[11].text()) > 0:
                price = float(self.texts[11].text())
        except:
            self.noticeLabel.setText('每百克数据错误')
            return
        energy = energy / gram * 100
        protein = protein / gram * 100
        fat = fat / gram * 100
        hc = hc / gram * 100
        if len(self.texts[11].text()) > 0:
            price = price / gram * 100

        self.texts[1].setText(('%.2f' %energy))
        self.texts[2].setText(('%.2f' %protein))
        self.texts[3].setText(('%.2f' %fat))
        self.texts[4].setText(('%.2f' %hc))
        if len(self.texts[11].text()) > 0:
            self.texts[5].setText(('%.2f' %price))

    def button2Clicked(self):
        try:
            gram = float(self.texts[6].text())
        except:
            self.noticeLabel.setText('每份重量错误')
            return
        try:
            energy = float(self.texts[1].text())
            protein = float(self.texts[2].text())
            fat = float(self.texts[3].text())
            hc = float(self.texts[4].text())
            if len(self.texts[5].text()) > 0:
                price = float(self.texts[5].text())
        except:
            self.noticeLabel.setText('每百克数据错误')
            return
        energy = energy * gram / 100
        protein = protein * gram / 100
        fat = fat * gram / 100
        hc = hc * gram / 100
        if len(self.texts[5].text()) > 0:
            price = price * gram / 100
        self.texts[7].setText(('%.2f' %energy))
        self.texts[8].setText(('%.2f' %protein))
        self.texts[9].setText(('%.2f' %fat))
        self.texts[10].setText(('%.2f' %hc))
        if len(self.texts[5].text()) > 0:
            self.texts[11].setText(('%.2f' %price))

    def addButtonClicked(self):
        newEntry = FoodEntry()
        tmp = newEntry.setEntry(self.texts[0].text(), self.texts[1].text(), self.texts[2].text(), self.texts[3].text(), self.texts[4].text(), self.texts[5].text(),
                                self.texts[6].text(), self.texts[7].text(), self.texts[8].text(), self.texts[9].text(), self.texts[10].text(), self.texts[11].text())
        if len(tmp) > 0:
            self.noticeLabel.setText(tmp)
        else:
            addFood(newEntry.printEntry())
            self.noticeLabel.setText('添加成功')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainFrame = AddFoodFrame()
    mainFrame.show()
    app.exec_()