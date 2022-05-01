def partition(pivot,xs):
    if xs != []:
        left, right = partition(pivot,xs[1:])
        if xs[0] <= pivot:
            left.append(xs[0])
        else:
            right.append(xs[0])
        return left, right
    else:
        return [], []