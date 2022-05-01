def sumrange(m,n):
    if m <= n:
        return m + sumrange(m+1,n)
    else:
        return 0

# Test code
print(sumrange(3,2))   # 0
print(sumrange(3,3))   # 3
print(sumrange(3,4))   # 7
print(sumrange(3,6))   # 18
print(sumrange(1,10))  # 55
print(sumrange(-5,10)) # 40
print(sumrange(-5,-2)) # -14