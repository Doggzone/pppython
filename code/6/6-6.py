def seq_search(s,x):
    def loop(i):
        if i < len(s):
            if s[i] == x:
                return i
            else:
                return loop(i+1)
        else:
            return None
    return loop(0)