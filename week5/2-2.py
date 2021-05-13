
'''
https://programmers.co.kr/learn/courses/30/lessons/42586
'''

import math

def solution(progresses, speeds):
    answer = []

    time = [math.ceil((100-a)/b) for a,b in zip(progresses, speeds)]
    n = len(time)
    idx = 0

    for i in range(idx, n):

        if time[idx] < time[i]:
            answer.append(i-idx)
            idx = i
    answer.append(n-idx)
    
    return answer


solution([93,30,55], [1,30,5])
