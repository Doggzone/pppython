def seq_search_OX(s,x):
    while s != []:
        if s[0] == x:
            return True
        else:
            s = s[1:]
    return False