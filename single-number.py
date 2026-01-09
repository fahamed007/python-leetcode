#https://leetcode.com/problems/single-number/description/
#136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        while i <len(nums):
            if i+1 <len(nums) and nums[i] !=nums[i+1]: 
                return nums[i]
            i +=2
            if i >len(nums):
                return nums[i-2]
    


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        if n ==1:
            return nums[0]
        nums.sort()
        
        for i in range(n):
            if 0<=i-1<=n-1 and 0<=i+1<=n-1:
                if not (nums[i-1] ==nums[i] or nums[i+1] ==nums[i]):
                    return nums[i]
            elif  0<=i-1<=n-1 :
                if nums[i-1] !=nums[i]:
                    return nums[i]
            elif 0<=i+1<=n-1:
                if nums[i+1] !=nums[i]:
                    return nums[i]

from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1

        for i in hash_table:
            if hash_table[i] == 1:
                return i
