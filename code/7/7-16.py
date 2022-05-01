def minbags(n):
    if n > 1:
        if n == 2 or n == 3 or n == 5:
            return 1
        else:
            smallest = minbags(n-2)
            if n > 4:
                smallest = min(smallest, minbags(n-3))
            if n > 6:
                smallest = min(smallest, minbags(n-5))
        return 1 + smallest
    else:
        return 0