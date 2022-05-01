def bin_search_closest(ss,x):
	pass # write your code here.

# Test code
print(bin_search_closest([],3))           # None
print(bin_search_closest([8],5))          # 0
print(bin_search_closest([8],8))          # 0
print(bin_search_closest([8],9))          # 0
print(bin_search_closest([1,2,5,9,10],0)) # 0
print(bin_search_closest([1,2,5,9,10],1)) # 0
print(bin_search_closest([1,2,5,9,10],2)) # 1
print(bin_search_closest([1,2,5,9,10],3)) # 1
print(bin_search_closest([1,2,5,9,10],4)) # 2
print(bin_search_closest([1,2,5,9,10],5)) # 2
print(bin_search_closest([1,2,5,9,10],6)) # 2
print(bin_search_closest([1,2,5,9,10],7)) # 2
print(bin_search_closest([1,2,5,9,10],8)) # 3
print(bin_search_closest([1,2,5,9,10],9)) # 3
print(bin_search_closest([1,2,5,9,10],10)) # 4
print(bin_search_closest([1,2,5,9,10],11)) # 4