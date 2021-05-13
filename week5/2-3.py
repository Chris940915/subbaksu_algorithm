

'''
https://www.acmicpc.net/problem/1927
'''

import heapq
import sys

n = int(input())
heap = list()
results = list()

for _ in range(n):
    enter = int(input())

    # 배열에서 가장 작은 값을 출력 및 제거.
    if enter == 0:
        if len(heap) == 0:
            results.append(0)
        else:
            results.append(heapq.heappop(heap))
    # 배열에 값 추가. 
    else:
        heapq.heappush(heap, enter)

for result in results:
    print(result)