from collections import deque

n, m, v = map(int, input().split())
matrix = [[0]*(n+1) for _ in range(n+1)]

def dfs(start, result):
    result += [start]

    for search in range(1, n+1):
        if matrix[start][search] and search not in result:
            dfs(search, result)
    return result

def bfs(start):
    q = deque()
    q.append(start)
    result = [start]

    while q:
        x = q.popleft()

        for search in range(1, n+1):
            if matrix[x][search] and search not in result:
                result.append(search)
                q.append(search)
    return result

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1