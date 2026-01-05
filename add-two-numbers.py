#https://leetcode.com/problems/add-two-numbers/
#2. Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        result=ListNode(0)
        new_list=result
        temp1=l1
        temp2=l2
        carry=0

        while temp1 or temp2 or carry:
            if temp1 and temp2:
                val =temp1.val+temp2.val+carry
                temp1=temp1.next
                temp2=temp2.next
            elif temp1:
                val =temp1.val+carry
                temp1=temp1.next
            elif temp2:
                val =temp2.val+carry
                temp2=temp2.next
            else:
                val =carry
                carry=0
            temp_result =val %10
            carry=val//10

            temp =ListNode(temp_result)
            new_list.next=temp
            new_list =new_list.next
        return result.next





        
