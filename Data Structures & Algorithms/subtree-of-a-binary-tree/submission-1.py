# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    res = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            if not root and not subRoot:
                return True 
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return isSame(root.left,subRoot.left) and isSame(root.right,subRoot.right)
        
        if root is None and subRoot != None:
            return False
        self.res = isSame(root,subRoot)
        if self.res == True:
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)



