def count_the(x, xss):
	pass # Write your code here.

# Test code
print(count_the(1,[])) # 0
print(count_the(7,[1,7,7])) # 2
print(count_the(7,[1,[7],7])) # 2
print(count_the(7,[7,[2,7,[4,7]]])) # 3
print(count_the(7,[[[[[[[],[[7,2,7]],7]]]]]])) # 3
print(count_the(7,[[[[7]],[7]],5,7,[3]])) # 3
print(count_the(5,[1,[5,2],[[3],[5,4]],[[[5,5,5,5]]],6,[5,[[5],[[9]]]]])) # 8