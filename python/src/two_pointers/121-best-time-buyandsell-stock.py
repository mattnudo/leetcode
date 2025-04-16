class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            return the maximum profit you can achieve from buying and selling at a later date
            If you cannot achieve a profit, return 0
        """
        max_profit = 0
        left, right = 0,1
        while( right < len(prices)):
            #if left val > right val, increment both
            #if left < right val, right++, save max
            #
            if( prices[left] > prices[right]):
                left=right
                right+=1
            else:
                #if prices at right - left > max, save it
                delta = prices[right] - prices[left]
                if(delta > max_profit):
                    max_profit = delta
                right+=1
        return max_profit

