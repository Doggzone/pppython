def validclock24(time):
    (hour, colon, minute) = time.partition(":")
    return None # Replace None with Boolean expression.

# Test code
print(validclock24("00:00"))  # True
print(validclock24("00:30"))  # True
print(validclock24("09:58"))  # True
print(validclock24("12:15"))  # True
print(validclock24("23:59"))  # True
print(validclock24("24:00"))  # True
print(validclock24("7:07"))   # False
print(validclock24("07:121")) # False
print(validclock24("13:4"))   # False
print(validclock24("00:60"))  # False
print(validclock24("24:01"))  # False
print(validclock24("25:10"))  # False