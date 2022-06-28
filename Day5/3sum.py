class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      
        ans=set()
        
        N , P , Z=[],[],[]
        #1. count no of positive ,  negative, zero in list
        
        for num in nums:
            if num >0:
                P.append(num)
            if num <0:
                N.append(num)
            if num==0:
                Z.append(0)
        #2. remove all duplicates from N, P
        n,p=set(N),set(P)
        
        #3. if len(Z)>3 add to ans([0,0,0]) and if even one 0 exist in Z then find its compliemnt and add to ans
            
        if len(Z)>=3:
            ans.add((0,0,0))
            
        if Z:
            for num in n:
                if -1*num in p:
                    ans.add((-1*num,0,num))
        
        #4. check if compliment of negative exist in P
        
        for i in range(len(N)):
            for j in range(i+1,len(N)):
                target=-1*(N[i]+N[j])
                if target in p:
                    ans.add(tuple(sorted([N[i],N[j],target])))
                    
                    
        #5  check if compliment of positive exist in N            
        for i in range(len(P)):
            for j in range(i+1,len(P)):
                target=-1*(P[i]+P[j])
                if target in n:
                    ans.add(tuple(sorted([P[i],P[j],target])))
                    
        return ans
