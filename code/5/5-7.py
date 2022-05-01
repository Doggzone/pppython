def fac(n):
    ans = 1
    while n > 0:
        n, ans = n-1, ans*n
    return ans