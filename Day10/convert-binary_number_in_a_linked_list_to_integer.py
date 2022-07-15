class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num=head.val
        while(head.next):
            num=num*2 +head.next.val
            head=head.next
        return num
        
        #jaise jaise number right ko shift hoga 
        #utne baar 2 se multiply hoga and finally jab head.next nahi hoga tab 
        #vo multiply nahi hoga and then well get our decimal number 
