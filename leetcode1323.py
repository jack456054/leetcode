# class Solution:
#     def maximum69Number (self, num: int) -> int:
#         num = str(num)
#         six = re.search('6', num)
#         if six:
#             first_six = six.span()[0]
#             return int(num[:first_six] + '9' + num[first_six + 1:])
#         else:
#             return int(num)

class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        return int(num.replace('6', '9', 1))
