
#https://binarybelle.medium.com/longest-palindrome-leetcode-challenge-61b7ac197cad
from collections import Counter
class Solution:
    #
    def longestPalindrome(self, s: str) -> int:
        """
            return the length of the longest palindrome for the given string
        """
        #could go permutations using itertools ...
        #perms vs do some math ... let's do some math
        longest = 0
        #even repeats count fully
        #odd counts only 1 can be the center of the string
        middle = False
        #get the counts of the chars in the string and iterate over them
        for char, count in Counter(s).items():
            longest += count // 2 * 2
            if(not middle and count % 2 == 1 ):
                longest+=1
                middle = True
        return longest