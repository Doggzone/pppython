def dec2bin(dec):
    bin = ''
    while not (dec == 0 or dec == 1):
        pass # Write your code here.
    bin = str(dec) + bin
    return bin

# Test code
print(bin2dec(0))  # "0"
print(bin2dec(1))  # "1"
print(bin2dec(6))  # "110"
print(bin2dec(19)) # "10011"
print(bin2dec(42)) # "101010"