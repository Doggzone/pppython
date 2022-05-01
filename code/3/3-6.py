x = int(input("Enter your number: "))
if x % 2 == 0 and x % 3 == 0:
    print(x, "is divisible by 2 and 3")
elif x % 2 == 0 and not(x % 3 == 0):
    print(x, "is divisible by 2 but not by 3")
elif not(x % 2 == 0) and x % 3 == 0:
    print(x, "is divisible by 3 but not by 2")
else:
    print(x, "is not divisible by 2 or 3")