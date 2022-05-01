def updown(ns):
    if ns != []:
        if ns[0] % 2 == 0:
            return [ns[0]//2] + updown(ns[1:])
        else:
            return [ns[0]*2] + updown(ns[1:])
    else:
        return []

# Test code
print(updown([4, 6,  5, 3,  7, 6, 2, 1, 3, 2]))
#            [2, 3, 10, 6, 14, 3, 1, 2, 6, 1]
print(updown([14, 69, 87, 13, 0, 16, 83, 19, 45, 88]))
#            [7, 138, 174, 26, 0, 8, 166, 38, 90, 44]