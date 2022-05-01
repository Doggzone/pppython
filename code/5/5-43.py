def reduce_diff(ns):
    if len(ns) > 1:
        if ns[0] < ns[1]:
            return [ns[0]+1] + reduce_diff(ns[1:])
        elif ns[0] > ns[1]:
            return [ns[0]-1] + reduce_diff(ns[1:])
        else:
            return [ns[0]] + reduce_diff(ns[1:])
    else:
        return ns

# Test code
print(reduce_diff([4, 6, 5, 3, 7, 6, 2, 1, 3, 2]))
#                 [5, 5, 4, 4, 6, 5, 1, 2, 2, 2]
print(reduce_diff([5, 4, 4, 5, 5, 4, 2, 2, 2, 2]))
#                 [4, 4, 5, 5, 4, 3, 2, 2, 2, 2]
print(reduce_diff([4, 3, 2, 2, 2, 2, 2, 2, 2, 2]))
#                 [3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(reduce_diff([3, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#                 [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(reduce_diff([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#                 [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]