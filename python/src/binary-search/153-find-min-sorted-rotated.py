class Solution:
    def findMin(self, nums: List[int]) -> int:
        # If the array is not rotated (or sorted in ascending order), 
        # then the smallest element is the first element.
        if nums[0] <= nums[-1]:
            return nums[0]
      
        # Initialize the left and right pointers.
        left, right = 0, len(nums) - 1
      
        # Perform a binary search for the minimum element.
        while left < right:
            # Calculate the midpoint index
            mid = (left + right) // 2  # Using // for floor division in Python 3
          
            # If the element at the midpoint is greater than or equal 
            # to the first element, then the minimum is to the right.
            if nums[0] <= nums[mid]:
                left = mid + 1
            else:
                # Otherwise, the minimum is to the left, so we reduce the right bound.
                right = mid
      
        # After the loop, left will point to the smallest element.
        return nums[left]
