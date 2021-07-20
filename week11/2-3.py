'''
https://www.acmicpc.net/problem/11404
'''

n = int(input())
m = int(input())
INF = 100000000
matrix = [[INF] * n for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    if matrix[a-1][b-1] > c:
        matrix[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

for i in matrix:
    for j in i:
        if j == INF:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()
