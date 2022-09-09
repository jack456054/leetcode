from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.results = list()
        for i in range(1, 10):
            if k == 0:
                self.results.append(int(str(i) * n))
            else:
                self._numsSameConsecDiff(n, k, str(i))
        return self.results

    def _numsSameConsecDiff(self, n: int, k: int, cur_num: str) -> List[int]:
        if len(cur_num) == n:
            self.results.append(int(cur_num))
            return
        last_dig = int(cur_num[-1])
        if last_dig - k >= 0:
            self._numsSameConsecDiff(n, k, cur_num + str(last_dig - k))
        if last_dig + k <= 9:
            self._numsSameConsecDiff(n, k, cur_num + str(last_dig + k))


if __name__ == "__main__":
    s = Solution()
    s.numsSameConsecDiff(3, 7)
    s.numsSameConsecDiff(2, 0)
