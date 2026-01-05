#https://leetcode.com/problems/reverse-linked-list/description/
#206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr_head=head 
        temp =head
        while temp and temp.next :
            node= temp.next
            temp.next = node.next
            node.next=curr_head
            curr_head=node
        return curr_head
