import time
print("Now, go!")
start = time.perf_counter()
print("Start at", start)
time.sleep(5)
finish = time.perf_counter()
print("Finish at", finish)
print("Total =", finish - start, "seconds")