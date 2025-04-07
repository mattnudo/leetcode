class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> List[int]:
        """
        return the max sliding window of size k for the provided list
        """
        if(len(nums)==1):
            return nums
        maxWindow = []
        for index in range(0, len(nums)-k+1):
            maxInWindow = max(nums[index: index + k])
            maxWindow.append(maxInWindow)
        return maxWindow