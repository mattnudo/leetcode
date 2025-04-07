from collections import Counter
class Solution:
    #O(n)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
            Can the ransom note be constructed from the magazine
        """
        # number of characters matters so sets are out
        # in string is out as order matters
        # check counts of words
        
        countMagazine = Counter(magazine)#O(n)
        countRansom = Counter(ransomNote)#O(n)
        print (countMagazine, countRansom)
        #O(n)
        for letter in countRansom:
            #if the count inthe magazine < count of the note, false
            if(countMagazine[letter] < countRansom[letter]):#O(1)
                return False
        return True
