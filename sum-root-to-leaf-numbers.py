# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def traverse(node,val):
            if not node:
                return 
            if not node.left and not node.right:
                ans.append((val*10)+node.val)
                return 
            val =(val*10) +node.val
            traverse(node.left,val)
            traverse(node.right,val)
        ans  =  []
        traverse(root,0)
        return sum(ans)
        
