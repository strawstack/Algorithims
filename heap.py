class Heap:

    def __init__(self, compare = None):
        if compare == None:
            compare = lambda a, b: a < b

        self.lst = []
        self.compare = compare
    
    def pushItem(self, item):
        self.lst.append(item)
        self.upHeap(len(self.lst) - 1)

    def popItem(self):
        if len(self.lst) == 0:
            return None

        lastIndex = len(self.lst) - 1
        
        temp = self.lst[0]
        self.lst[0] = self.lst[lastIndex]
        self.lst[lastIndex] = temp
        
        value = self.lst.pop()
        self.downHeap(0)
        return value

    def heapify(self):        
        for i in range(len(lst) - 1, -1, -1):
            self.upHeap(i)
    
    def downHeap(self, index):
        leftIndex = (2 * index) + 1
        rightIndex = (2 * index) + 2

        if leftIndex >= len(self.lst):
            return None

        swapIndex = leftIndex
        if rightIndex < len(self.lst):
            swapIndex = leftIndex if self.compare(self.lst[leftIndex], self.lst[rightIndex]) else rightIndex

        if self.compare(self.lst[swapIndex], self.lst[index]):
            temp = self.lst[index]
            self.lst[index] = self.lst[swapIndex]
            self.lst[swapIndex] = temp
            self.downHeap(swapIndex)

    def upHeap(self, index):
        if index == 0:
            return None
        
        parentIndex = (index - 1) // 2
        if self.compare(self.lst[index], self.lst[parentIndex]):
            temp = self.lst[parentIndex]
            self.lst[parentIndex] = self.lst[index]
            self.lst[index] = temp
            self.upHeap(parentIndex)

class HeapWithDecreaseKey:

    def __init__(self, compare = None, hashItem = None):
        if compare == None:
            compare = lambda a, b: a < b

        if hashItem == None:
            hashItem = lambda x: x

        self.lst = []
        self.lookup = {}
        self.compare = compare
        self.hashItem = hashItem
    
    def pushItem(self, item):
        self.lst.append(item)
        self.lookup[self.hashItem(item)] = len(self.lst) - 1
        self.upHeap(len(self.lst) - 1)

    def popItem(self):
        if len(self.lst) == 0:
            return None

        lastIndex = len(self.lst) - 1
        
        temp = self.lst[0]
        self.lst[0] = self.lst[lastIndex]
        self.lst[lastIndex] = temp

        self.lookup[self.hashItem(self.lst[lastIndex])] = lastIndex
        self.lookup[self.hashItem(self.lst[0])] = 0
        
        item = self.lst.pop()
        del self.lookup[self.hashItem(item)]

        self.downHeap(0)
        
        return item

    def heapify(self):
        for i in range(len(lst) - 1, -1, -1):
            self.upHeap(i)
    
    def downHeap(self, index):
        leftIndex = (2 * index) + 1
        rightIndex = (2 * index) + 2

        if leftIndex >= len(self.lst):
            return None

        swapIndex = leftIndex
        if rightIndex < len(self.lst):
            swapIndex = leftIndex if self.compare(self.lst[leftIndex], self.lst[rightIndex]) else rightIndex

        if self.compare(self.lst[swapIndex], self.lst[index]):
            temp = self.lst[index]
            self.lst[index] = self.lst[swapIndex]
            self.lst[swapIndex] = temp

            self.lookup[self.hashItem(self.lst[index])] = index
            self.lookup[self.hashItem(self.lst[swapIndex])] = swapIndex

            self.downHeap(swapIndex)

    def upHeap(self, index):
        if index == 0:
            return None
        
        parentIndex = (index - 1) // 2
        if self.compare(self.lst[index], self.lst[parentIndex]):
            temp = self.lst[parentIndex]
            self.lst[parentIndex] = self.lst[index]
            self.lst[index] = temp

            self.lookup[self.hashItem(self.lst[parentIndex])] = parentIndex
            self.lookup[self.hashItem(self.lst[index])] = index

            self.upHeap(parentIndex)
    
    def decreaseKey(self, targetKey, itemChangeFunction = None):
        lastIndex = len(self.lst) - 1

        targetItem = targetKey # default item is the key if element not in heap
        if targetKey in self.lookup:
            targetKeyIndex = self.lookup[targetKey]
        
            temp = self.lst[targetKeyIndex]
            self.lst[targetKeyIndex] = self.lst[lastIndex]
            self.lst[lastIndex] = temp

            self.lookup[self.hashItem(self.lst[targetKeyIndex])] = targetKeyIndex
            self.lookup[self.hashItem(self.lst[lastIndex])] = lastIndex

            targetItem = self.lst.pop()
            del self.lookup[self.hashItem(targetItem)]

            self.downHeap(targetKeyIndex)

        if itemChangeFunction == None:
            itemChangeFunction = lambda targetItem: targetItem

        newItem = itemChangeFunction(targetItem)

        self.pushItem(newItem)