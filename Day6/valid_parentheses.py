class Solution:
    def isValid(self, s: str) -> bool:
        #use one hashmap to store all pairs
        #use a stack to check if the brackets are in pair
        
        pair={0:None,'(':')','{':'}','[':']'}
        stack=[]
        
        for brack in s:
            if brack in pair:
                stack.append(brack)
            elif stack==[] or (pair[stack.pop()]!= brack) :
                    return False
        return stack==[]
