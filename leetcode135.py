from math import inf
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        result: int = 1
        current_strike = 1
        last_strike = inf
        last_comparision = 0
        last_value = ratings[0]
        for v in ratings[1:]:
            if v > last_value:
                if last_comparision == 0 or last_comparision == 1:
                    current_strike += 1
                    result += current_strike
                else:
                    last_strike = current_strike
                    current_strike = 2
                    result += 2
                last_comparision = 1
            elif v < last_value:
                if last_comparision == 1:
                    result += 1
                    last_strike = current_strike
                    current_strike = 1
                else:
                    current_strike += 1
                    result += current_strike
                    if last_comparision == -1:
                        if current_strike >= last_strike:
                            result += 1
                last_comparision = -1
            else:
                result += 1
                last_strike = inf
                current_strike = 1
                last_comparision = 0
            last_value = v
        return result
