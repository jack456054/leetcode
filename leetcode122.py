class Solution:
    def maxProfit(self, prices):
        min = 0
        profit = 0
        length = len(prices)
        for index, value in enumerate(prices):
            if index == 0:
                min = value
            elif prices[index] <= prices[index - 1]:
                profit += prices[index - 1] - min
                min = value
            elif index == length - 1:
                profit += value - min
        return profit


if __name__ == '__main__':
    print(Solution.maxProfit("self", [7, 1, 5, 3, 6, 4]))
    print(Solution.maxProfit("self", [7, 6, 4, 3, 1]))
    print(Solution.maxProfit("self", [1, 2, 3, 4, 5]))
