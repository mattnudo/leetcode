# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next):
            return head
        #start with a dummy node
        reversed = None
        #head will traverse through
        #dummy will invert pointers from ahead to behind, using a temp value to store the pointer to head.next
        while head:
            temp = head.next
            head.next = reversed
            reversed = head
            head = temp
        return reversed


            
            
        