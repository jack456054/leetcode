from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        len_utf8 = 1
        for _, number in enumerate(data):
            bitstring = format(number, 'b').zfill(8)
            if bitstring.startswith('0') and len_utf8 == 1:
                continue
            elif bitstring.startswith('1') and len_utf8 == 1:
                num_of_starting_one = len(bitstring.split('0')[0])
                if bitstring[1] == '0' or num_of_starting_one > 4:
                    return False
                else:
                    len_utf8 = num_of_starting_one
            elif bitstring.startswith('10'):
                len_utf8 -= 1
            else:
                return False
        return True if len_utf8 == 1 else False
