
class Solution:

    def findMinDiff(self, arr,n,m):

        # code here
        arr.sort()
        
        if (n==0 or m==0):
            return 0
        if(n<m):
            return -1
            
        min_diff=arr[n-1]-arr[0]
        
        for i in range(len(arr)-m+1):
            min_diff=min(min_diff,arr[i+m-1]-arr[i])
            
        return min_diff
