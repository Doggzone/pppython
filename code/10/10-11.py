def factorial():
    while True:
        try:
            n = int(input("Enter a number: "))
            assert n >= 1
        except ValueError:
            print("Not a number.")
        except AssertionError:
            print("Not a natural number.")
        else:
            print("factorial(", n, ") = ", fac(n), sep='')
            print("Goodbye!")
            break