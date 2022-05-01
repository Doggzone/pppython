def drop_before(s,index):
    if s != [] and index > 0:
        return drop_before(s[1:],index-1)
    else:
        return s

# Test code
s = [1,2,3,4,5]
print(drop_before(s,0))  # [1, 2, 3, 4, 5]
print(drop_before(s,1))  # [2, 3, 4, 5]
print(drop_before(s,2))  # [3, 4, 5]
print(drop_before(s,3))  # [4, 5]
print(drop_before(s,4))  # [5]
print(drop_before(s,5))  # []
print(drop_before(s,6))  # []
print(drop_before(s,-3)) # [1, 2, 3, 4, 5]
print(drop_before([],4)) # []