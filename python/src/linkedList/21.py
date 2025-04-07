# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #setup a dummy node to track either an exception case or store the result
        result = ListNode()
        #if both lists are empty, None
        if(not list1 and not list2):
            return None
        #if empty first list, return list2
        if(not list1):
            return list2
        #if empty list2, return list1
        if(not list2 ):
            return list1
        #set the lowest node between each lists as the first node in the result
        result.next = list1 if list1.val < list2.val else list2
        #work against merged, which is pointing at the first node in the result.
        #we will build on this LL and return the result, which remains at the head
        merged = result
        #while elements in either list have not been added to the result
        while( list1 or list2 ):
            #if we've added all elements of list2, start ramming in list1 nodes to the merged list
            if(not list2):
                merged.next = list1
                list1 = list1.next
            #if we've added all elements of list1, start ramming in list2 nodes to the merged list
            elif(not list1):
                merged.next = list2
                list2 = list2.next
            #if list 1 has the smallest current node
            elif(list1.val <= list2.val):
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            merged = merged.next
                
        return result.next
  