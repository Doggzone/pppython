def isleapyear(year):
    # assume year >= 0
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0