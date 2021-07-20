import sys

INF = sys.maxsize

def dijkstra(start, goal, n, graph):
    distance = [INF] * n
    distance[start] = 0
    visit = [False] * n

    while True:
        k = -1
        m = INF

        for i in range(n):
            if m > distance[i] and not visit[i]:
                m = distance[i]
                k = i
        if m == INF:
            break

        visit[k] = True

        for i in range(n):
            if visit[i]:
                continue
            via = distance[k] + graph[k][i]
            if via < distance[i]:
                distance[i] = via
    return distance[goal]


n, e = map(int, input().split())
matrix = [[INF]*n for _ in range(n)]
for _ in range(e):
    a, b, c = map(int, input().split())
    matrix[a-1][b-1] = c
    matrix[b-1][a-1] = c

mid_1, mid_2 = map(int, input().split())
