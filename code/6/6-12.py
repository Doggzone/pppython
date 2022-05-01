def bin_search(ss,x):
    low = 0
    high = len(ss) - 1
    while low <= high:
        mid = (high + low) // 2
        if x == ss[mid]:
            return mid
        elif x < ss[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None