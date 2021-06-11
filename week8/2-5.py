def preorder(data):
    print(data.item, end='')

    if data.left != '.':
        preorder(tree[data.left])
    
    if data.right != '.':
        preorder(tree[data.right])

def inorder(data):
    if data.left != '.':
        inorder(tree[data.left])
    print(data.item, end='')

    if data.right != '.':
        inorder(tree[data.right])

def postorder(data):
    if data.left != '.':
        postorder(tree[data.left])
    if data.right != '.':
        postorder(tree[data.right])
    print(data.item, end='')



class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

n = int(input())
tree = {}
for _ in range(n):
    enter = input().split() 
    tree[enter[0]] = Node(item=enter[0],left=enter[1], right=enter[2])

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])