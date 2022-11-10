class Solution:
    def removeDuplicates(self, s: str) -> str:
        results: List[str] = []
        for c in s:
            if results and results[-1] == c:
                results.pop()
            else:
                results.append(c)
        return ''.join(results)