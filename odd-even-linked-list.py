#https://leetcode.com/problems/odd-even-linked-list/
#328. Odd Even Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        even_end=head.next
        odd_end=head
        pt1=head.next

        while pt1 and pt1.next :
            temp=pt1.next
            pt1.next=temp.next
            pt1=pt1.next
            temp.next=even_end
            odd_end.next=temp
            odd_end =temp

        return head
    
