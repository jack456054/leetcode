def maxSubArray(self, nums):
    result = maxSum = 0
    maxNum = max(nums)
    if maxNum < 0:
        return maxNum
    for i in nums:
        if i >= 0:
            maxSum += i
            result = max(maxSum, result)
        if i < 0:
            if maxSum + i < 0:
                result = max(maxSum, result)
                maxSum = 0
            else:
                maxSum += i
    return result


if __name__ == '__main__':
    print(maxSubArray('self', [-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(maxSubArray('self', [-1]))
    print(maxSubArray('self', [1, -1, -2]))
