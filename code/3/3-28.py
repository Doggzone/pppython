def time_passed(fromtime, totime):
    (hour1,_,minute1) = fromtime.partition(":")
    (hour2,_,minute2) = totime.partition(":")
    hour = int(hour2) - int(hour1)
    if minute1 > minute2:
        pass # Write your code here.
    else:
        pass # Write your code here.
    return str(hour) + ":" + str(minute)

# Test code
print(time_passed("03:12","03:25")) # "0:13"
print(time_passed("11:45","13:15")) # "1:30"
print(time_passed("06:15","07:45")) # "1:30"
print(time_passed("03:34","05:00")) # "1:26"