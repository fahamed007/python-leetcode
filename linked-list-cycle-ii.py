#https://leetcode.com/problems/linked-list-cycle-ii/
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
        
        fast_pointer_1=head.next
        fast_pointer_2=head
        slow_pointer=None 
        tracker=set()
    

        while fast_pointer_1 and fast_pointer_1.next:
            fast_pointer_1 =fast_pointer_1.next.next
            fast_pointer_2=fast_pointer_2.next.next
            if not slow_pointer:
                slow_pointer =head
            else:
                slow_pointer =slow_pointer.next
            tracker.add(slow_pointer)

            if fast_pointer_1 in tracker and fast_pointer_2 in tracker:
                return fast_pointer_2
            if fast_pointer_1 in tracker:
                return fast_pointer_1
            if fast_pointer_2 in tracker:
                return fast_pointer_2
        
        return None
