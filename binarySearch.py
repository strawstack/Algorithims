def search(item, lst):
    
    lo = 0
    hi = len(lst) - 1
    mid = (lo + hi) // 2

    while lo <= hi:

        mid = (lo + hi) // 2

        if lst[mid] == item:
            return mid

        elif lst[mid] < item:
            lo = mid + 1
        
        else: # item < lst[mid]
            hi = mid - 1
    
    return mid