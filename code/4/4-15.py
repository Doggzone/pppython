def power(b,n):
    def loop(n,prod):
        if n > 0:
            return loop(n-1,b*prod)
        else:
            return prod
    return loop(n,1)