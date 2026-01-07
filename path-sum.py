#https://leetcode.com/problems/path-sum/description/
#112. Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,val):
            if not node:
                return False
            if not node.left and not node.right:
                return val+node.val ==targetSum
            l_child_sum=dfs(node.left, val+node.val)
            r_child_sum=dfs(node.right, val+node.val)
            return l_child_sum or r_child_sum
        
        return dfs(root,0)
