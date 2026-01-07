#https://leetcode.com/problems/symmetric-tree/description/
#101. Symmetric Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(left,right):
            if not left and not right:
                return True
            if not left:
                return False
            
            if not right:
                return False 
            
            if left.val  !=right.val:
                return False 
            
            option1=dfs(left.left,right.right)
            option2=dfs(left.right,right.left)
            return option1 and option2
        
        return dfs(root.left,root.right)
