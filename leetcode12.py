class Solution:
    def intToRoman(self, num: int) -> str:
        digit: List[str] = ['MMM', 'MDC', 'CLX', 'XVI'][::-1]
        results: str = ''
        for index, value in enumerate(str(num)[::-1]):
            d = digit[index]
            itor_dict: Dict[int, str] = {
                0: '',
                1: d[2],
                2: d[2] * 2,
                3: d[2] * 3,
                4: d[2] + d[1],
                5: d[1],
                6: d[1] + d[2],
                7: d[1] + d[2] * 2,
                8: d[1] + d[2] * 3,
                9: d[2] + d[0],
            }
            results = itor_dict[int(value)] + results
        return results
