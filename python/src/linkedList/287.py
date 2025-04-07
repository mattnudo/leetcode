
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """
        return the repeated member of nums
        """
        for num in nums:
            if(nums.count(num) > 1):
                return num
        return 0
        