# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    is_balanced = True
    def height(self,root):
        if root is None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        diff = abs(left-right)
        if diff > 1:
           self.is_balanced = False 
        height = 1 + max(left,right)
        return height
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.height(root)
        return self.is_balanced

        