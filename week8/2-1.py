class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preoderTraversal(self, root : TreeNode) -> list[int]:
        stack, res = [root], []

        while stack:
            node = stack.pop()
            
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
        