class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA and headB:
            A, B = headA, headB
            while A!=B:
                #A = A.next if A else headB
                #B = B.next if B else headA
                
                if A: A=A.next
                else:A=headB
                    
                if B:B=B.next
                else:B=headA
            return A
        
        #here we're returning the value where A=B and not actually intersecting it
        
          
