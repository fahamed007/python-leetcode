#https://leetcode.com/problems/last-stone-weight/description/
#1046. Last Stone Weight
from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=list(map(lambda x:-x, stones))
        heapify(stones)
        while len(stones) >=2:
            stone1=heappop(stones)
            stone2=heappop(stones)
            reminder= abs(stone1 - stone2)
            if reminder >0:
                heappush(stones,-reminder)
        return 0 if len(stones) ==0 else -stones[0]
