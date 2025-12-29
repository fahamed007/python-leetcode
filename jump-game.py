#https://leetcode.com/problems/jump-game/
#55. Jump Game
#https://www.youtube.com/watch?v=Yan0cv2cLy8
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goals =len(nums) -1

        for i in range(len(nums) -1, -1, -1):
            if i +nums[i] >=goals:
                goals =i

        return goals ==0


