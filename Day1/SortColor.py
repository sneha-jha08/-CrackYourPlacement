class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # first we will count each color and then place those color in ascending order
        red, white, blue=0,0,0
        
        for i in range(0,len(nums)):
            if(nums[i])==0:
                red+=1;
            elif (nums[i]==1):
                white+=1;
            elif(nums[i]==2):
                blue+=1;
        nums[0:0+red]=[0]*red;##lets say red=5 so nums[0:4]=[0,0,0,0,0] as [0]*red will duplicate that element red no of times
        nums[0+red:red+white]=[1]*white ;
        nums[red+white:red+white+blue]=[2]*blue;
