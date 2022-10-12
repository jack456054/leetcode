class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for index, num in enumerate(nums[:-2]):
            if num < nums[index + 1] + nums[index + 2]:
                return num + nums[index + 1] + nums[index + 2]
        return 0
