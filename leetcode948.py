from collections import deque
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        return_score = 0
        tokens.sort()
        tokens = deque(tokens)
        while tokens:
            if power >= tokens[0]:
                score += 1
                return_score = 0
                power -= tokens.popleft()
            elif score > 0:
                score -= 1
                return_score += 1
                power += tokens.pop()
            else:
                break
        return score + return_score
