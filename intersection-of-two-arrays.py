#https://leetcode.com/problems/intersection-of-two-arrays/description/
#349. Intersection of Two Arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def calculate_results(min_length_array,max_length_array):
            result=[]
            for i in range(len(min_length_array)):
                if min_length_array[i] in max_length_array and min_length_array[i] not in result:
                    result.append(min_length_array[i])
            return result

        if len(nums1) <len(nums2):
            result= calculate_results(nums1,nums2)
        else:
            result= calculate_results(nums2,nums1)
        return result

        

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result =set()
        nums1=set(nums1)
        nums2=set(nums2)
        if len(nums1) <len(nums2):
            for val in nums1:
                if val in nums2:
                    result.add(val)
        else:
            for val in nums2:
                if val in nums1:
                    result.add(val)
        return list(result)

