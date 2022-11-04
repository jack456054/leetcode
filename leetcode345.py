class Solution:
    def reverseVowels(self, s: str) -> str:
        p0: int = 0
        p1: int = len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        while p1 > p0:
            while s[p0] not in vowels:
                p0 += 1
                if p0 >= p1:
                    break
            while s[p1] not in vowels:
                p1 -= 1
                if p0 >= p1:
                    break
            if p0 <= p1:
                s[p0], s[p1] = s[p1], s[p0]
            p0 += 1
            p1 -= 1
        return ''.join(s)
