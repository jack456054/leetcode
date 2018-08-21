import collections
import math


class Solution(object):
    def countPrimes(self, n):
        count = 1
        primes = collections.defaultdict(list)
        primes[0], primes[1] = False, False
        for number1 in range(2, math.floor(math.sqrt(n)) + 1):
            for number2 in range(number1 ** 2, n, number1):
                if primes[number2] is not False:
                    count += 1
                primes[number2] = False
        if n - 1 - count < 0:
            return 0
        return n - 1 - count


if __name__ == '__main__':
    print(Solution.countPrimes("self", 10))
    print(Solution.countPrimes("self", 20))
    print(Solution.countPrimes("self", 0))
    print(Solution.countPrimes("self", 2))
    print(Solution.countPrimes("self", 1500000))
