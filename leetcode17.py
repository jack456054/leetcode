class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        number_map: Dict[int, List[str]] = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mon',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        results = product(*[number_map[x] for x in digits])
        return [''.join(x) for x in results]
