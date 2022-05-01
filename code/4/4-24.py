def gcd(m,n):
    def loop(m,n,k):
        if not (m == 0 or n == 0):
            if even(m) and even(n):
                return loop(m//2,n//2,_____)
            elif even(m) and odd(n):
                return loop(m//2,n,k)
            elif odd(m) and even(n):
                return loop(m,n//2,k)
            elif m <= n:
                return loop(m,(n-m)//2,k)
            else:
                return loop(n,(m-n)//2,k)
        else:
            if m == 0:
                return _______
            else: # n == 0
                return _______
    return loop(m,n,1)