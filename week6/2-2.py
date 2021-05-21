

'''

https://programmers.co.kr/learn/courses/30/lessons/42587

내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다.

내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.
'''

from collections import deque

def solution(priorities, location):
    answer = 0

    priorities = deque([[i,v] for i,v in enumerate(priorities)])
    while True:
        # J를 pop 
        temp = priorities.popleft()
        # 하나라도 J 보다 중요
        if any(temp[1] < q[1] for q in priorities):
            priorities.append(temp)
        else:
            answer += 1

            if temp[0] == location:
                return answer

    return answer