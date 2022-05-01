def merge_sort(xs):
    if len(xs) > 1:
        mid = len(xs) // 2
        return merge(merge_sort(xs[:mid]),merge_sort(xs[mid:]))
    else:
        return xs