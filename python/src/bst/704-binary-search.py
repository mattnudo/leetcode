class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        return index of target, otherwise -1
        """
        if(not target in nums):
            return -1
        if(len(nums) == 1):
            return 0
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left ) // 2
            if nums[mid] == target:
                return mid 
            elif(target < nums[mid]):
                right = mid 
            else:
                left = mid + 1
        return -1