
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits=[]
        
        for i in range(1,len(prices)):
            if(prices[i]-prices[i-1]):
                profits.append(max(0,prices[i]-prices[i-1])) 
        return sum(profits)
                ##list, return sum of all profits but holding is for only 1 day
