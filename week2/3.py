
# https://programmers.co.kr/learn/courses/30/lessons/60057


import sys


def compress(s, step, n):

    compressed_result = ""
    standard = s[0:step]
    
    count = 1
    for idx in range(step, n, step):
        check = s[idx:idx+step]
        # 같을 때,
        if standard == check:
            count += 1
            continue
        else:

            if count > 1:
                compressed_result += str(count) + standard
            else:
                compressed_result += standard
            standard = check
            count = 1
    
    # 마지막 처리
    if count > 1:
        compressed_result += str(count) + standard
    else:
        compressed_result += standard
    return len(compressed_result)


def solution(s):
    answer = sys.maxsize

    n = len(s)

    if n == 1:
        return 1
    
    for i in range(1, n//2+1):
        answer = min(answer, compress(s, i, n))

    return answer