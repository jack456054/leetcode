import re
INT_MAX = 2 ** 31 - 1
INT_MIN = -(2 ** 31)


class Solution:
    def myAtoi(self, str: str) -> int:
        first_word = str.split()
        if not first_word:
            return 0
        if first_word[0].isdigit() or first_word[0].lstrip('-').isdigit():
            try:
                result = int(first_word[0])
                if result > INT_MAX:
                    return INT_MAX
                elif result < INT_MIN:
                    return INT_MIN
                else:
                    return result
            except ValueError:
                return 0

        else:
            try:
                result = float(first_word[0])
                if result > INT_MAX:
                    return INT_MAX
                elif result < INT_MIN:
                    return INT_MIN
                else:
                    return int(result)
            except ValueError:
                return 0


if __name__ == '__main__':
    print(Solution.myAtoi("self", "  23a45    555664"))
    print(Solution.myAtoi("self", "  -42"))
    print(Solution.myAtoi("self", "  --2"))
    print(Solution.myAtoi("self", "-91283472332"))
    print(Solution.myAtoi("self", "3.14159"))
    print(Solution.myAtoi("self", "-0012a42"))
