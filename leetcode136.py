class Solution:
    # (Method 1)
    # def singleNumber(self, nums):
    #     while nums:
    #         currentValue = nums.pop()
    #         try:
    #             nums.remove(currentValue)
    #         except ValueError:
    #             return currentValue

    # (Method 2)
    def singleNumber(self, nums):
        nums.sort()
        length = len(nums)
        for index in range(0, length, 2):
            if index == length - 1 or nums[index] != nums[index + 1]:
                return nums[index]


if __name__ == '__main__':
    print(Solution.singleNumber("self", [2, 2, 1]))
    print(Solution.singleNumber("self", [4, 1, 2, 1, 2]))
