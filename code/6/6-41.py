import random
def test_bin_search_closest():
    data = random.sample(range(500),100)
    print("Binary search closest function test")
    data.sort()
    print(data)
    for _ in range(10):
        x = random.randrange(500)
        index = bin_search_closest(data, x)
        print("The closest to", x, ":", data[index], "at index", index)