#https://leetcode.com/problems/longest-common-prefix/description/

def longestCommonPrefix(strs: list[str]) -> str:
    if(not strs or len(strs)==0):
        return ""
    longest_prefix = ""
    #Populate multidim
    matrix = [list(s) for s in strs]
    lcp = ""

    column = 0

    while column < 

        




# prefix implies starting of strings, so we can use one pointer across all
# turn into a multidim array of strings

print(longestCommonPrefix(["flower","flow","flight"]))#"fl"
print(longestCommonPrefix(["dog","racecar","car"]))#""