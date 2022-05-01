while True:
    try:
        x = int(input("Enter a number: "))
        reciprocal = 1 / x
        print("The reciprocal of", x, "is", reciprocal)
        break
    except ValueError as message:
        print(message)
    except ZeroDivisionError as message:
        print(message)
        break