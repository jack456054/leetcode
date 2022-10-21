# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         if len(nums) == 1:
#             return False
#         distances = sorted([(num, index) for index, num in enumerate(nums)])
#         for index, value in enumerate(distances[:-1]):
#             if value[0] == distances[index + 1][0] and abs(distances[index + 1][1] - value[1]) <= k:
#                 return True
#         return False
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for index, value in enumerate(nums):
            if value in dic and abs(dic[value] - index) <= k:
                return True
            dic[value] = index
        return False
                