class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root : TreeNode):
        stack, res = [root], []

        while stack:
            node = stack.pop()
            if node:
                res.append(val)
                stack.append(node.right)
                stack.append(node.left)
        return res[::-1]