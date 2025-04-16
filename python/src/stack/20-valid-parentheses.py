from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        """
            return whether the string has valid bracket closure
        """
        if(len(s) == 1):
            return False
        stack = []
        brackets = {"(":")", "{":"}", "[":"]"}
        for char in s:
            if char in brackets:
                stack.append(char)
                continue
            else:
                if(len(stack) == 0):
                    return False
                popped = stack.pop()
                if brackets[popped] != char:
                    return False
        if(len(stack)>0):
            return False        
        return True




