def seq_search_OX(s,x):
    if s != []:
        if s[0] == x:
            return True
        else:
            return seq_search_OX(s[1:],x)
    else:
        return False