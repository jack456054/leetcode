def plusOne(self, digits):
    # (Method 1)
    digits[-1] += 1
    for index in range(len(digits) - 1, -1, -1):
        if digits[index] >= 10:
            if index == 0:
                digits[index] = 0
                digits.insert(0, 1)
            else:
                digits[index] = 0
                digits[index - 1] += 1
        else:
            return digits
    return digits

    # (Method 2)
    # number = int(''.join(str(x) for x in digits)) + 1
    # result = [int(x) for x in str(number)]
    # return result


if __name__ == '__main__':
    print(plusOne('self', [1, 2, 3]))
    print(plusOne('self', [4, 3, 2, 1]))
    print(plusOne('self', [9, 9, 9]))
