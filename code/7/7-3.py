def fib(n):
    if n > 1:
        i = 2
        a, b = 0, 1
        while i <= n:
            a, b = b, a + b
            i += 1
        return b
    else:
        return n