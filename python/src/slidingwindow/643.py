#https://leetcode.com/problems/maximum-average-subarray-i/description/

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """
            returns the maximum average value of list's subarray of size k
        """
        if(len(nums)==k):
            return sum(nums) / k
        if (len(nums) == 1):
            return sum(nums)
        maxAvg = 0.0
        #sliding window as we are finding a contiguous average of a subarray
        for x in range(0, len(nums)-k + 1 ):
            avg = sum(nums[x:x+k]) / k
            maxAvg = max(avg,maxAvg)
        return maxAvg
