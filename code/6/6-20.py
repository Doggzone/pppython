def greatest(ns):
    def loop(ns,top):
        if ns != []:
            if ns[0] > top:
                return loop(ns[1:],ns[0])
            else:
                return loop(ns[1:],top)
        else:
            return top
    if len(ns) == 0:
        return None
    else:
        return loop(ns[1:],ns[0])

# Test code
print(greatest([5,2,3,6,4,3,7,5,8,2])) # 8
print(greatest([5,2]))                 # 5
print(greatest([5]))                   # 5
print(greatest([]))                    # None