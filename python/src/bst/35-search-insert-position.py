#https://leetcode.com/problems/search-insert-position/
# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

def searchInsert(self, nums: list[int], target: int) -> int:
    left, right = 0, len(nums) 
    while(left < right):
        mid = left + (right - left) // 2
        if(nums[mid] >= target):
            right = mid
        else:
            left = mid + 1
    return left