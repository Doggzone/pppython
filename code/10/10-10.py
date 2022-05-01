def factorial():
    n = int(input("Enter a number: "))
    assert n >= 1
    print("factorial(", n, ") = ", fac(n), sep='')