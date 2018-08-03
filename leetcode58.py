def lengthOfLastWord(self, s):
    resultList = s.split()
    if not resultList:
        return 0
    return len(resultList[-1])


if __name__ == '__main__':
    print(lengthOfLastWord('self', "Hello World"))
    print(lengthOfLastWord('self', ""))
    print(lengthOfLastWord('self', " "))
