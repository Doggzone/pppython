def isanagram(word1,word2):
    while word1 != '':
        if word1[0] in word2:
            pass # write your code here.
        else:
            return False
    return word2 == ''

# Test code
print(isanagram('silent','listen'))     # True
print(isanagram('silent','listens'))    # False
print(isanagram('elvis','lives'))       # True
print(isanagram('restful','fluster'))   # True
print(isanagram('restfully','fluster')) # False