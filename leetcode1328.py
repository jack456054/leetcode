class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        if len(palindrome) % 2 == 0:
            for index, c in enumerate(palindrome):
                if c != 'a':
                    return palindrome.replace(c, 'a', 1)
        else:
            for index, c in enumerate(palindrome):
                if c != 'a' and index != len(palindrome) // 2:
                    return palindrome.replace(c, 'a', 1)
        return palindrome[:-1] + 'b'
