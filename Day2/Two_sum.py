class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        
        for i in range(0,len(nums)):
            comple=target-nums[i]
            if comple in hashmap and hashmap[comple]!=i:
                return[i,hashmap[comple]]
            hashmap[nums[i]]=i
