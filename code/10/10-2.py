try:
    x = int(input("Enter a number: "))
    reciprocal = 1 / x
    print("The reciprocal of", x, "is", reciprocal)
except ValueError:
    print("Not a number.")
except ZeroDivisionError:
    print("The reciprocal of 0 does not exist.")