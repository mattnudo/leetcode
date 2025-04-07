#https://leetcode.com/problems/two-sum/description/

def two_sum(nums, target):
    result = {}
    for index,value in enumerate(nums):
        if (target-value in result):
            return [result[target-value], index]
        result[value] = index

def twoSum(nums: list[int], target: int) -> list[int]:
        left, right = 0, len(nums)-1
        while (left <= right):
            summed = nums[left] + nums[right]
            if(summed == target):
                return (left, right)
            elif(summed <= target):
                left+=1
            else:
                right-=1

print(two_sum([2,7,11,15], 9))

print(two_sum([3,2,4], 6))

print(two_sum([3,3], 6))

print(twoSum([2,7,11,15], 9))

print(twoSum([3,2,4], 6))

print(twoSum([3,3], 6))