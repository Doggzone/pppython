def minsteps(n):
    memo = [0 for _ in range(n+1)] 
    def loop(n):
        if n > 1:
            if memo[n] == 0:
                steps = loop(n - 1) 
                if n % 2 == 0:
                    steps = min(steps, loop(n // 2)) 
                if n % 3 == 0:
                    steps = min(steps, loop(n // 3))
                memo[n] = steps + 1
            return memo[n]
        else:
            return 0
    return loop(n)