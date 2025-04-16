import heapq
class Solution:
    #O(n+n+k) -> O(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #deal with weird outliers
        if(k > len(nums)):
            return -1
        #reverse the list since heapq is minheap
        #O(n)
        heap = [-num for num in nums]
        #heapify in O(n)
        heapq.heapify(heap)
        kth = 0
        #(k)
        for k in range(k):
            kth = heapq.heappop(heap)
        return -kth