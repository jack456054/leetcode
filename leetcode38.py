def countAndSay(self, n):
    seq = "1"
    for i in range(n - 1):
        result = previous = ""
        count = 0
        for j in seq:
            if j == previous:
                count += 1
            else:
                if previous:
                    result += str(count) + previous
                previous = j
                count = 1
        result += str(count) + previous
        seq = result
    return seq


if __name__ == '__main__':
    print(countAndSay('self', 1))
    print(countAndSay('self', 4))
