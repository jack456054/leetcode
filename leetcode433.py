class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue: List = deque([start])
        bank_set: Set[str] = set(bank)
        changes: int = 0
        return self.bfs({start}, 0, bank_set, end)

    def compare_c(self, s: str, s_set: Set[str]) -> Set[str]:
        results: Set[str] = set()
        for gene in s_set:
            diff: int = 0
            for i, c in enumerate(gene):
                if s[i] != c:
                    diff += 1
                if diff > 1:
                    break
            if diff == 1:
                results.add(gene)
        return results

    def bfs(self, queue: Set[str], changes: str, bank_set: Set[str], end: str):
        if not queue:
            return -1
        next_level_queue = set()
        for g in queue:
            next_queue = self.compare_c(g, bank_set)
            if end in next_queue:
                return changes + 1
            next_level_queue |= next_queue
            bank_set -= next_queue
        return self.bfs(next_level_queue, changes + 1, bank_set, end)
