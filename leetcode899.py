class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k >= 2:
            return ''.join(sorted(s))
        else:
            min_s = s
            for i, _ in enumerate(s):
                min_s = min(min_s, s[i:] + s[:i])
            return min_s
                 
            