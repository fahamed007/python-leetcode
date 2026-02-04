#https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/description/
#1196. How Many Apples Can You Put into the Basket
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        ans =0
        total_weight =5000 
        for apple in weight:
            total_weight -=apple
            if total_weight <0:
                return ans
            ans +=1
        return ans
