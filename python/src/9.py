#https://leetcode.com/problems/palindrome-number/description/

def is_palindrome(x:int) -> bool:
    if(not x):
        return False
    string = str(x)
    reverse = string[::-1]
    return string == reverse

print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(10))