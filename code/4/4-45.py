def date_after_n_days(year, month, day, n):
    pass # Write your code here.

# Test code    
print(date_after_n_days(2019,4,20,2))    # (2019, 4, 22)
print(date_after_n_days(2019,4,20,7))    # (2019, 4, 27)
print(date_after_n_days(2019,4,20,10))   # (2019, 4, 30)
print(date_after_n_days(2019,4,20,11))   # (2019, 5, 1)
print(date_after_n_days(2019,4,20,50))   # (2019, 6, 9)
print(date_after_n_days(2019,4,20,100))  # (2019, 7, 29)
print(date_after_n_days(2019,4,20,200))  # (2019, 11, 6)
print(date_after_n_days(2019,4,20,300))  # (2020, 2, 14)
print(date_after_n_days(2019,4,20,1000)) # (2022, 1, 14)