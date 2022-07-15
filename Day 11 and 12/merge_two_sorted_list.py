class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr= dummy=ListNode()
        while(list1 and list2):
            if(list1.val<list2.val):
                curr.next=list1
                curr, list1=curr.next,list1.next
            else:
                curr.next=list2
                curr,list2=curr.next,list2.next
        while(list1 or list2):
            if list1:
                curr.next=list1
                curr, list1=curr.next,list1.next
            else:
                curr.next=list2
                curr,list2=curr.next,list2.next
        return dummy.next

      ## used 2 dummy nodes, 1 to merge and 1 to store the value:-
      ## check if  both list are present , 
          #then check if num1 is less than num2 :  
          #if true then curr.next =list1, and move to next num in that list 
          #else curr.next =list2...
      ## -check if either of list is present then connect that particular list with curr node.
