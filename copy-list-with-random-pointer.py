#https://leetcode.com/problems/copy-list-with-random-pointer/
#138. Copy List with Random Pointer
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        store={}
        temp =head
        while temp:
            node =Node(temp.val)
            store[temp] =node
            temp=temp.next
        
        temp2=head
        while temp2:
            if temp2.next is None:
                store[temp2].next
            else:
                store[temp2].next = store[temp2.next]
            if temp2.random is None:
                store[temp2].random =None
            else:
                store[temp2].random = store[temp2.random]
            temp2 = temp2.next
        return store[head]
        
