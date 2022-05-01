while True:
    try:
        x = int(input("Enter a number: "))
        reciprocal = 1 / x
    except ValueError:
        print("Not a number.")
    except ZeroDivisionError:
        print("The reciprocal of 0 does not exist.")
        break
    else:
        print("The reciprocal of", x, "is", reciprocal)
        break