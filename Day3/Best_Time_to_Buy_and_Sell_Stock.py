class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right=0,1
        ##l=buy, r=sell
        ##profit=buy-sell
        max_profit=0
        if(len(prices)==0):
            return 0
        while(right<len(prices)):
            profit=prices[right]-prices[left]  
            if(profit>0):
                max_profit=max(max_profit,profit)
            else: left = right
            
            right=right+1
            
        return max_profit
