def run_minbags(n):
    from time import perf_counter
    start = perf_counter()
    answer = minbags(n)
    finish = perf_counter()
    print("minbags(", n, ") => ", answer, sep="")
    print(round(finish-start,1), "seconds")