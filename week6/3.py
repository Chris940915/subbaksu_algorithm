'''
https://programmers.co.kr/learn/courses/30/lessons/67258

'''

import heapq
from collections import defaultdict

def solution(gems):
    answer = []
    n_ = len(gems)
    n = len(list(set(gems)))
    cart = defaultdict(int)

    start, end = 0, 0
    while True:

        if len(cart) == n:
            heapq.heappush(answer, [end-start, start, end])
        
        if len(cart) >= n:
            cart[gems[start]] -= 1
            if cart[gems[start]] == 0:
                del cart[gems[start]]
            start += 1
        elif end == n_:
            break
        elif len(cart) < n:
            cart[gems[end]] += 1
            end += 1

    return [answer[0][1]+1, answer[0][2]]
