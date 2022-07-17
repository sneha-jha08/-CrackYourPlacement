class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None , head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
      # prev initially stores None and curr stores the value of head
      # let our LL be 1->2->3
      # so prev=None
      # curr=1
      # now well take a temporary variable that will store the value of curr.next i.e 2 rn
      # we'll update the value of curr.next to prev so the LL will be None<-1
      # next prev will be uodated to curr i.e 1 rn
      # curr will be updated to temp i.e 2 rn
      # next list will be none<- 1<-2<-3
      # as our curr will be none the loop will end
      
