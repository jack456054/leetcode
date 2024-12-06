class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        sum = 0
        count = 0
        banned = set(banned)
        for i in range(1, n + 1):
            if i not in banned:
                sum += i
                if sum > maxSum:
                    return count
                count += 1
        return count
