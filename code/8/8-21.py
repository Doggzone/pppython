def flatten(xss):
    flat = []
    pass  # Write your for-loop here.
    return flat

# Test code
print(flatten([])) # []
print(flatten([1,2,3])) # [1, 2, 3]
print(flatten([1,[],3])) # [1, 3]
print(flatten([1,[1,2,[3,4]]])) # [1, 1, 2, 3, 4]
print(flatten([[[[[[[[1,2,3]]]]]]]])) # [1, 2, 3]
print(flatten([[[[3]],[4]],5,6,[7]])) # [3, 4, 5, 6, 7]
print(flatten([1,[2,2],[[3],[4,4]],[[[5,5,5,5]]],6,[7,[[8],[[9]]]]])) 
# [1, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 9]