def addBinary(self, a, b):
    # (My method)
    # binary = int(a) + int(b)
    # currentBit = 0
    # result = ""
    # if not binary:
    #     return "0"
    # while binary:
    #     currentBit = binary % 10
    #     if currentBit == 2:
    #         binary += 10
    #         result = "0" + result
    #     elif currentBit == 3:
    #         binary += 10
    #         result = "1" + result
    #     else:
    #         result = str(currentBit) + result
    #     binary //= 10
    # return result

    # (One line method)
    return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    print(addBinary('self', "11", "1"))
    print(addBinary('self', "1010", "1011"))
    print(addBinary('self', "0", "0"))
    print(addBinary('self', "1111", "1111"))
