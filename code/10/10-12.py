class NonPositive(Exception): pass

def factorial():
    while True:
        try:
            n = int(input("Enter a number: "))
            if n < 1:
                raise NonPositive
        except ValueError:
            print("Not a number.")
        except NonPositive:
            print("Not a natural number.")
        else:
            print("factorial(", n, ") = ", fac(n), sep='')
            print("Goodbye!")
            break