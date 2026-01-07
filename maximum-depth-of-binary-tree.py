#https://leetcode.com/problems/maximum-depth-of-binary-tree/
#104. Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#top-down approach
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ans =0
        def dfs(node,depth):
            if not node:
                return 0
            if not node.left and not node.right:
                self.ans =max(self.ans,depth)
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
            return self.ans
        return dfs(root,1)
    


#Bottom-up approach
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            l_depth=dfs(node.left)
            r_depth=dfs(node.right)
            return max(l_depth,r_depth) +1
        return dfs(root)
