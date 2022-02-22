from getData import randomIntList
import binarySearch

# binarySearch test
n = 1000
k = 543
lst = list(sorted(randomIntList.getList(n)))
ans = binarySearch.search(lst[k], lst)

if ans != k:
    print("binarySearch: FAIL")
else:
    print("binarySearch: PASS")

# queue

