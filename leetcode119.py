class Solution:
    def getRow(self, rowIndex):
        result = []
        for row in range(rowIndex + 1):
            if row == 0:
                result = [1]
            else:
                pascalNow = []
                for index, value in enumerate(result):
                    pascalNow.append(1) if index == 0 else pascalNow.append(result[index - 1] + result[index])
                pascalNow.append(1)
                result = pascalNow
        return result


if __name__ == '__main__':
    print(Solution.getRow("self", 3))
    print(Solution.getRow("self", 4))
