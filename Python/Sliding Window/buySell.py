class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            print("rtyui", r < len(prices), r, len(prices))

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP


solution = Solution()
result = solution.maxProfit([7, 1, 5, 3, 6, 4])
print(result)
