def bin_search_closest(ss,x):
    if ss == []:
        return None
    low = 0
    high = highest = len(ss) - 1
    while low <= high:
        mid = (high + low) // 2
        if x == ss[mid]:
            return mid
        elif x < ss[mid]:
            high = mid - 1
        else:
            low = mid + 1
    # Write your code that determine the closest index 
    # when searching fails.








