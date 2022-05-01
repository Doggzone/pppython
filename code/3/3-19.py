def isRRN(s):
    (front, mid, back) = s.partition("-")
    return frontOK(front+back[0]) and mid == "-" and backOK(s)