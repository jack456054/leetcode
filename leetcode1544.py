class Solution:
    def makeGood(self, s: str) -> str:
        results = []
        for c in s:
            if results and abs(ord(results[-1]) - ord(c)) == 32:
                results.pop()
            else:
                results.append(c)
        return ''.join(results)
                