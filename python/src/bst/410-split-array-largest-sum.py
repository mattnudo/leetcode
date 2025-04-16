#https://leetcode.com/problems/split-array-largest-sum/
def splitArray(nums: list[int], m: int) -> int:
    def condition(watermark):
        count=1
        total = 0
        for num in nums:
            total += num
            if(total > watermark):
                count+=1
                total = num
                if(count > m):
                    return False
        return True

    left, right = max(nums), sum(nums)
    while (left < right):
        mid = left + (right - left) // 2
        if(condition(mid)):
            right = mid
        else: 
            left = mid + 1
    return left 

# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
# Return the minimized largest sum of the split.
# A subarray is a contiguous part of the array.
# output: minimized largest sum of the split of nums into m lists

# Example 1:

# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
# Example 2:
print(splitArray([7,2,5,10,8],2))

# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
print(splitArray([1,2,3,4,5],2))