class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for left in range(len(prices)):
            right = len(prices)-1
            while right > left:
                maxProfit = max(maxProfit, prices[right]-prices[left])
                right -= 1
        return maxProfit
        