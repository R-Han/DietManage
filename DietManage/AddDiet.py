from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from FileManage import *
import time

class AddDietFrame(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        grid = QtWidgets.QGridLayout()
        self.searchText = QtWidgets.QLineEdit()
        grid.addWidget(self.searchText, 0, 0, 1, 5)
        self.searchButton = QtWidgets.QPushButton('搜索')
        self.searchButton.clicked.connect(self.search)
        grid.addWidget(self.searchButton, 0, 5, 1, 1)
        self.foodList = QtWidgets.QListWidget()
        grid.addWidget(self.foodList, 1, 0, 5, 2)
        self.foodList.currentItemChanged.connect(self.changeItem)
        self.detailText = QtWidgets.QTextBrowser()
        grid.addWidget(self.detailText, 1, 2, 5, 4)
        self.yearText = QtWidgets.QLineEdit()
        self.monthText = QtWidgets.QLineEdit()
        self.dayText = QtWidgets.QLineEdit()
        self.yearLabel = QtWidgets.QLabel('年')
        self.monthLabel = QtWidgets.QLabel('月')
        self.dayLabel = QtWidgets.QLabel('日')
        self.eatTime = QtWidgets.QComboBox()
        self.eatTime.addItems(['其它', '早餐', '中餐', '晚餐', '加餐', '零食'])
        t = time.localtime()
        self.yearText.setText('%d' %t[0])
        self.monthText.setText('%d' %t[1])
        self.dayText.setText('%d' %t[2])
        timeGrid = QtWidgets.QGridLayout()
        timeGrid.addWidget(self.yearText, 0, 0)
        timeGrid.addWidget(self.yearLabel, 0, 1)
        timeGrid.addWidget(self.monthText, 0, 2)
        timeGrid.addWidget(self.monthLabel, 0, 3)
        timeGrid.addWidget(self.dayText, 0, 4)
        timeGrid.addWidget(self.dayLabel, 0, 5)
        timeGrid.addWidget(self.eatTime, 0, 6)
        self.gramText = QtWidgets.QLineEdit()
        self.gramText.setText('100')
        self.gramLabel = QtWidgets.QLabel('克')
        self.pieceText = QtWidgets.QLineEdit()
        self.pieceText.setText('1')
        self.pieceLabel = QtWidgets.QLabel('份')
        self.saveByGramButton = QtWidgets.QPushButton('按重量保存')
        self.saveByGramButton.clicked.connect(self.saveByGram)
        self.saveByPieceButton = QtWidgets.QPushButton('按份数保存')
        self.saveByPieceButton.clicked.connect(self.saveByPiece)
        buttonGrid = QtWidgets.QGridLayout()
        buttonGrid.addWidget(self.gramText, 0, 0)
        buttonGrid.addWidget(self.gramLabel, 0, 1)
        buttonGrid.addWidget(self.saveByGramButton, 0, 2)
        buttonGrid.addWidget(self.pieceText, 0, 3)
        buttonGrid.addWidget(self.pieceLabel, 0, 4)
        buttonGrid.addWidget(self.saveByPieceButton, 0, 5)
        self.noticeLabel = QtWidgets.QLabel('')

        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addLayout(timeGrid)
        vbox.addLayout(buttonGrid)
        vbox.addWidget(self.noticeLabel, 0, QtCore.Qt.AlignLeft)
        self.setLayout(vbox)

    def search(self):
        foodName = self.searchText.text()
        self.foodItems = searchFood(foodName)
        self.nameList = []
        if len(self.foodItems) == 0:
            self.foodList.clear()
            return
        for foodItem in self.foodItems:
            self.nameList.append(foodItem.split('|')[1])
        self.foodList.clear()
        self.foodList.addItems(self.nameList)
        self.foodList.setCurrentRow(0)
        self.changeItem()

    def saveByGram(self):
        if self.foodList.count() == 0:
            self.noticeLabel.setText('没有项目')
            return
        index = self.foodList.currentRow()
        try:
            year = int(self.yearText.text())
            month = int(self.monthText.text())
            day = int(self.dayText.text())
        except:
            self.noticeLabel.setText('时间错误')
            return
        if max([year, month, day]) < 1 or month > 12:
            self.noticeLabel.setText('时间错误')
            return
        maxDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if day > maxDays[month-1]:
            self.noticeLabel.setText('时间错误')
            return
        if day == 29 and month == 2 and (divmod(year, 4)[1] != 0 or (divmod(year, 100)[1] == 0 and divmod(year, 400)[1] != 0)):
            self.noticeLabel.setText('时间错误')
            return
        inday = self.eatTime.currentIndex()
        try:
            gram = float(self.gramText.text())
        except:
            self.noticeLabel.setText('重量错误')
            return
        if gram < 0:
            self.noticeLabel.setText('重量错误')
            return
        gram = gram/100
        info = [year, month, day, inday, gram]
        addDiet(self.foodItems[index], info, 0)
        self.noticeLabel.setText('添加成功')

    def saveByPiece(self):
        if self.foodList.count() == 0:
            self.noticeLabel.setText('没有项目')
            return
        index = self.foodList.currentRow()
        tmp = self.foodItems[index].split('|')[7]
        if float(tmp) < 0:
            self.noticeLabel.setText('没有每份数据')
            return
        try:
            year = int(self.yearText.text())
            month = int(self.monthText.text())
            day = int(self.dayText.text())
        except:
            self.noticeLabel.setText('时间错误')
            return
        if max([year, month, day]) < 1 or month > 12:
            self.noticeLabel.setText('时间错误')
            return
        maxDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if day > maxDays[month-1]:
            self.noticeLabel.setText('时间错误')
            return
        if day == 29 and month == 2 and (divmod(year, 4)[1] != 0 or (divmod(year, 100)[1] == 0 and divmod(year, 400)[1] != 0)):
            self.noticeLabel.setText('时间错误')
            return
        inday = self.eatTime.currentIndex()
        try:
            piece = float(self.pieceText.text())
        except:
            self.noticeLabel.setText('重量错误')
            return
        if piece < 0:
            self.noticeLabel.setText('重量错误')
            return
        info = [year, month, day, inday, piece]
        addDiet(self.foodItems[index], info, 1)
        self.noticeLabel.setText('添加成功')

    def changeItem(self):
        index = self.foodList.currentRow()
        if index >= 0:
            detail = self.getDetails(self.foodItems[index])
            self.detailText.setText(detail)

    def getDetails(self, line):
        items = line.split('|')
        if float(items[6]) < 0:
            items[6] = ''
            items[12] = ''
        if float(items[7]) < 0:
            items[7:13] = ['', '', '', '', '', '']
        result = '名称：' + items[1] + '\t\t一份重量：' + items[7] + '\n'
        result += '每百克能量(kCal)：' + items[2] + '\t能量：' + items[8] + '\n'
        result += '每百克蛋白质：' + items[3] + '\t\t蛋白质：' + items[9] + '\n'
        result += '每百克脂肪：' + items[4] + '\t\t脂肪：' + items[10] + '\n'
        result += '每百克碳水：' + items[5] + '\t\t碳水：' + items[11] + '\n'
        result += '每百克价格：' + items[6] + '\t\t价格：' + items[12] + '\n'
        return result

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainFrame = AddDietFrame()
    mainFrame.show()
    app.exec_()