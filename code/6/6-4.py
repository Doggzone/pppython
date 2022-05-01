def seq_search_OX(s,x):
    return s != [] and (s[0] == x or seq_search_OX(s[1:],x))