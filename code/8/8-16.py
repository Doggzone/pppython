def get_integer(message, i, j):
    number = input(message)
    while not (number.isdigit() and i <= int(number) <= j):
        number = input(message)
    return int(number)