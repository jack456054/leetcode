class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        travel_days = set(days)
        for day in range(days[-1] + 1):
            if day in travel_days:
                dp[day] = min(
                    dp[day - 1] + costs[0],
                    dp[max(0, day - 7)] + costs[1],
                    dp[max(0, day - 30)] + costs[2],
                )
            else:
                dp[day] = dp[day - 1]
        return dp[-1]
