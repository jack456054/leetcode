class Solution:
    def smallestNumber(self, pattern: str) -> str:
        length = len(pattern)
        result = [0] * (length + 1)
        for i in range(length + 1):
            result[i] = i + 1
        conti = 1
        last_c = 'I'
        for index, value in enumerate(pattern):
            if value == 'D':
                if last_c == 'D':
                    conti += 1
                else:
                    conti = 2
                last_c = 'D'
            else:
                if last_c == 'D':
                    result[index + 1 - conti : index + 1] = result[
                        index + 1 - conti : index + 1
                    ][::-1]
                last_c = 'I'
        if last_c == 'D':
            result[-(conti):] = result[-(conti):][::-1]
        return ''.join(map(str, result))
