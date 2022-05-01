def seq_search(s,x):
    for i in range(len(s)):
        if s[i] == x:
            return i
    return None