def transpose(mat):
    no_of_columns = len(mat[0])
    transposed = []  
    for _ in range(no_of_columns):
        transposed.append([])
    for row in mat:
        i = 0
        for entry in row:
            transposed[i].append(entry)
            i += 1
    return transposed