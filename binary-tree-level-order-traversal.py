#https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#102. Binary Tree Level Order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result =[]
        queue=deque()
        queue.append(root)
        while queue:
            total=len(queue)
            temp_result=[]
            for i in range(total):
                node=queue.popleft()
                temp_result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(temp_result)
        return result
