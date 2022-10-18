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


# class Solution:
#     def countAndSay(self, n: int) -> str:
#         pattern = '1'
#         while n > 1:
#             last_c = pattern[0]
#             count = 1
#             next_pattern = ''
#             for c in pattern[1:]:
#                 if c == last_c:
#                     count += 1
#                 else:
#                     next_pattern += f'{count}{last_c}'
#                     count = 1
#                     last_c = c
#             pattern = next_pattern + f'{count}{last_c}'
#             n -= 1
#         return pattern
class Solution:
    def countAndSay(self, n: int) -> str:
        return '1' if n == 1 else self._countAndSay(n - 1, '1')

    def _countAndSay(self, n: int, pattern: str) -> str:
        results = ''.join([f'{len(list(g))}{k}' for k, g in groupby(pattern)])
        return results if n == 1 else self._countAndSay(n - 1, results)


if __name__ == '__main__':
    print(countAndSay('self', 1))
    print(countAndSay('self', 4))
