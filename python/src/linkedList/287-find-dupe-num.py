
from collections import Counter
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """
        return the repeated member of nums
        """
        return Counter(nums).most_common()[0][0]
        