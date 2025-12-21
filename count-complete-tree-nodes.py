#https://leetcode.com/problems/count-complete-tree-nodes/description/?envType=study-plan-v2&envId=top-interview-150
#222. Count Complete Tree Nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def traverse(node):
            if not node:
                return 0
            self.ans +=1
            traverse(node.left)
            traverse(node.right)
            return self.ans

        return traverse(root)

        
