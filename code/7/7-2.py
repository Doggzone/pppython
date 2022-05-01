def run_fib(n):
    from time import perf_counter
    start = perf_counter()
    answer = fib(n)
    finish = perf_counter()
    print("fib(", n, ") => ", answer, sep="")
    print(round(finish-start,4), "seconds")