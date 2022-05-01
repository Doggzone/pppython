import random
def testsearch_widest_gap():
    db = random.sample(range(500),100)
    print("Searching the widest gap...")
    db.sort()
    print(db)
    index, gap = search_widest_gap(db)
    print("The widest gap is:", gap)
    print("between", db[index], "and", db[index+1])
    print("at", index)