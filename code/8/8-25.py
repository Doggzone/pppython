def appears_once(ns):
    count = 0
    for n in ns:
        if n == 1:
            count += 1
    return count == 1