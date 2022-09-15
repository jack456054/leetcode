class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        counter = Counter(changed)
        if counter[0] % 2 == 1:
            return []
        changed = sorted(list(set(changed)))
        for value in changed:
            if value == 0:
                if counter[value] % 2 == 1:
                    return []
                else:
                    counter[value] //= 2
            else:
                counter[value * 2] -= counter[value]
                if counter[value * 2] < 0:
                    return []
        return list(counter.elements())
