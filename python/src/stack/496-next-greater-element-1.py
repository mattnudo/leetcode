#https://leetcode.com/problems/next-greater-element-i/
def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        for i,num in enumerate(nums1):
            temp = nums2
            index=temp.index(num)
            print(index)
            for number in temp[index:]:
                 if(number > num):
                      result.append(number)
                      break
            if(len(result)<i+1):
                result.append(-1)
        return result

print(nextGreaterElement([4,1,2],[1,3,4,2]))