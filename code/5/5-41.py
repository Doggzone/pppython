def take_before(s,index):
	pass # To be filled in later.

# Test code
s = [1,2,3,4,5]
print(take_before(s,0))  # []
print(take_before(s,1))  # [1]
print(take_before(s,2))  # [1, 2]
print(take_before(s,3))  # [1, 2, 3]
print(take_before(s,4))  # [1, 2, 3, 4]
print(take_before(s,5))  # [1, 2, 3, 4, 5]
print(take_before(s,6))  # [1, 2, 3, 4, 5]
print(take_before([],4)) # []
print(take_before(s,-3)) # []