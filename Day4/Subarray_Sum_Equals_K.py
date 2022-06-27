class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ##calculate sum->calculate difference from target ->agar sum exist nahi krta toh usko add krenge hashmap mein - agar sum exist krta h toh uska count incerement kar denge
        # at the end we'll sum up the total sum of prefixSum values i.e count
        
        res=0
        diff=0
        currSum=0
        prefixSum={0:1}
        
        for num in nums:
            
            #calculate sum
            currSum+=num
            
            #calculate difference from target
            diff=currSum-k
            
            # if we can find a difference from the hashmap that means we can form the required target value
            res+=prefixSum.get(diff,0)
            
            #agar sum exist nahi krta toh usko add krenge hashmap mein - agar sum exist krta h toh uska count incerement kar denge
            prefixSum[currSum]=1+prefixSum.get(currSum,0)
            
            
        return res
