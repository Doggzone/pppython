def ascending_sublists(ns):
	pass # write your code here.

# Test code
print(ascending_sublists([]))      # []
print(ascending_sublists([1]))     # []
print(ascending_sublists([1,2]))   # [[1, 2]]
print(ascending_sublists([1,2,3])) # [[1, 2], [2, 3], [1, 2, 3]]
print(ascending_sublists([3,1,2])) # [[1, 2]]
print(ascending_sublists([1,3,2])) # [[1, 3]]
print(ascending_sublists([1,5,3,4,8,2,3,5])) # [[1, 5], [3, 4], [4, 8], [2, 3], [3, 5], [3, 4, 8], [2, 3, 5]]