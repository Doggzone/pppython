def ispalindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return ispalindrome(s[1:-1])