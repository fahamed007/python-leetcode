#2140. Solving Questions With Brainpower
#https://leetcode.com/problems/solving-questions-with-brainpower/description/
#https://www.youtube.com/watch?v=D7TD_ArkfkA

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        def dp(i):
            if i >=len(questions):
                return 0
            if i in memo:
                return memo[i]
            j = i +questions[i][1] +1
            memo[i] = max(dp(i+1), questions[i][0] + dp(j))
            return memo[i]
        memo ={}
        dp(0)
        return max(memo.values())
    
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        dp =[0] * (n+1)
        for i in range(n -1, -1,-1):
            j = i+questions[i][1] +1
            dp[i] =max(questions[i][0]+dp[min(j,n)],dp[i+1])
        return dp[0]

