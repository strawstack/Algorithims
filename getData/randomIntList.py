import random

def getList(size):
    lst = []
    for i in range(size):
        lst.append(i + 13)
    random.shuffle(lst)
    return lst

