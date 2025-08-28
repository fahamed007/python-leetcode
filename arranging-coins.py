#https://leetcode.com/problems/arranging-coins/?language=Python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        sum_value=0
        last = 0
        for i in range(1,n +1):
            sum_value +=i
            if sum_value <=n:
                last= i
            else:
                break
        return last