def merge(left,right):
    if not (left == [] or right == []):
        if left[0] <= right[0]:
            return [left[0]] + merge(left[1:],right)
        else:
            return [right[0]] + merge(left,right[1:])
    else:
        return left + right