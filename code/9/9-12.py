def sparse_add(ms,ns):
	pass # Write your code here.

# Test code
print(sparse_add({},{})) # {}
print(sparse_add({2: 3, 9: 7},{})) # {2: 3, 9: 7}
print(sparse_add({},{0: 1, 2: 2, 6: 9})) # {0: 1, 2: 2, 6: 9}
print(sparse_add({2: 3, 9: 7},{0: 1, 2: 2, 6: 9})) # {2: 5, 9: 7, 0: 1, 6: 9}