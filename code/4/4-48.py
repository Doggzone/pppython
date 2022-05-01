def days_in_month(year, month):
    # assume year >= 0 and 1 <= month <= 12
    if month == 1 or month == 3 or month == 5 or month == 7 or \
       month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if isleapyear(year):
            return 29
        else:
            return 28