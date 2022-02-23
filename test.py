from getData import randomIntList
import binarySearch
from queue import Queue
from getData import binaryTree
from treeTraversal import TreeTraversal
from breadthFirstSearch import BreadthFirstSearch
from depthFirstSearch import DepthFirstSearch

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



# tests complete
print("testing complete.")