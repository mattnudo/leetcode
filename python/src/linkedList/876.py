# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        #2 pointers, one fast, one slow, when fast is out of nodes, return slow
        left, right = head, head
        while right  :
            left = left.next
            right = right.next.next
            if not right or not right.next:
                return left
        return head