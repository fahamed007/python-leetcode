#https://leetcode.com/problems/linked-list-cycle-ii/description/
#142. Linked List Cycle II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow_pointer=head 
        tracker={head}
        while slow_pointer:
            slow_pointer=slow_pointer.next
            if slow_pointer in tracker:
                return slow_pointer
            tracker.add(slow_pointer)
        return None
