class FoodEntry():
    def __init__(self):
        pass

    def setEntry(self, name, energy100, protein100, fat100, hc100, price100,
                 weight, energy, protein, fat, hc, price):
        if name == '': return '名称必须填写'
        if name.find('|') > 0: return '名称不符合规范（包含|）'
        self.name = name
        try:
            self.energy100 = float(energy100)
            self.protein100 = float(protein100)
            self.fat100 = float(fat100)
            self.hc100 = float(hc100)
        except:
            return '存在不正确的数字'
        if len(price100) > 0:
            try:
                self.price100 = float(price100)
            except:
                return '存在不正确的数字'
        else: self.price100 = -1.0;
        if len(weight) > 0:
            try:
                self.weight = float(weight)
                self.energy = float(energy)
                self.protein = float(protein)
                self.fat = float(fat)
                self.hc = float(hc)
                if self.price100 >= 0:
                    self.price = float(price)
                else:
                    self.price = -1.0
            except:
                return '存在不正确的数字'
        else:
            self.weight = -1.0
            self.energy = -1.0
            self.protein = -1.0
            self.fat = -1.0
            self.hc = -1.0
            self.price = -1.0
        return ''

    def printEntry(self):
        s = ''
        s = s + self.name + '|'
        tmp = '%.2f|%.2f|%.2f|%.2f|%.2f' %(self.energy100, self.protein100, self.fat100, self.hc100, self.price100)
        s = s + tmp + '|'
        tmp = '%.2f|%.2f|%.2f|%.2f|%.2f|%.2f' %(self.weight, self.energy, self.protein, self.fat, self.hc, self.price)
        s = s + tmp
        return s