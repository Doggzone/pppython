def sigma(n):
    def loop(n,total):
        if n > 0:
            return loop(n-1,n+total)
        else:
            return total
    return loop(n,0)

print(sigma(512))
print(sigma(1024))
