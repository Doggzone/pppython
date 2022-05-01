def gcd(m,n):
    if n != 0:
        return gcd(n,m%n)
    else:
        return m

# Test code
print(gcd(48,18))  # 6
print(gcd(18,48))  # 6
print(gcd(192,72)) # 24
print(gcd(18,57))  # 3
print(gcd(0,11))   # 11