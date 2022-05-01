def selection_sort(xs):
    def loop(xs,ss):
        if xs != []:
            smallest = min(xs)
            xs.remove(smallest)
            return loop(xs,ss+[smallest])
        else:
            return ss
    return loop(xs,[])