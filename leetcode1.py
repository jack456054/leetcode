def twoSum(self, nums, target):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


if __name__ == '__main__':
    print(twoSum('self', [3, 2, 4], 6))
