from random import sample, randrange
from time import perf_counter

print("Preparing data. Please, wait a moment ...")
data = sample(range(10000000),8000000)

print("Testing seq_search function begins ...")
for _ in range(10):
    x = randrange(10000000)
    start = perf_counter()
    index = seq_search(data, x)
    finish = perf_counter()
    print(x, "is found at", index, "in", finish - start, "seconds")

print("Preparing data for bin_search. Please, wait a moment ...")
data.sort()

print("Testing bin_search function begins ...")
for _ in range(10):
    x = randrange(10000000)
    start = perf_counter()
    index = bin_search(data, x)
    finish = perf_counter()
    print(x, "is found at", index, "in", finish - start, "seconds")
