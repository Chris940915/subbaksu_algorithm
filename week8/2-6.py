
# https://www.acmicpc.net/problem/1068

def dfs(x):
    global cnt
    if tree[x].childern == []:
        cnt += 1
    
    for search in tree[x].childern:
        dfs(search)


class Node:
    def __init__(self):
        self.childern = []
    
    def insert(self, node):
        self.childern.append(node)
    
    def remove(self, node):
        self.childern.remove(node)

n = int(input())
parents = list(map(int, input().split()))
dele = int(input())
tree = [Node() for _ in range(n)]
cnt = 0

for idx in range(n):
    if parents[idx] != -1:
        tree[parents[idx]].insert(idx)

if n != 1 and parents[dele] != -1:
    tree[parents[dele]].remove(dele)
    dfs(parents.index(-1))
print(cnt)
