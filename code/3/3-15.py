def isinteger(s):
    return s.isdigit() or \
           s != '' and s[0] == '-' and s[1:].isdigit()

# Test code
print(isinteger("55"))    # True
print(isinteger("5o5"))   # False
print(isinteger("-55"))   # True
print(isinteger("--55"))  # False
print(isinteger("---55")) # False
print(isinteger("5-5"))   # False
print(isinteger("55-"))   # False
print(isinteger("+55"))   # False
print(isinteger("five"))  # False
print(isinteger("-"))     # False
print(isinteger(""))      # False