class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if(len(bloomDay) < k * m):
            return -1
        def condition(days):
            flowers, bouquets = 0,0
            for bloom in bloomDay:
                if(bloom > days):
                    flowers = 0
                else:
                    bouquets += (flowers + 1) // k
                    flowers = (flowers +1 ) % k
            return bouquets >= m
                

        left, right = 1, max(bloomDay)
        while(left < right):
            mid = left + (right - left) // 2
            if(condition(mid)):
                right = mid
            else: 
                left = mid + 1
        return left
    
nums = [1,2,5,3,4]
nums.sort()
nums.reverse()
print(nums)