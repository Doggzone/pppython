def selection_sort(xs): // Erroneous version
    if xs != []:
        smallest = min(xs)
        xs = xs.remove(smallest)
        return [smallest] + selection_sort(xs)
    else:
        return []