class Solution:
    #runtime: O(n), mem: O(n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
            returns the indices of the two numbers in the numbers array that equal the target
        """
        if len(numbers) == 0:
            return numbers
        #two pointers, left at start, right at end
        left, right = 0, len(numbers)-1
        #loop over the array, left <= right
        while left <= right:
            #if sum of the numbers < target, right--
            if(numbers[left] + numbers[right] == target):
                return [left+1, right+1]
            elif(numbers[left] + numbers[right] > target):
                right-=1
            #if sum of numbers > target, right++
            else:
                left+=1
        return numbers