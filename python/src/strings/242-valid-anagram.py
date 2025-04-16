class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sort both words and check equality
        return sorted(s) == sorted(t)
        