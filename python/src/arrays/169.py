from collections import Counter
class Solution:
    #compL O(n) mem: O(k)
    def majorityElement(self, nums: List[int]) -> int:
        #dictionary value-> count
        #return max count
        counts = Counter(nums)
        return counts.most_common()[0][0]