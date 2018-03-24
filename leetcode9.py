def isPalindrome(self, x):
    if x < 0:
        return False
    s = str(x)
    j = len(s) - 1
    i = 0
    while j >= i:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True
