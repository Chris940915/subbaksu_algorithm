
'''
https://www.acmicpc.net/problem/1238
'''

import sys
import heapq

INF = sys.maxsize

def dijsktra(n, v, graph):
    distance = [INF] * n
    distance[v] = 0
    q = []
    heapq.heappush(q, [0, v])

    while q:
        cost, pos = heapq.heappop(q)
        for p, c in graph[pos]:
            c += cost

            if c < distance[p]:
                distance[p] = c
                heapq.heappush(q, [c, p])
    return distance


n, m, x = map(int, input().split())
matrix = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a-1].append([b-1, c])
result = [0] * n

for idx in range(n):
    temp = dijsktra(n, idx, matrix)

    # 해당 마을 일때, 해당 마을에서 다른 마을의 거리 계산한 값을 더해준다.
    if idx == x-1:
        for i, v in enumerate(temp):
            result[i] += v
    else:
        result[idx] += temp[x-1]
print(max(result))
