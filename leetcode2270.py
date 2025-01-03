class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        left = 0
        right = sum(nums)
        for i in nums[:-1]:
            left += i
            right -= i
            if left >= right:
                count += 1
        return count
