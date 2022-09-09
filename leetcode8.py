INT_MAX = 2**31 - 1
INT_MIN = -(2**31)


class Solution:
    def myAtoi(self, str: str) -> int:
        result, neg, pos = 0, 0, 0
        first_word = str.split()
        if not first_word:
            return result
        first_word = first_word[0]
        if (
            first_word[0] != '-'
            and first_word[0] != '+'
            and not first_word[0].isdigit()
        ):
            return result
        if first_word[0] == '-':
            neg = 1

        # Start from index 0 if non-negative else 1
        for index in range(neg, len(first_word)):
            if first_word[0] == '+' and not pos:
                pos = 1
            elif not first_word[index].isdigit():
                return Solution.num_bound(self, result, neg)
            else:
                result *= 10
                result += int(first_word[index])
        return Solution.num_bound(self, result, neg)

    def num_bound(self, result, neg):
        if not neg:
            return result if result <= INT_MAX else INT_MAX
        else:
            return -result if -result >= INT_MIN else INT_MIN


if __name__ == '__main__':
    print(Solution.myAtoi("self", "  23a45    555664"))
    print(Solution.myAtoi("self", "  -42"))
    print(Solution.myAtoi("self", "  --2"))
    print(Solution.myAtoi("self", "-91283472332"))
    print(Solution.myAtoi("self", "3.14159"))
    print(Solution.myAtoi("self", "-0012a42"))
    print(Solution.myAtoi("self", "-abc123"))
    print(Solution.myAtoi("self", ""))
    print(Solution.myAtoi("self", "+1"))
