from collections import defaultdict

import bisect


class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.arr_dict = self.query_dict(arr)

    def query(self, left: int, right: int, value: int) -> int:
        left_bound = bisect.bisect_left(self.arr_dict[value], left)
        right_bound = bisect.bisect_right(self.arr_dict[value], right)
        return right_bound - left_bound

    def query_dict(self, arr: List[int]):
        dic = defaultdict(list)
        for index, value in enumerate(arr):
            dic[value].append(index)
        return dic


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
