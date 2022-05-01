def mult(m,n):
    if n > 0:
        return m + mult(m,n-1)
    else:
        return 0