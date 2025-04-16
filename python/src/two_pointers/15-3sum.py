class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
            returns triplets [nums[i], nums[j], nums[k]] such that:
             i != j, i != k and j != k (does not include triplicates)
             and nums[i] + nums[j] + nums[k] == 0
        """
        # Sort the input array to facilitate the two-pointer approach.
        nums.sort()
        # Get the length of the array.
        n = len(nums)
        # Initialize the list to store the triplets.
        triplets = []

        # Iterate through the array.
        for i in range(n - 2):
            # If the current number is greater than 0, since the array is sorted,
            # no three numbers can add up to zero.
            if nums[i] > 0:
                break
            # Skip the same element to avoid duplicate triplets.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Set the two pointers, one just after the current element,
            # and the other at the end of the array.
            left, right = i + 1, n - 1

            # While the left pointer is less than the right pointer.
            while left < right:
                # Calculate the sum of the current three elements.
                current_sum = nums[i] + nums[left] + nums[right]
                # If the sum is less than zero, move the left pointer to the right.
                if current_sum < 0:
                    left += 1
                # If the sum is greater than zero, move the right pointer to the left.
                elif current_sum > 0:
                    right -= 1
                # If the sum is zero, we've found a valid triplet.
                else:
                    # Add the triplet to the result.
                    triplets.append([nums[i], nums[left], nums[right]])
                    # Move both the left and right pointers to continue searching.
                    left, right = left + 1, right - 1
                    # Skip duplicate elements by moving the left pointer to the right.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicate elements by moving the right pointer to the left.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        # Return the list of found triplets.
        return triplets

        