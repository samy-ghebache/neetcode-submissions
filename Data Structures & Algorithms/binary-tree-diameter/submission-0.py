# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:

    def helper(self, root):
        if root == None:
            return 0
        return 1 + max(self.helper(root.left), self.helper(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        diameter = 0
        while q :
            node = q.popleft()
            diameter = max(diameter, self.helper(node.left) + self.helper(node.right))
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return diameter
            
        

