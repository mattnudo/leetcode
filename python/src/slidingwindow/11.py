import heapq
#https://leetcode.com/problems/container-with-most-water/description/
def maxArea(lines:[int]) -> int:
    max=0
    left = 0
    right = 1
    while left < len(lines):
        area = min(lines[left],lines[right]) * (right-left)
        max = area if area > max else max
        if(right >= len(lines)-1):
            left+=1
        elif(lines[right] > lines[left]):
            left+=1
            right+=1
        else:
            right+=1
    return max


#loop over contents
#left and right pointer. store max value = min length values between left and right elements * distance between them
#grab the max key from the map

#loop over contents
#create a dict to map x*y -> index
#return the highest key

#negate contents, put into minheap
#iterate through, calculating the largest x*y

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))