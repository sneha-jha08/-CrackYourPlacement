## CASE 1:: using arrays
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums=[]
        
        while head:
            nums.append(head.val)
            head = head.next
        for i in range (0, len(nums) // 2):
            if nums[i] != nums[-i-1]:
                return False
        return True
      
## CASE 2 ::using two pointers
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
         # find middle element   
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            
        #reverse second half
        # LL is 2-> 1-> None
        prev=None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
         # after reversal LL is : None->1-> 2
        
         #check if palindrome
        left, right = head, prev
        while right:
            if left.val!= right.val:
                return False
            else: 
                left=left.next
                right=right.next
        return True
