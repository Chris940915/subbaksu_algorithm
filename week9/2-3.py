"""
https://www.acmicpc.net/problem/2606
"""

from collections import deque

def bfs():
    q = deque()
    q.append(0)
    visit.append(0)

    while q:
        x = q.popleft()

        for target in range(1, n):
            if matrix[x][target] and target not in visit:
                q.append(target)
                visit.append(target)
    return len(visit)-1

n = int(input())
m = int(input())
matrix = [[0]*n for _ in range(n)]
visit = []

for _ in range(m):
    a, b = map(int, input().split())

    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1

res = bfs()
print(res)