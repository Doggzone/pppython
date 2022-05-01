def sigma(n):
    if n > 0:
        return sigma(n-1) + n
    else:
        return 0

print(sigma(512))
print(sigma(1024))
