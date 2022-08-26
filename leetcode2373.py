class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        margin = len(grid) - 2
        result = [[0] * margin for i in range(margin)]
        for rm in range(margin):
            for cm in range(margin):
                local_max = 0
                for i in range(3):
                    for j in range(3):
                        local_max = max(grid[j + cm][i + rm], local_max)
                result[cm][rm] = local_max
        return result
