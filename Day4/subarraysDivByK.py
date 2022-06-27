class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int: 
       
        dict_t=collections.defaultdict(int)
        dict_t[0]=1
        curr_sum=0
        count=0
        
        for num in nums:
          
            curr_sum+=num
            count+=dict_t[curr_sum%k]
            dict_t[curr_sum%k]+=1
         
        return count
   
