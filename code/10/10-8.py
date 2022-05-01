def fac(n):
    ans = 1
    while n > 1:
        ans = n * ans
        n = n - 1
    return ans