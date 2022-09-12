import heapq
from typing import List

# class Solution:
#     def maxPerformance(self, n, speed, efficiency, k):
#         people = sorted(zip(speed, efficiency), key=lambda x: -x[1])
#         result, sum_speed = 0, 0
#         min_heap = []
#         for i, (s, e) in enumerate(people):
#             if i < k:
#                 sum_speed += s
#                 heapq.heappush(min_heap, s)
#             elif s > min_heap[0]:
#                 sum_speed += s - heapq.heappushpop(min_heap, s)
#             else:
#                 continue
#             result = max(result, sum_speed * e)
#         return result % 1000000007


class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        people = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        result, sum_speed = 0, 0
        max_speed = []
        for _, (s, e) in enumerate(people):
            if len(max_speed) > k - 1:
                sum_speed -= heapq.heappop(max_speed)
            sum_speed += s
            heapq.heappush(max_speed, s)
            result = max(result, sum_speed * e)
        return result % 1000000007


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2))
    print(solution.maxPerformance(3, [2, 8, 2], [2, 7, 1], 2))
    print(solution.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3))
    print(solution.maxPerformance(6, [10, 5, 1, 7, 4, 2], [2, 1, 1, 1, 7, 3], 6))
    print(
        solution.maxPerformance(
            7,
            [1, 4, 1, 9, 4, 4, 4],
            [8, 2, 1, 7, 1, 8, 4],
            6,
        )
    )
