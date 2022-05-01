def comb_pascal(n,r):
    vector = [1 for _ in range(r+1)]
    for _ in range(1, n-r+1):
        for j in range(1, r+1):
            vector[j] = vector[j-1] + vector[j]
    return vector[r]