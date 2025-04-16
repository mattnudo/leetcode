#https://leetcode.com/problems/median-of-two-sorted-arrays/description/

def findMedianSortedArrays(nums1, nums2):
    nums3 = sorted(nums1+nums2)
    return sum(nums3)/len(nums3)
      

nums1=[1,2]
nums2=[3,4]
print(findMedianSortedArrays( nums1, nums2  ))
