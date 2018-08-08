def climbStairs(self, n):
    if not n:
        return 0
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    print(climbStairs('self', 0))
    print(climbStairs('self', 3))
