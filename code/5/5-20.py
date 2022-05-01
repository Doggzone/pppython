def insertion_sort(xs):
    if xs != []:
        return insert(xs[0],insertion_sort(xs[1:]))
    else:
        return []