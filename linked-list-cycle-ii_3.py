#https://leetcode.com/problems/linked-list-cycle-ii/description/
#142. Linked List Cycle II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer=head
        fast_pointer=head 
        while fast_pointer and fast_pointer.next:
            fast_pointer=fast_pointer.next.next
            slow_pointer=slow_pointer.next

            if slow_pointer  ==fast_pointer:
                break 
        if not fast_pointer or not fast_pointer.next:
            return None 
        

        fast_pointer=head

        while fast_pointer!=slow_pointer:
            slow_pointer =slow_pointer.next
            fast_pointer=fast_pointer.next
        
        return fast_pointer
