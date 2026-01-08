#https://leetcode.com/problems/count-univalue-subtrees/description/
#250. Count Univalue Subtrees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.ans =0
        def dfs(node,values):
            if not node:
                return  values

            values1= dfs(node.left,values)
            values2=dfs(node.right,values)
            combined =values1.union(values2)
            combined.add(node.val)
            if len(combined) ==1:
                self.ans +=1
            return combined
        dfs(root,set())
        return self.ans
