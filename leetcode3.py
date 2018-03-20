def lengthOfLongestSubstring(self, s):
    maxnum = 0
    subnum = 0
    subset = []
    for i in s:
        for index, j in enumerate(subset):
            if j == i:
                subset = subset[index + 1:]
                subnum = len(subset)

        subset.append(i)
        subnum += 1
        maxnum = max(maxnum, subnum)
    return maxnum


if __name__ == '__main__':
    print(lengthOfLongestSubstring('self', "abcabcbb"))
