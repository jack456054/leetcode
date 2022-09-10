from math import inf
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= 1 or k == 0:
            return 0
        upper_bound = -inf
        lower_bound = inf
        profit_list = []
        for day, price in enumerate(prices):
            if price >= upper_bound:
                if upper_bound == -inf:
                    lower_bound = price
                upper_bound = price
            else:
                if lower_bound != inf and upper_bound != lower_bound:
                    profit_list.append((lower_bound, upper_bound))
                lower_bound = price
                upper_bound = price
        if upper_bound != -inf:
            profit_list.append((lower_bound, upper_bound))
        p = len(profit_list)
        dp_price = [[0] * k for _p in range(p)]
        for _p in range(p):
            for _k in range(k):
                if _k == 0 and _p == 0:  # Base case:
                    dp_price[_p][_k] = profit_list[0][1] - profit_list[0][0]
                elif _k > _p:
                    dp_price[_p][_k] = dp_price[_p][_p]
                else:
                    result = 0
                    if _p - 1 >= 0:
                        result = max(result, dp_price[_p - 1][_k])
                    for i in range(_k, _p + 1):
                        if _k - 1 >= 0:  # Base cases if _k - 1 < 0.
                            result = max(
                                result,
                                dp_price[i - 1][_k - 1]
                                + profit_list[_p][1]
                                - profit_list[i][0],
                            )
                        else:
                            result = max(result, profit_list[_p][1] - profit_list[i][0])
                    dp_price[_p][_k] = result
        return dp_price[-1][-1]
