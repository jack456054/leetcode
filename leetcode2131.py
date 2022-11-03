class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counts = Counter(words)
        lens = 0
        max_dup = 0
        word_set = set(words)
        for s in word_set:
            if s[0] != s[1]:
                if s[::-1] in counts:
                    lens += min(counts[s], counts[s[::-1]]) * 4
                    del counts[s]
                    del counts[s[::-1]]
            else:
                lens += (counts[s] // 2) * 4
                max_dup = max(counts[s] % 2, max_dup)
        return lens + max_dup * 2
