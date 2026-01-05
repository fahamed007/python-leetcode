#https://leetcode.com/problems/remove-linked-list-elements/
#203. Remove Linked List Elements
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        hp=ListNode
        hp.next=head
        head=hp
        temp=head.next
        prev=head
        
        while temp:
            if temp.val !=val:
                prev=temp
            else:
                prev.next=temp.next
            temp=temp.next
        return head.next
                
