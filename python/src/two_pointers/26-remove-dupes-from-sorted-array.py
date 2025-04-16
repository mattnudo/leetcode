class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        return the number of unique elements in nums
        """
        #2 pointers, 1 fast, 1 slow
        left, right = 0, 0
        #runtime: O(n) mem: O(n)
        while right < len(nums):#till eol
            # when the values of the pointers =, right++
            if nums[left] == nums[right]: 
                right+=1
            #when values are !=, left++ and set the right value to the left index's value
            elif nums[right] != nums[left]:
                left+=1
                nums[left] = nums[right]
        #when the right pointer hits the end of the list, return the range from 0 to the left +1
        return len(nums[:left+1])
