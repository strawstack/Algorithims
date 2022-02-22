from getData import randomIntList
import binarySearch
from queue import Queue
from getData import inOrderBinaryTree
from treeTraversal import TreeTraversal

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
root = inOrderBinaryTree.getTree(height)
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
root = inOrderBinaryTree.getTree(height)











# tests complete
print("testing complete.")