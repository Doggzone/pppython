def selection_sort(xs):
    if xs != []:
        smallest = min(xs)
        xs.remove(smallest)
        return [smallest] + selection_sort(xs)
    else:
        return []