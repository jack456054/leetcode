def longestCommonPrefix(self, strs):
    length = len(strs)
    if strs:
        index = len(min(strs, key=len))
    else:
        return ""
    result = ""
    for strIndex in range(index):
        char = strs[0][strIndex]
        for i in strs:
            if i[strIndex] != char:
                return result
        result += char
    return result


if __name__ == '__main__':
    print(longestCommonPrefix('self', ["flower", "flow", "flight"]))
