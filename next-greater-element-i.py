#https://leetcode.com/problems/next-greater-element-i/description/
#496. Next Greater Element I
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        result=[-1]*len(nums1)
        for k in range(len(nums1)):
            index=nums2.index(nums1[k])
            for i in range(index+1,n):
                if nums2[i] >nums1[k]:
                    result[k] =nums2[i]
                    break
        return result
