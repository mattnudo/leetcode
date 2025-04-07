class Solution:
    def isPalindrome(self, s: str) -> bool:
        if(s is None):
            return None
        if(s is "" or s is " "):
            return True
        """
            return whether the string is a palindrome once normalized as an alphanumeric
        """
        #convert to alphanumeric characters
        stripped = ''.join(ch for ch in s if ch.isalnum()).lower()
        left, right = 0,len(stripped)-1
        #two pointers, at at start, one at end.
        #while left < right, ensure s at left and right are equal
        while left < right:
            if(stripped[left] != stripped[right]):
                return False
            left+=1
            right-=1
        return True