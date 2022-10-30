class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == len(grid[0]) == 1:
            return 0
        seen = {(0, 0, k)}
        queue = deque([(0, 0, k, 0)])
        while queue:
            pos = queue.popleft()
            for i, j in [(pos[0] + 1, pos[1]), (pos[0], pos[1] + 1), (pos[0] - 1, pos[1]), (pos[0], pos[1] - 1)]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                    if grid[i][j] == 1 and pos[2] > 0 and (i, j, pos[2] - 1) not in seen:
                        seen.add((i, j, pos[2] - 1))
                        queue.append((i, j, pos[2] - 1, pos[3] + 1))
                    elif grid[i][j] == 0 and (i, j, pos[2]) not in seen:
                        if i == len(grid) - 1 and j == len(grid[0]) - 1:
                            return pos[3] + 1
                        seen.add((i, j, pos[2]))
                        queue.append((i, j, pos[2], pos[3] + 1))
        return -1
