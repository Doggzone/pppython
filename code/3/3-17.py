def isleapyear(year):
    if year >= 0:
        return None # Replace None with Boolean expression.
    else:
        return None

# Test code
print(isleapyear(0))     # True
print(isleapyear(1))     # False
print(isleapyear(4))     # True
print(isleapyear(2010))  # False
print(isleapyear(2011))  # False
print(isleapyear(2012))  # True
print(isleapyear(2013))  # False
print(isleapyear(2016))  # True
print(isleapyear(1900))  # False
print(isleapyear(2000))  # True
print(isleapyear(2020))  # True
print(isleapyear(2100))  # False
print(isleapyear(2200))  # False
print(isleapyear(2400))  # True
print(isleapyear(-2000)) # None