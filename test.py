from getData import randomIntList
import binarySearch
from queue import Queue
from getData import binaryTree
from treeTraversal import TreeTraversal
from breadthFirstSearch import BreadthFirstSearch
from depthFirstSearch import DepthFirstSearch
from heap import * # Heap, HeapWithDecreaseKey
from dijkstrasShortestPath import * # DijkstrasShortestPath, DijkstrasShortestPathWithDecreaseKey

#
# binarySearch
#

lstLength = 1000
searchIndex = 543
lst = list(sorted(randomIntList.getList(lstLength)))
ans = binarySearch.search(lst[searchIndex], lst)

if ans != searchIndex:
    print("binarySearch: FAIL")

#
# queue
#

q = Queue()
q.push(3)
q.push(4)
q.push(5)
a = q.pop()
b = q.pop()
c = q.pop()

if a != 3 or b != 4 or c != 5:
    print("queue: FAIL")

#
# tree traversal
#

# create tree height 3
height = 3
root = binaryTree.getTree(height)
tt = TreeTraversal()
tt.lst = [] # clear list
tt.inOrder(root)
inOrderList = tt.lst # get inOrder list

# assign correct values for in order
count = 0
for n in inOrderList:
    n.value = count
    count += 1

# obtain pre-order list 
tt.lst = []
tt.preOrder(root)
preOrderList = tt.lst

# verify correct values are returned by preorder
checkList = [3, 1, 0, 2, 5, 4, 6]
preOrderAns = list(map(lambda x: x.value, preOrderList))
for i in range(len(checkList)):
    if preOrderAns[i] != checkList[i]:
        print("tree traversal: FAIL")
        break

# obtain post-order list 
tt.lst = []
tt.postOrder(root)
postOrderList = tt.lst

# verify correct values are returned by post-order
checkList = [0, 2, 1, 4, 6, 5, 3]
postOrderAns = list(map(lambda x: x.value, postOrderList))
for i in range(len(checkList)):
    if postOrderAns[i] != checkList[i]:
        print("tree traversal: FAIL")
        break

#
# breadthFirstSearch
#

height = 5
root = binaryTree.getTree(height)

tt.lst = [] # clear list
tt.inOrder(root)
inOrderList = tt.lst # get inOrder list

# assign correct values for in order
count = 0
for n in inOrderList:
    n.value = count
    count += 1

bfs = BreadthFirstSearch()
bfsList = bfs.search(root)

checkList = [15, 7, 23, 3, 11, 19, 27, 1, 5, 9, 13, 17, 21, 25, 29, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
bfsList = list(map(lambda x: x.value, bfsList))

for i in range(len(checkList)):
    if bfsList[i] != checkList[i]:
        print("breadth first search: FAIL")
        break

#
# depthFirstSearch
#

height = 8
root = binaryTree.getTree(height)

tt.lst = [] # clear list
tt.inOrder(root)
inOrderList = tt.lst # get inOrder list

# assign correct values for in order
count = 0
for n in inOrderList:
    n.value = count
    count += 1

dfs = DepthFirstSearch()
dfs.search(root, 25)

checkList = [127, 63, 31, 15, 7, 3, 1, 0, 2, 5, 4, 6, 11, 9, 8, 10, 13, 12, 14, 23, 19, 17, 16, 18, 21, 20, 22, 27, 25]
dfsList = dfs.lst

for i in range(len(checkList)):
    if dfsList[i] != checkList[i]:
        print("depth first search: FAIL")
        break

#
# heap
#

h = Heap()

h.pushItem(7)
h.pushItem(1)
h.pushItem(5)
h.pushItem(6)
h.pushItem(10)
h.pushItem(4)
h.pushItem(3)

ans = []
while len(h.lst) > 0:
    item = h.popItem()
    ans.append(item)

checkList = [1, 3, 4, 5, 6, 7, 10]
if ans != checkList:
    print("heap: FAIL")

#
# heapWithDecreaseKey
#

def HeapWithDecreaseKey_compareItems(a, b):
    return a[0] < b[0]

def HeapWithDecreaseKey_hashItem(a):
    return a[1]

h = HeapWithDecreaseKey(HeapWithDecreaseKey_compareItems, HeapWithDecreaseKey_hashItem)

h.pushItem([7, 111])
h.pushItem([1, 222])
h.pushItem([5, 333])
h.pushItem([6, 444])

def HeapWithDecreaseKey_itemChangeFunction(oldItem):
    newItem = [
        oldItem[0] - 5,
        oldItem[1]
    ]
    return newItem

h.decreaseKey(333, HeapWithDecreaseKey_itemChangeFunction)

ans = []
while len(h.lst) > 0:
    item = h.popItem()
    ans.append(item)

checkList = [[0, 333], [1, 222], [6, 444], [7, 111]]

for i in range(len(checkList)):
    if ans[i][0] != checkList[i][0] or ans[i][1] != checkList[i][1]:
        print("heapWithDecreaseKey: FAIL")
        break

#
# dijkstrasShortestPath
#
testGraph = [
    [],                                 # 0
    [[2, 7], [3, 9], [6, 14]],          # 1
    [[1, 7], [3, 10], [4, 15]],         # 2
    [[1, 9], [2, 10], [4, 11], [6, 2]], # 3
    [[2, 15], [3, 11], [5, 6]],         # 4
    [[4, 6], [6, 9]],                   # 5
    [[1, 14], [3, 2], [5, 9]]           # 6
]

dijk = DijkstrasShortestPath()
path = dijk.findPath(1, 5, testGraph)

checkList = [1, 3, 6, 5]

if path != checkList:
    print("dijkstrasShortestPath: FAIL")

#
# dijkstrasShortestPathWithDecreaseKey
#
testGraph = [
    [],                                 # 0
    [[2, 7], [3, 9], [6, 14]],          # 1
    [[1, 7], [3, 10], [4, 15]],         # 2
    [[1, 9], [2, 10], [4, 11], [6, 2]], # 3
    [[2, 15], [3, 11], [5, 6]],         # 4
    [[4, 6], [6, 9]],                   # 5
    [[1, 14], [3, 2], [5, 9]]           # 6
]

dijk = DijkstrasShortestPathWithDecreaseKey()
path = dijk.findPath(1, 5, testGraph)

checkList = [1, 3, 6, 5]

if path != checkList:
    print("dijkstrasShortestPath: FAIL")

# tests complete
print("testing complete.")