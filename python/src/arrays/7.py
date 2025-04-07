#https://leetcode.com/problems/reverse-integer/description/

def reverse(x: int) -> int:
    string = str(x)
    NEGATIVE_SIGN = "-"
    negative = string[0] == NEGATIVE_SIGN
    if(negative):
        string = string[1:]
    
    string = string[::-1]
    integer = int(string)
    string = str(integer)
    return string if not negative else NEGATIVE_SIGN+string
    
    

print(reverse(123))
print(reverse(-123))
print(reverse(120))

#consider negatives 
#consider trailing 0s
#strip sign, convert to string. reverse string. add sign. 