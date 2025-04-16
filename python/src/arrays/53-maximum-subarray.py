class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
            return the largest sum of the subarrary
        """
        #track the traveral sum max and total sum max
        max_total = current = nums[0]
        #iterate over nums beyond the first element we've already set as max
        for num in nums[1:]:
            current = max(num,  num + current)
            if current > max_total:
                max_total=current
        return max_total
        