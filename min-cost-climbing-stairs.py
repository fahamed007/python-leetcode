#746. Min Cost Climbing Stairs
#https://leetcode.com/problems/min-cost-climbing-stairs/description/
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n= len(cost)
        arr =[0] *(n+1)
        for i in range(2,n+1):
            arr[i] = min(arr[i-1]+cost[i-1],arr[i-2]+cost[i-2])
        return arr[n]


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(n):
            if n  <=1:
                return 0
            if n in memo:
                return memo[n]
            memo[n] = min(dp(n-1)+cost[n-1],dp(n-2)+cost[n-2])
            return memo[n]
        memo={}
        n=len(cost)
        return dp(n)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n =len(cost)
        arr =[0] *(n+1)
        for i in range(2,n+1):
            arr[i] =min(arr[i-1] +cost[i-1],arr[i-2] +cost[i-2])
        
        return arr[n]
