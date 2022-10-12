class Solution:
    def concatenatedBinary(self, n: int) -> int:
        results: str = ''
        for i in range(1, n + 1):
            results += f'{i:b}'
        return (int(results, 2)) % (pow(10, 9) + 7)
