def isinteger(s):
    return s.isdigit() or \
           s != '' and s[0] == '-' and s[1:].isdigit()

def isfloat(s):
    (left, dot, right) = s.partition(".")
    return None # Replace None with Boolean expression.

# Test code
print(isfloat(".112"))   # True
print(isfloat("-.112"))  # True
print(isfloat("3.14"))   # True
print(isfloat("-3.14"))  # True
print(isfloat("5."))     # True
print(isfloat("5.0"))    # True
print(isfloat("-777.0")) # True
print(isfloat("-777."))  # True
print(isfloat("."))      # False
print(isfloat(".."))     # False