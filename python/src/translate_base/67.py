class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #convert to base 2 integer
        a_int = int(a,2)
        b_int = int(b,2)
        #convert sum to bin, then str and range losing the 0b
        return str(bin(a_int + b_int))[2:]