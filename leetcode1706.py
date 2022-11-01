class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        results: List[int] = []
        for j, _ in enumerate(grid[0]):
            results.append(self._findBall(0, j, grid))
        return results
                
    
    def _findBall(self, i: int, j: int, grid: List[List[int]]):
        if grid[i][j] == 1:
            if j + 1 < len(grid[0]):
                if grid[i][j + 1] == 1:
                    return j + 1 if i == len(grid) - 1 else self._findBall(i + 1, j + 1, grid)
            return -1
        elif grid[i][j] == -1:
            if j - 1 >= 0:
                if grid[i][j - 1] == -1:
                    return j - 1 if i == len(grid) - 1 else self._findBall(i + 1, j - 1, grid)
            return -1
        else:
            return -1 
            