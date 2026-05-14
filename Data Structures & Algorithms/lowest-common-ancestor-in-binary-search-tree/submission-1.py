# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = root
        temp = root
        stop = False
        while not stop:
            ancestor = temp

            if p.val < temp.val and q.val < temp.val:
                temp = temp.left
            elif p.val > temp.val and q.val > temp.val:
                temp = temp.right
            else:
                stop = True
        
        return ancestor
        

            



