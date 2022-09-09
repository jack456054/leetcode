def generate(self, numRows):
    result = []
    if numRows == 0:
        return result
    result.append([1])
    for i in range(0, numRows - 1):
        pascalNow = []
        for (index, _) in enumerate(result[-1]):
            pascalNow.append(1) if index == 0 else pascalNow.append(
                result[-1][index - 1] + result[-1][index]
            )
        pascalNow.append(1)
        result.append(pascalNow)
    return result


if __name__ == '__main__':
    print(generate("self", 0))
    print(generate("self", 1))
    print(generate("self", 5))
