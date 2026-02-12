#70. Climbing Stairs
#https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i):
            if i  <0:
                return 0
            if i  ==1:
                return 1
            if i  ==2:
                return 2
            if i in memo:
                return memo[i]

            memo[i] =dp(i -1) + dp(i-2)
            return memo[i]
        memo ={}
        return dp(n)
      
class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        dp =[0] *n
        dp[0] =1
        dp[1] =2
        for i in range(2,n):
            dp[i] =dp[i-1] +dp[i-2]
        return dp[n-1]
    


