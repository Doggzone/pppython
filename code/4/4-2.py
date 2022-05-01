def sigma(n):
    return loop(n, 0)

def loop(n, total):
    if n > 0:
        return loop(n-1, n+total)
    else:
        return total
