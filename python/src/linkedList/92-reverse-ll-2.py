## Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#https://leetcode.com/problems/reverse-linked-list-ii/
#https://algo.monster/liteproblems/92
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        #make a dummy to handle full reversal case
        dummy = ListNode(0)
        dummy.next = head

        #create list for items before reversal
        before = dummy

        for index in range(left - 1):
            before = before.next

        reversed = before.next
        current = reversed
        last = None

        #reverse list
        for x in range(right - left + 1):
            temp = current.next
            current.next = last
            last = current
            current = temp
        
        #connect before, reversed, and remainder
        before.next = last
        reversed.next=current

        return dummy.next
            
