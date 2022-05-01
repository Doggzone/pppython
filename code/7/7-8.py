def comb_pascal(n,r):
    row0 = [1 for _ in range(r+1)]
    matrix = [row0] + [[1] for _ in range(n-r)]
    for i in range(1, n-r+1):
        for j in range(1, r+1):
            newvalue = matrix[i][j-1] + matrix[i-1][j]
            matrix[i].append(newvalue)
    return matrix[n-r][r]