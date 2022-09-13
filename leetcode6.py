class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result_group_order = list(range(numRows)) + list(range(numRows - 2, 0, -1))
        results = [[] for _ in range(numRows)]
        for i, c in enumerate(s):
            results[result_group_order[i % len(result_group_order)]].append(c)
        return ''.join([c for sublist in results for c in sublist])
