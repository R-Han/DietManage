foodFile = 'foods.txt'
dietFile = 'diets.txt'

from DietEntry import DietEntry

def addFood(foodEntry):
    f = open(foodFile, 'a+', encoding='utf-8')
    f.seek(0, 2)
    if f.tell() == 0:
        f.write('1|' + foodEntry + '\n')
        f.close()
        return
    f.seek(0, 0)
    for line in f.readlines():
        if line != '\n':
            lastLine = line
        else:
            break
    f.seek(0, 2)
    words = lastLine.split('|')
    order = int(words[0])
    order += 1
    nextOrder = '%d' %order
    f.write(nextOrder + '|' + foodEntry + '\n')
    f.close()

def addDiet(food, info, mode):
    tmp = food.split('|')
    if mode == 0:
        weight = 100.0
        energy = float(tmp[2])
        protein = float(tmp[3])
        fat = float(tmp[4])
        hc = float(tmp[5])
        if float(tmp[6]) > 0:
            price = float(tmp[6])
        else:
            price = 0.0
    else:
        weight = float(tmp[7])
        energy = float(tmp[8])
        protein = float(tmp[9])
        fat = float(tmp[10])
        hc = float(tmp[11])
        if float(tmp[12]) > 0:
            price = float(tmp[12])
        else:
            price = 0.0
    weight = weight * info[4]
    energy = energy * info[4]
    protein = protein * info[4]
    fat = fat * info[4]
    hc = hc * info[4]
    price = price * info[4]
    outLine = '%s|%s|%d|%d|%d|%d|%.2f|%.2f|%.2f|%.2f|%.2f|%.2f\n' %(tmp[0], tmp[1], info[0], info[1], info[2], info[3], weight, energy, protein, fat, hc, price)
    f = open(dietFile, 'a', encoding='utf-8')
    f.write(outLine)
    f.close()

def searchFood(foodName):
    f = open(foodFile, 'r', encoding='utf-8')
    results = []
    for line in f.readlines():
        if len(foodName) == 0:
            results.append(line)
        else:
            if line.find(foodName) >= 0:
                results.append(line)
    f.close()
    return results

def searchDiet(time1, time2, eatTime):
    dietEntries = []
    t1 = time1[0]*400 + time1[1]*32 + time1[2]
    t2 = time2[0]*400 + time2[1]*32 + time2[2]
    f = open(dietFile, 'r', encoding='utf-8')
    for line in f.readlines():
        if line == '\n':
            f.close()
            return dietEntries
        tmp = DietEntry(line)
        t = tmp.year*400 + tmp.month*32 + tmp.day
        if t < t1 or t > t2:
            continue
        if eatTime < 0 or eatTime == tmp.eatTime:
            dietEntries.append(tmp)
    f.close()
    return  dietEntries
