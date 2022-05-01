def seq_search(s,x):
    i = 0
    while i < len(s):
        if s[i] == x:
            return i
        else:
            i = i + 1
    return None