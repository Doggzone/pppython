from time import sleep
def countdown(n):
    while n > 0:
        print(n)
        sleep(1)
        n = n - 1
    print("Launch!")