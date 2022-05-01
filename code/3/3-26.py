def clock12to24(time):
    (hour, colon, minuteplus) = time.partition(":")
    minute = minuteplus[:-2]
    am_or_pm = minuteplus[-2:]
    pass # Write your code here.
    return hour + colon + minute

# Test code
print(clock12to24("12:00am")) # "00:00"
print(clock12to24("12:05am")) # "00:05"
print(clock12to24("1:30am"))  # "01:30"
print(clock12to24("3:05am"))  # "03:05"
print(clock12to24("12:00pm")) # "12:00"
print(clock12to24("12:08pm")) # "12:08"
print(clock12to24("3:50pm"))  # "15:50"
print(clock12to24("9:12pm"))  # "21:12"
print(clock12to24("11:59pm")) # "23:59"