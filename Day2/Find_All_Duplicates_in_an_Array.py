class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        check_nums=set()
        ans=[]
        for i in range(len(nums)):
            if nums[i] in check_nums:
                       ans.append(nums[i])
            check_nums.add(nums[i])
                       
        return ans
