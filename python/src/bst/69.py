#https://leetcode.com/problems/sqrtx/

def squareRoot(num:int)-> int:
    left, right = 0, num + 1
    while( left < right):
        mid = left + (right - left ) // 2
        if(mid * mid > num):
            right = mid
        else:
            left = mid + 1
    return left - 1

print(squareRoot(4))#2
print(squareRoot(8))#2
print(squareRoot(9))#3
print(squareRoot(0))#3
print(squareRoot(1))#3