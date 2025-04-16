class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
            returns the max average of length k within nums
        """
        # Initial sum of the first 'k' elements
        current_sum = sum(nums[:k])
        # Starting with the initial sum as the max sum
        max_sum = current_sum

        # Iterate over the list starting from the k-th element to the end
        for i in range(k, len(nums)):
            # Update the current sum by adding the next element and 
            # subtracting the (i-k)-th element, sliding the window forward
            current_sum += nums[i] - nums[i - k]
            # Update the max sum if the current sum is greater
            max_sum = max_sum if max_sum > current_sum else current_sum
      
        # Calculate the maximum average by dividing the max sum by k
        return max_sum / k