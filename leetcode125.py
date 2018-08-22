import re


class Solution:
    def isPalindrome(self, s):
        result = re.findall(r'\w', s.lower())
        return result == list(reversed(result))  # Or result[::-1]


if __name__ == '__main__':
    print(Solution.isPalindrome("self", "A man, a plan, a canal: Panama"))
