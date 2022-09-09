import math


class Solution(object):
    def countPrimes(self, n):
        # (Method 1)
        # if n <= 2:
        #     return 0
        # primes = [True] * n
        # primes[0], primes[1] = False, False
        # for number1 in range(2, math.floor(math.sqrt(n)) + 1):
        #     if primes[number1]:
        #         for number2 in range(number1 ** 2, n, number1):
        #             primes[number2] = False
        # return primes.count(True)

        # (Method 2)
        count = 1
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0], primes[1] = False, False
        for number1 in range(2, math.floor(math.sqrt(n)) + 1):
            if primes[number1]:
                for number2 in range(number1**2, n, number1):
                    if primes[number2]:
                        count += 1
                    primes[number2] = False
        return n - count - 1


if __name__ == '__main__':
    print(Solution.countPrimes("self", 10))
    print(Solution.countPrimes("self", 20))
    print(Solution.countPrimes("self", 0))
    print(Solution.countPrimes("self", 1))
    print(Solution.countPrimes("self", 2))
    print(Solution.countPrimes("self", 1500000))
