# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        result = []
        def dfs(root, subRoot):
            if root == None:
                return False
            if check(root, subRoot):
                return True

            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        def check(sub_root, subRoot):
            if not sub_root and not subRoot:
                return True
            if not sub_root or not subRoot:
                return False
            if sub_root.val != subRoot.val:
                return False
            return check(sub_root.left, subRoot.left) and  check(sub_root.right, subRoot.right)
        
        return dfs(root, subRoot)
        
