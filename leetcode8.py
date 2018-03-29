def myAtoi(self, str):
    result = 0
    for i in str:
        if i != ' ':
            try:
                print(result)
                result += int(i)
                result *= 10
            except ValueError:
                print('v', result)
                return result // 10
        elif result:
            return result // 10
    return result // 10


if __name__ == '__main__':
    print(myAtoi('self', "  23a45"))
