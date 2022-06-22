class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        for num in nums:# find elements other than 0 and exchange its position in ordered form 
            if num!=0:
                nums[i]=num
                i=i+1
        for j in range(i, len(nums)):# add remaining 0's after k different elements
            nums[j]=0
                
