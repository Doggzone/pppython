from time import sleep
def countdown(n):
    if n > 0:              
        print(n)
        sleep(1)
        countdown(n-1)
    else:                   
        print("Launch!")