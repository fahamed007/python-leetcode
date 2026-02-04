#https://leetcode.com/problems/minimum-operations-to-halve-array-sum/description/
#2208. Minimum Operations to Halve Array Sum
from heapq import *
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target_sum=sum(nums) /2
        nums=[-x for x in nums]
        heapify(nums)
        ans =0
        while target_sum >0:
            ans +=1
            val=heappop(nums)
            target_sum +=val/2
            heappush(nums,val/2)
        return ans 
