class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_dict = defaultdict(list)
        for s in strs:
            map_dict[''.join(sorted(s))].append(s)
        return map_dict.values()
