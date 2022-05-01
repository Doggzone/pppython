def add_binary(n1,n2):
    over = 0
    answer = ''
    for d in range(-1,-len(n1)-1,-1):
        total = int(n1[d]) + int(n2[d]) + over
        if total == 1:
            over = None # Write your expression here.
            answer = None # Write your expression here.
        elif total == 2:
            over = None # Write your expression here.
            answer = None # Write your expression here.
        elif total == 3:
            over = None # Write your expression here.
            answer = None # Write your expression here.
        else: # total = 0
            over = None # Write your expression here.
            answer = None # Write your expression here.
    if over == 1:
        answer = None # Write your expression here.
    return answer

# Test code
print(add_binary('',''))                 # ''
print(add_binary('0','0'))               # '0'
print(add_binary('1','0'))               # '1'
print(add_binary('0','1'))               # '1'
print(add_binary('1','1'))               # '10'
print(add_binary('10','11'))             # '101'
print(add_binary('11','11'))             # '110'
print(add_binary('1011','1101'))         # '11000'
print(add_binary('1111','1111'))         # '11110'
print(add_binary('11011001','00011011')) # '11110100'
