from collections import Counter
from math import ceil, floor, log


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_lower_bound = ceil(log(pow(10, len(str(n)) - 1), 2))
        power_upper_bound = floor(log(pow(10, len(str(n))), 2))
        counter_n = Counter(str(n))
        for digit in range(power_lower_bound, power_upper_bound + 1):
            if counter_n == Counter(str(pow(2, digit))):
                return True
        return False

if __name__ == '__main__':
    print(Solution().reorderedPowerOf2(1))
