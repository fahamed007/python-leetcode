#https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#160. Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        tempA =headA
        teamB=headB

        len_a=1
        len_b=1
        while tempA:
            tempA =tempA.next
            len_a +=1

        while teamB:
            teamB =teamB.next
            len_b +=1

        tempA2=headA
        tempB2=headB
        if len_a >len_b:
            for _ in range(len_a -len_b):
                tempA2 =tempA2.next
            
        elif len_a <len_b:
            for _ in range(len_b - len_a):
                tempB2 =tempB2.next
        
        while  tempA2:
            if tempA2 == tempB2:
                return tempA2
            tempA2=tempA2.next
            tempB2=tempB2.next
        
        return None
