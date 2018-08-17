class Solution:
    def maxProfit(self, prices):
        profit = 0
        min = float("inf")
        for index, value in enumerate(prices):
            if value < min:
                min = value
            if index:
                profit = max(profit, value - min)
        return profit


if __name__ == '__main__':
    print(Solution.maxProfit("self", [7, 1, 5, 3, 6, 4]))
    print(Solution.maxProfit("self", [7, 6, 4, 3, 1]))
