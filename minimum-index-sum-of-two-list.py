#https://leetcode.com/problems/minimum-index-sum-of-two-lists/
#599. Minimum Index Sum of Two Lists
from collections import defaultdict
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1={}
        d2={}
        result =defaultdict(list)
        for i in range(len(list1)):
            if list1[i]  not in d1:
                d1[list1[i]]  =i
        

        for i in range(len(list2)):
            if list2[i]  not in d2:
                d2[list2[i]]  =i
            
        for key in d1.keys():
            if key in d2:
                result[d1[key] + d2[key]].append(key)
        
        return result[min(result.keys())]
