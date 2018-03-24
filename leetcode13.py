def romanToInt(self, s):
    result = 0
    cur_num = 1
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(s) - 1, -1, -1):
        if cur_num > dic[s[i]]:
            result -= dic[s[i]]
        else:
            result += dic[s[i]]
            cur_num = dic[s[i]]
    return result


if __name__ == '__main__':
    print(romanToInt('self', "DCXXI"))
