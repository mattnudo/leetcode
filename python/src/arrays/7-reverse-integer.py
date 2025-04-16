class Solution:
    def reverse(self, x: int) -> int:
       
        string = str(x)[::-1]
        result = int(string) if string[-1] != '-' else int("-"+string[:len(string)-1])
        if(result >= math.pow(2,31)-1 or result <= math.pow(-2,31)):
            return 0
        return result
