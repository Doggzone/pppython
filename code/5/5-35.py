def is_leap_year(year):
    return year % 400 == 0 or \
           year % 4 == 0 and year % 100 != 0

def print_leap_year(yearfrom, yearto):
    print("List of leap years between", yearfrom, "and", yearto, ":")
    pass # Write your for-loop here. 

print_leap_year(1990,2004) # 1992 1996 2000 2004
print_leap_year(2005,2014) # 2008 2012
print_leap_year(2094,2106) # 2096 2104