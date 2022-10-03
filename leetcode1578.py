class Solution:
    # def minCost(self, colors: str, neededTime: List[int]) -> int:
    #     if len(colors) == 1:
    #         return 0
    #     current_color: str = None
    #     time_list: List[int] = []
    #     results: int = 0
    #     for index, color in enumerate(colors):
    #         if current_color == color:
    #             heappush(time_list, neededTime[index])
    #         else:
    #             tl_len = len(time_list)
    #             if tl_len > 1:
    #                 results += sum(nsmallest(tl_len - 1, time_list))
    #             current_color = color
    #             time_list = [neededTime[index]]
    #     tl_len = len(time_list)
    #     if tl_len > 1:
    #         results += sum(nsmallest(tl_len - 1, time_list))
    #     return results
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(colors) == 1:
            return 0
        current_color: str = colors[0]
        current_largest: int = neededTime[0]
        results: int = neededTime[0]
        for index, color in enumerate(colors[1:]):
            results += neededTime[index + 1]
            if current_color == color:
                current_largest = max(current_largest, neededTime[index + 1])
            else:
                results -= current_largest
                current_color = color
                current_largest = neededTime[index + 1]
        results -= current_largest
        return results
