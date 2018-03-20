def reverse(self, x):
    result, neg = 0, False
    x, neg = abs(x), True if x < 0 else 0
    while x != 0:
        result *= 10
        result += x % 10 if not (x % 10 == 0 and result == 0) else 0
        x //= 10
    if abs(x) >= 2 ** 31:
        return 0
    return -result if neg else result


if __name__ == '__main__':
    print(reverse('self', 120))
    print(reverse('self', -123))
