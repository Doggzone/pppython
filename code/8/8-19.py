def count_deep(xss):
    counter = 0
    for xs in xss:
        if isinstance(xs,list):
            counter += count_deep(xs)
        else:
            counter += 1
    return counter

# Test code
print(count_deep([1,2,3])) # 3
print(count_deep([1,[],3])) # 2
print(count_deep([1,[1,2,[3,4]]])) # 5
print(count_deep([[[[[[[[1,2,3]]]]]]]])) # 3
print(count_deep([])) # 0
print(count_deep([[[[3]],[4]],5,6,[7]])) # 5
print(count_deep([1,[2,2],[[3],[4,4]],[[[5,5,5,5]]],6,[7,[[8],[[9]]]]])) # 14