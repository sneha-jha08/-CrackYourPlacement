class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        L , maxArea , width , R = 0 , 0 , len(height)-1 , len(height)-1,
       
        for width in range(width,0,-1):
            if(height[L]<height[R]):
                maxArea,L=max(maxArea, width*height[L]),L+1
                
            else:
                maxArea,R=max(maxArea, width*height[R]),R-1
           
        return maxArea
      
      ##in this question we need to return the max area 
      ##for doing that we can find the area for each sector and compare it with each area and subsequently update the value of maxArea
      ## if the height on left hand side < right hand side :
          ##- area=height of left * width 
          ##- we will increase the value of L so that it moves ahead
          
    ## if the height on left hand side > right hand side :
          ##- area=height of right * width 
          ##- we will Decrease the value of R so that it moves behind
        
        ## and will reduce the width after each step so that we cover each height
       
