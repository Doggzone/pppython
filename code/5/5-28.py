def quicksort(xs):
    if len(xs) > 1:
        pivot = xs[0]
        (left, right) = partition(pivot,xs[1:])
        return quicksort(left) + [pivot] + quicksort(right)
    else:
        return xs