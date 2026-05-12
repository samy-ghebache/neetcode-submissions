# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True
        def dfs(root: Optional[TreeNode]):
            if root == None:
                return 0
            
            left = (1 + dfs(root.left) if root.left else 0)
            right = (1 + dfs(root.right) if root.right else 0)
            nonlocal result
            if abs(left - right) > 1 :
                result = False
            
            return max(left, right)
        
        dfs(root)

        return result
            
            
