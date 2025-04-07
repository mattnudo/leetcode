#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==1):
            return len(s)
        """
            returns the length of the longest substring without repeating characters
        """
        left = 0
        longest = ""
        for index, value in enumerate(s):
            if(value in longest):
                left+=1
            else:
                potential = s[left:index+1]
                for i in potential:
                    if(potential.count(i) > 1):
                        left+=1
                        break
                longest = s[left:index+1]
        return len(longest)

soln = Solution()            
# print(soln.lengthOfLongestSubstring("abcabcbb"))
# print(soln.lengthOfLongestSubstring("bbbbb"))
#print(soln.lengthOfLongestSubstring("pwwkew"))
#print(soln.lengthOfLongestSubstring("au"))
print(soln.lengthOfLongestSubstring("ckilbkd"))