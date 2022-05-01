def selection_sort(xs):
    ss = []
    while xs != []:
        smallest = min(xs)
        xs.remove(smallest)
        ss.append(smallest)
    return ss