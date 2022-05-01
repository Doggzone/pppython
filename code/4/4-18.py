def power(b,n):
    def loop(b,n,prod):
        if n > 0:
            if n % 2 == 0:
                return loop(b*b,n//2,prod)  
            else:
                return loop(b,n-1,b*prod)
        else:
            return prod
    return loop(b,n,1)