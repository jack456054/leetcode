class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        if n == 0: 
            return ['']
        for c in range(n):
            for i in self.generateParenthesis(c):
                for j in self.generateParenthesis(n - c - 1):
                    results.append(f'({i}){j}')
        return results
