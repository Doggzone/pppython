def clock24to12(time):
    (hour, colon, minute) = time.partition(":")
    pass # Write your code here.

# Test code
print(clock24to12("00:00")) # "12:00am"
print(clock24to12("00:05")) # "12:05am"
print(clock24to12("09:58")) # "9:58am"
print(clock24to12("11:43")) # "11:43am"
print(clock24to12("12:08")) # "12:08pm"
print(clock24to12("15:50")) # "3:50pm"
print(clock24to12("20:20")) # "8:20pm"
print(clock24to12("24:00")) # "12:00am"