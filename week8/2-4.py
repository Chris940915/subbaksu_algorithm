from collections import deque

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.right = right
        self. left = left
    
class Solution:
    def levelOrder(self, root : TreeNode):
        if not root:
            return []
        res = []
        q = deque([root])

        while q:
            n = len(q)
            temp = []

            for _ in range(n):
                node = q.popleft()
                temp.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            res.append(temp)
        return res