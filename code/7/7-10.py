def minsteps(n):
    if n > 1:
        steps = minsteps(n-1) 
        if n % 2 == 0:
            steps = min(steps, minsteps(n//2)) 
        if n % 3 == 0:
            steps = min(steps, minsteps(n//3)) 
        return 1 + steps
    else:
        return 0