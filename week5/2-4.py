
'''
https://www.acmicpc.net/problem/2075
'''

import heapq

n = int(input())
q = []

enters = list(map(int, input().split()))
for enter in enters:
    heapq.heappush(q, enter)

for idx in range(1, n):
    enters = list(map(int, input().split()))

    for enter in enters:
        if q[0] < enter:
            heapq.heappop(q)
            heapq.heappush(q, enter)
print(q[0])