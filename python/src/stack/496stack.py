class Solution:
    #O(n+k)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        returns an array of the next greater element to the right in nums2 for all elements in nums1
        """
        #use a stack to keep track of elements in order so we can find the next greater element
        stack = []
        #use a dict to map elements to their next greatest element
        num1ToNextGreatest = {}
        # populate a stack and map of next greatest numbers in the array
        #O(k)
        for num in nums2:
            #populate the map with the element -> next greatest element
            while( stack and num > stack[-1]):
                num1ToNextGreatest[stack.pop()] = num
            stack.append(num)
            #populate and return array of next greatest for each element in num1
            #O(n)
        return [ num1ToNextGreatest.get(num,-1) for num in nums1]




