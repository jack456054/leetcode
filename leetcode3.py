def lengthOfLongestSubstring(self, s):
    j = 0
    maxnum = 0
    subset = {}
    for index, i in enumerate(s):
        if i in subset and subset[i] + 1 > j:
            j = subset[i] + 1
        subset[i] = index
        maxnum = max(maxnum, index - j + 1)
    return maxnum


if __name__ == '__main__':
    print(lengthOfLongestSubstring('self', "abcabcbb"))
    print(lengthOfLongestSubstring('self', "abba"))
