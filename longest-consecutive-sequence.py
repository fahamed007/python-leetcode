#https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s1=sorted(set(nums))

        longest =0
        for i in range(len(s1)):
            if i ==0:
                curr=1
            elif s1[i] ==s1[i -1] +1:
                curr +=1
            else:
                curr =1
            longest =max(longest,curr)
        
        return longest
