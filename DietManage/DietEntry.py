class DietEntry():
    def __init__(self, line):
        items = line.split('|')
        self.name = items[1]
        self.year = int(items[2])
        self.month = int(items[3])
        self.day = int(items[4])
        self.eatTime = int(items[5])
        self.weight = float(items[6])
        self.energy = float(items[7])
        self.protein = float(items[8])
        self.fat = float(items[9])
        self.hc = float(items[10])
        self.price = float(items[11])

    def shortPrint(self):
        eatTimes = ['其它', '早餐', '中餐', '晚餐', '加餐', '零食']
        result = ''
        result = result + ('%d' %self.year) + '年'
        result = result + ('%d' %self.month) + '月'
        result = result + ('%d' %self.day) + '日'
        result = result + eatTimes[self.eatTime] + '：'
        result = result + self.name + '：'
        result = result + ('%.2f' %self.weight) + '克，能量'
        result = result + ('%.2f' %self.energy) + '千卡'
        return result

def keyDiet(dietEntry):
    key = (dietEntry.year*400 + dietEntry.month*32 + dietEntry.day) * 10 + dietEntry.eatTime
    return key