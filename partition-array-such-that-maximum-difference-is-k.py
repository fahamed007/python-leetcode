#https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/description/
#2294. Partition Array Such That Maximum Difference Is K
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        left=0
        right=0
        ans=0
        n=len(nums)
        nums.sort()

        while right <n:
            max_val =nums[left] +k
            while right <n and  nums[right] <=max_val:
                right +=1
            ans +=1
            left =right
        return ans
