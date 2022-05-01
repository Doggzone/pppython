def next_month(year, month):
    # assume year >= 0 and 1 <= month <= 12
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return (year, month)