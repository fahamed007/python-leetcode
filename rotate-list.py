#https://leetcode.com/problems/rotate-list/description/
#61. Rotate List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n =0
        temp=head
        while temp:
            temp=temp.next
            n +=1
        k =k%n
        for i in range(k):
            node = ListNode()
            node.next=head
            head=node
        
        pt1=head
        pt2=head
        for i in range(k):
            pt2=pt2.next
        prev = None
        while pt2:
            prev=pt1
            pt1=pt1.next
            pt2=pt2.next
        
        temp1=pt1
        temp2=head
        while temp1:
            temp2.val=temp1.val
            temp1=temp1.next
            temp2=temp2.next
        prev.next=None

        
        return head
        
