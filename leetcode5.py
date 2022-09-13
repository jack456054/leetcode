class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = ''
        s: str = '*' + '*'.join(list(s)) + '*'
        for i, c in enumerate(s):
            moves = 0
            current_str = ''
            while True:
                if len(max_str) >= (len(s) - i) * 2 - 1:
                    return ''.join(max_str.split('*'))
                try:
                    if s[i - moves] == s[i + moves]:
                        current_str = s[i - moves : i + moves + 1]
                        if len(current_str) > len(max_str):
                            max_str = current_str
                        moves += 1
                    else:
                        break
                except KeyError:
                    break
        return ''.join(max_str.split('*'))
