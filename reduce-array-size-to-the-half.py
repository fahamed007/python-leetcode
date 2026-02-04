#https://leetcode.com/problems/reduce-array-size-to-the-half/description/
#1338. Reduce Array Size to The Half
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        total_len=math.ceil(len(arr)/2)
        freq={}
        for val in arr:
            if val in freq:
                freq[val] +=1
            else:
                freq[val] =1
        ans =0

        for val in sorted(freq.values(),reverse=True):
            total_len -=val
            ans +=1
            if total_len <=0:
                return ans
