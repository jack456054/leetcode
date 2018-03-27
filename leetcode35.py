def searchInsert(self, nums, target):
    n = len(nums)
    for index in range(n):
        if target <= nums[index]:
            return index
        if index == n - 1:
            return index + 1
        if nums[index] < target and nums[index + 1] > target:
            return index + 1
