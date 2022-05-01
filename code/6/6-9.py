def bin_search_OX(ss,x):
    if ss != []:
        mid = len(ss) // 2
        if x == ss[mid]:
            return True
        elif x < ss[mid]:
            return bin_search_OX(ss[:mid],x)
        else:
            return bin_search_OX(ss[mid+1:],x)
    else:
        return False

# Test code
s = [3,5,8,7,4,6,1,9,2]
s.sort()
print(bin_search_OX(s,5))
print(bin_search_OX(s,8))
print(bin_search_OX(s,1))
print(bin_search_OX(s,11))