def selection_sort(xs):
    def loop(xs,ss):
        if xs != []:
            smallest = min(xs)
            xs.remove(smallest)
            ss.append(smallest)
            return loop(xs,ss)
        else:
            return ss
    return loop(xs,[])