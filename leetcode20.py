def isValid(self, s):
    result = []
    for par in s:
        if par == '{' or par == '[' or par == '(':
            result.append(par)
        elif par == '}':
            if result and result[-1] == '{':
                result.pop()
            else:
                return False
        elif par == ']':
            if result and result[-1] == '[':
                result.pop()
            else:
                return False
        elif par == ')':
            if result and result[-1] == '(':
                result.pop()
            else:
                return False
    return not result


if __name__ == '__main__':
    print(isValid('self', "()[]{}"))
    print(isValid('self', "{[]}"))
    print(isValid('self', "]"))
