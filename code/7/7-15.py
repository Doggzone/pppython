def tower_of_hanoi(n, source, destin, temp):
    global count
    if n > 1:
        tower_of_hanoi(n-1, source, temp, destin)
        count += 1
        tower_of_hanoi(n-1, temp, destin, source)
    else:
        count += 1

for n in [4,6,8,16,24,25,26,27,28]:
    count = 0
    from time import perf_counter
    start = perf_counter()
    tower_of_hanoi(n, "A", "C", "B")
    finish = perf_counter()
    cpu_time = round(finish-start,1)
    print(n, "disks:", count, "moves in", cpu_time, "seconds")