from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from FileManage import *
from DietEntry import keyDiet
import time

class ManageDietFrame(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        grid = QtWidgets.QGridLayout()
        (self.fromLabel, self.yearLabel1, self.monthLabel1, self.dayLabel1) = (QtWidgets.QLabel('从'), QtWidgets.QLabel('年'), QtWidgets.QLabel('月'), QtWidgets.QLabel('日'))
        (self.toLabel, self.yearLabel2, self.monthLabel2, self.dayLabel2) = (QtWidgets.QLabel('到'), QtWidgets.QLabel('年'), QtWidgets.QLabel('月'), QtWidgets.QLabel('日'))
        (self.yearText1, self.monthText1, self.dayText1) = (QtWidgets.QLineEdit(), QtWidgets.QLineEdit(), QtWidgets.QLineEdit())
        (self.yearText2, self.monthText2, self.dayText2) = (QtWidgets.QLineEdit(), QtWidgets.QLineEdit(), QtWidgets.QLineEdit())
        t = time.localtime()
        self.yearText1.setText('%d' %t[0])
        self.monthText1.setText('%d' %t[1])
        self.dayText1.setText('%d' %t[2])
        self.yearText2.setText('%d' %t[0])
        self.monthText2.setText('%d' %t[1])
        self.dayText2.setText('%d' %t[2])
        grid.addWidget(self.fromLabel, 0, 0, 1, 1)
        grid.addWidget(self.yearText1, 0, 1, 1, 2)
        grid.addWidget(self.yearLabel1, 0, 3, 1, 1)
        grid.addWidget(self.monthText1, 0, 4, 1, 2)
        grid.addWidget(self.monthLabel1, 0, 6, 1, 1)
        grid.addWidget(self.dayText1, 0, 7, 1, 2)
        grid.addWidget(self.dayLabel1, 0, 9, 1, 1)
        grid.addWidget(self.toLabel, 1, 0, 1, 1)
        grid.addWidget(self.yearText2, 1, 1, 1, 2)
        grid.addWidget(self.yearLabel2, 1, 3, 1, 1)
        grid.addWidget(self.monthText2, 1, 4, 1, 2)
        grid.addWidget(self.monthLabel2, 1, 6, 1, 1)
        grid.addWidget(self.dayText2, 1, 7, 1, 2)
        grid.addWidget(self.dayLabel2, 1, 9, 1, 1)

        self.eatTime = QtWidgets.QComboBox()
        self.eatTime.addItems(['其它', '早餐', '中餐', '晚餐', '加餐', '零食', '所有'])
        self.eatTime.setCurrentIndex(6)
        self.searchButton = QtWidgets.QPushButton('查找')
        self.searchButton.clicked.connect(self.search)
        grid.addWidget(self.eatTime, 2, 0, 1, 2)
        grid.addWidget(self.searchButton, 2, 2, 1, 1)
        self.dietList = QtWidgets.QListWidget()
        grid.addWidget(self.dietList, 3, 0, 5, 10)

        self.sumLabel = QtWidgets.QLabel('总计：')
        self.aveLabel = QtWidgets.QLabel('日均：')
        self.noticeLabel = QtWidgets.QLabel('')

        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addWidget(self.sumLabel, 0, QtCore.Qt.AlignLeft)
        vbox.addWidget(self.aveLabel, 0, QtCore.Qt.AlignLeft)
        vbox.addWidget(self.noticeLabel, 0, QtCore.Qt.AlignLeft)
        self.setLayout(vbox)

    def search(self):
        try:
            year1 = int(self.yearText1.text())
            month1 = int(self.monthText1.text())
            day1 = int(self.dayText1.text())
            year2 = int(self.yearText2.text())
            month2 = int(self.monthText2.text())
            day2 = int(self.dayText2.text())
        except:
            self.clearNotice('日期不正确')
            return
        if not self.checkTime([year1, month1, day1], [year2, month2, day2]):
            self.clearNotice('日期不正确')
            return
        eatTime = self.eatTime.currentIndex()
        if eatTime == 6: eatTime = -1
        dietEntries = searchDiet([year1, month1, day1], [year2, month2, day2], eatTime)
        if len(dietEntries) == 0:
            self.clearNotice('没有找到任何记录')
            return
        self.clearNotice('')
        dietEntries.sort(key=keyDiet, reverse=True)

        sumData = [0, 0, 0, 0, 0]
        listEntires = []
        days = []
        for entry in dietEntries:
            listEntires.append(entry.shortPrint())
            t = entry.year*400 + entry.month*32 + entry.day
            if not t in days:
                days.append(t)
            sumData[0] += entry.energy
            sumData[1] += entry.protein
            sumData[2] += entry.fat
            sumData[3] += entry.hc
            sumData[4] += entry.price
        totDay = len(days)
        aveData = [0, 0, 0, 0, 0]
        for i in range(5):
            aveData[i] = sumData[i]/totDay
        self.dietList.addItems(listEntires)
        sumText = '总计：能量：%.2f千卡，蛋白质：%.2f克，脂肪：%.2f克，碳水：%.2f克，价格：%.2f元' %(sumData[0], sumData[1], sumData[2], sumData[3], sumData[4])
        aveText = '日均：能量：%.2f千卡，蛋白质：%.2f克，脂肪：%.2f克，碳水：%.2f克，价格：%.2f元' %(aveData[0], aveData[1], aveData[2], aveData[3], aveData[4])
        self.sumLabel.setText(sumText)
        self.aveLabel.setText(aveText)

    def checkTime(self, time1, time2):
        if max(time1) < 1 or time1[1] > 12:
            return False
        if max(time2) < 1 or time2[1] > 12:
            return False
        maxDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if time1[2] > maxDays[time1[1]-1]:
            return False
        if time2[2] > maxDays[time2[1]-1]:
            return False
        if time1[2] == 29 and time1[1] == 2 and (divmod(time1[0], 4)[1] != 0 or (divmod(time1[0], 100)[1] == 0 and divmod(time1[0], 400)[1] != 0)):
            return False
        if time2[2] == 29 and time2[1] == 2 and (divmod(time2[0], 4)[1] != 0 or (divmod(time2[0], 100)[1] == 0 and divmod(time2[0], 400)[1] != 0)):
            return False
        t1 = 400*time1[0] + 32 * time1[1] + time1[2]
        t2 = 400*time2[0] + 32 * time2[1] + time2[2]
        if t1 > t2:
            return  False
        return True

    def clearNotice(self, notice):
        self.noticeLabel.setText(notice)
        self.sumLabel.setText('总计：')
        self.aveLabel.setText('日均：')
        if self.dietList.count() > 0:
            self.dietList.clear()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainFrame = ManageDietFrame()
    mainFrame.show()
    app.exec_()