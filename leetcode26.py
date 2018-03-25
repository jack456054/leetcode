def removeDuplicates(self, nums):
    nums[:] = list(set(nums))
    nums.sort()
    return len(nums)


if __name__ == '__main__':
    print(removeDuplicates('self', [1, 1, 2]))
