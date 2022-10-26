class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s: int = nums[0] % k
        sum_list: List[int] = [nums[0] % k]
        for n in nums[1:]:
            s += n
            s = s % k
            if s == 0:
                return True
            sum_list.append(s)
        sum_list = sorted([(value, index) for index, value in enumerate(sum_list)])
        sum_list = groupby(sum_list, key=lambda x: x[0])
        for _, g in sum_list:
            g = list(g)
            if len(g) > 2 or (len(g) == 2 and abs(g[0][1] - g[1][1]) > 1):
                return True
        return False
