def bin_search_OX(ss,x):
    while ss != []:
        mid = len(ss) // 2
        if x == ss[mid]:
            return True
        elif x < ss[mid]:
            ss = ss[:mid]
        else:
            ss = ss[mid+1:]
    return False