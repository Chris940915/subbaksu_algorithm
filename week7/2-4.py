import heapq

def solution(operations):
    answer = [0, 0]

    n = len(operations)
    max_heap = []
    min_heap = []

    for i, v in enumerate(operations):
        enter = v.split()

        if enter[0] == 'I':
            heapq.heappush(max_heap, (-int(enter[1]),int(enter[1])))
            heapq.heappush(min_heap, int(enter[1]))            

        elif enter[0] == 'D':
            if len(min_heap) == 0:
                continue

            if int(enter[1]) > 0:
                tmp = heapq.heappop(max_heap)[1]
                min_heap.remove(tmp)
            else:
                tmp = heapq.heappop(min_heap)
                max_heap.remove((-tmp, tmp))

    if max_heap:
        answer[0] = max_heap[0][1]
    if min_heap:
        answer[1] = min_heap[0]
    print(answer)
    return answer