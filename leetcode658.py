class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        results: List[Tuple[int, int]] = []
        for n in arr:
            results.append((n, abs(n-x)))
        results.sort(key=lambda x: (x[1], x[0]))
        return sorted([x[0] for x in results[:k]])
