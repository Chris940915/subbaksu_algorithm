'''
https://www.acmicpc.net/problem/2667
'''

from collections import  deque

n = int(input())
dx, dy = [0,0,1,-1], [1,-1,0,0]


def bfs(a, b):
    matrix[a][b] = 0
    count = 1
    q = deque()
    q.append([a, b])

    while q:
        x, y = q.popleft()
        for idx in range(4):
            tx, ty = x+dx[idx], y+dy[idx]
            if 0<=tx<n and 0<=ty<n:
                if matrix[tx][ty] == 1:
                    matrix[tx][ty] = 0
                    q.append([tx, ty])
                    count += 1
    return count
matrix = []
result = []
for _ in range(n):
    line = list(map(int, input()))
    matrix.append(line)

count = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            result.append(bfs(i, j))
            count += 1
result.sort()
print(count)
for r in result:
    print(r)
