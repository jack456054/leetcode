class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        pg_list = list(zip(plantTime, growTime))
        pg_list.sort(key=lambda x: (-x[1], -x[0]))
        min_day: int = 0
        current_pt : int = 0
        for _, (pt, gt) in enumerate(pg_list):
            current_pt += pt
            min_day = max(current_pt + gt, min_day)       
        return min_day
