def sublists(ns):
	pass # write your code here.

# Test code
print(sublists([]))      # [[]]
print(sublists([1]))     # [[], [1]]
print(sublists([1,2]))   # [[], [1], [2], [1, 2]]
print(sublists([1,2,3])) # [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]
print(sublists([1,2,3,4])) # [[], [1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3], [2, 3, 4], [1, 2, 3, 4]]