def seq_search(s,x):
    def loop(s,i):
        if s != []:
            if s[0] == x:
                return i
            else:
                return loop(s[1:],i+1)
        else:
            return None
    return loop(s,0)