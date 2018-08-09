def merge(self, nums1, m, nums2, n):
    for index in range(m, m + n):
        nums1[index] = nums2[index - m]
    nums1.sort()
    # return nums1


if __name__ == '__main__':
    print(merge("self", [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
    # print(merge("self", 1))
    # print(merge("self", 5))
