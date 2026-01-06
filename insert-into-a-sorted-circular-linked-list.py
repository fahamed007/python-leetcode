#https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
#708. Insert into a Sorted Circular Linked List
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node =Node(insertVal)
        if not head:
            node.next=node
            head=node
            return head

        max_val=float("-inf")
        min_val=float("inf")
        temp=head
        count =0
        while temp:
            min_val =min(min_val, temp.val)
            max_val=max(max_val,temp.val)
            temp=temp.next
            if count >0 and temp == head:
                break
            count +=1

        pt1=head
        pt2=head.next

        if min_val ==max_val:
            node.next=pt2
            pt1.next=node
            return head
        outbound=  False
        inbound= False

        if insertVal <=min_val or insertVal >=max_val: 
            outbound =True
        elif insertVal >=min_val or insertVal <=max_val: 
            inbound=True

        while True:
            if outbound:
                if pt1.val == max_val and   pt2.val ==min_val:
                    break
            elif inbound:
                if insertVal >=pt1.val and insertVal <=pt2.val:
                    break
            pt1=pt1.next
            pt2=pt2.next

        node.next=pt2
        pt1.next=node

        return head
