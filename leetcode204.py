import math


class Solution(object):
    def countPrimes(self, n):
        for number in range(1, math.floor(math.sqrt(n)) + 1):
            print(number)


if __name__ == '__main__':
    print(Solution.countPrimes("self", 10))
    print(Solution.countPrimes("self", 20))
