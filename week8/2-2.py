class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def inorderTraversal(self, root):
        res = []
        self.recursive(root, res)
        return res
    
    def recursive(self, root, res):
        if root:
            self.recursive(root.left, res)
            res.append(root.val)
            self.recursive(root.right, res)