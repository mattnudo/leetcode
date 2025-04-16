from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
            return whether the list containts any duplicate entries
        """
        #need to count the elements
        #get the most common and if count>1, false else true
        counted = Counter(nums)#O(n) mem: O(n)
        return counted.most_common()[0][1] > 1