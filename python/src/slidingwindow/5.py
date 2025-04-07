class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s)==1):
            return s
        def isPalindrome(s):
            reversed = s[::-1]
            return s == reversed
        left=0
        right=1
        result=[]
        #while left < 
        while(left <= len(s)-1):
            slice = s[left: right]
            if(isPalindrome(slice) and right <= len(s)):
                if(len(slice) > len(result)):
                    result = slice
                right+=1
            #if len(result) > right - left, return result
            elif(len(result) > len(s) - left):
                return result
            elif(right > len(s)):
                left+=1
                right = left+1
            else:
                right+=1
                
        return result