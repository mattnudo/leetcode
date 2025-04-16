#https://leetcode.com/problems/add-two-numbers/description/ 

def list_to_linked_list(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next
    
def linked_list_to_list(lst):
    result = []
    while lst:
        result.append(lst.val)
        lst = lst.next
    return result

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rem = 0
        dummy = cur = ListNode(0)
        while (l1 or l2 or rem):
            summed = 0
            if(l1):
                summed+=l1.val
                l1 = l1.next
            if(l2):
                summed+=l2.val
                l2 = l2.next
            summed += rem
            rem = 0
            tuple = divmod(summed,10)
            # print(tuple)
            rem = tuple[0]
            quotient = tuple[1]
            cur.next=ListNode(quotient)
            cur = cur.next
        return dummy.next
        
soln = Solution().addTwoNumbers(list_to_linked_list([2,4,3]), list_to_linked_list([5,6,4]))
print(linked_list_to_list(soln))

soln = Solution().addTwoNumbers(list_to_linked_list([0]), list_to_linked_list([0]))
print(linked_list_to_list(soln))

soln = Solution().addTwoNumbers(list_to_linked_list([9,9,9,9,9,9,9]), list_to_linked_list([9,9,9,9]))
print(linked_list_to_list(soln))
