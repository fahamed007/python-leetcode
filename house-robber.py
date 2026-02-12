#198. House Robber
#https://leetcode.com/problems/house-robber/description/
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n ==1:
            return nums[0]
        arr =[0]*n
        arr[0] =nums[0]
        arr[1] =max(nums[0],nums[1])
        for i in range(2,n):
            arr[i] =max(arr[i -2] +nums[i],arr[i-1])
        
        return arr[n -1]
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(n):
            if n ==1:
                return max(nums[0],nums[1])
            if n ==0:
                return nums[0]
            if n in memo:
                return memo[n]
            memo[n] =max(dp(n-1),dp(n-2) +nums[n])
            return memo[n]        

        memo={}
        n =len(nums)
        return dp(n-1)
