# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def height(root_one:Optional[TreeNode],root_two:Optional[TreeNode]):
            if not root_one and not root_two:
                return True
            if not root_one or not root_two:
                return False 
            if root_one.val != root_two.val:
                return False
            return height(root_one.left,root_two.left) and height(root_one.right,root_two.right)

        
        return height(p,q)
        
