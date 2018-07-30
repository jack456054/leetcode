def removeElement(self, nums, val):

    # (This is not O(1) space complexity)
    # nums = list(filter(lambda a: a != val, nums))

    # (This one is slower)
    # for i in range(nums.count(val)):
    #         nums.remove(val)
    # return len(nums)

    while True:
        try:
            nums.remove(val)
        except ValueError:
            return len(nums)


if __name__ == '__main__':
    print(removeElement('self', [3, 2, 2, 3], 3))
    print(removeElement('self', [0, 1, 2, 2, 3, 0, 4, 2], 2))
    print(removeElement('self', [2], 3))
    print(removeElement('self', [], 0))
