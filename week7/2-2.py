import heapq

q = []

n, m = map(int, input().split())
path = [[] for _ in range(n)]
indegree = [0]*n
result = []

for _ in range(m):
    a, b = map(int, input().split())
    path[a-1].append(b-1)
    indegree[b-1] += 1

for i in range(n):
    if indegree[i] == 0:
        heapq.heappush(q, i)

while q:
    x = heapq.heappop(q)
    result.append(x)

    for search in path[x]:
        indegree[search] -= 1

        if indegree[search] == 0:
            heapq.heappush(q, search)

for i in result:
    print(i+1, end=' ')