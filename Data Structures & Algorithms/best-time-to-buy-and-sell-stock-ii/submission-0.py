class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                d+=(prices[i]-prices[i-1])
        return d            


