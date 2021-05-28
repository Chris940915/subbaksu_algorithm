
import heapq

n = int(input())

max_heap = list()
min_heap = list()

result = list()

for _ in range(n):
    k = int(input())

    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, (-k, k))
    else:
        heapq.heappush(min_heap, (k, k))

    '''
    min_heap 에 요소가 존재하는지 확인, 가운뎃 값을 max_heap 에 첫번째 놓는다.

    '''
    if min_heap and max_heap[0][1] > min_heap[0][1]: 
        min_v = heapq.heappop(min_heap)[1]
        max_v = heapq.heappop(max_heap)[1]

        heapq.heappush(max_heap, (-min_v, min_v))
        heapq.heappush(min_heap, (max_v, max_v))

    result.append(max_heap[0][1])

for i in result:
    print(i)