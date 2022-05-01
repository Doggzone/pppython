def minutes_after(time, minuteplus):
    (hour,":",minute) = time.partition(":")
    hourplus = minuteplus // 60
    minuteplus = minuteplus % 60
    pass # Write your code here.
    return str(hour) + ":" + str(minute)

# Test code
print(minutes_after("3:34",100))   # "5:14"
print(minutes_after("11:45",20))   # "12:5"
print(minutes_after("9:59",1))     # "10:0"
print(minutes_after("123:10",200)) # "126:30"