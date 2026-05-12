# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root: Optional[TreeNode]):
            if root == None:
                return 0
            
            left = dfs(root.left) if root.left else 0
            right = dfs(root.right) if root.right else 0

            if left < 0 or right < 0 :
                return -1
            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)


        return dfs(root) >= 0
            
            
