"""
https://programmers.co.kr/learn/courses/30/lessons/43162
"""

from collections import deque

def solution(n, computers):
    answer = 0

    def bfs(s):
        queue = deque()
        queue.append(s)
        visit[s] = 0
        cnt = 1
        while queue:
            x = queue.popleft()

            for search in range(len(matrix[x])):
                if matrix[x][search] == 1 and visit[search] == -1:
                    queue.append(search)
                    visit[search] = 0
                    cnt += 1
        return cnt

    matrix = [[0] * n for _ in range(n)]
    visit = [-1] * n
    node = set()

    for c_i, computer in enumerate(computers):
        for c_j, c in enumerate(computer):
            if c_i == c_j:
                matrix[c_i][c_j] = -1
            elif c == 1:
                node.add(c_i)
                node.add(c_j)
                matrix[c_i][c_j] = 1
                matrix[c_j][c_i] = 1
    sum_cnt = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1 and visit[i] == -1:
                sum_cnt += bfs(i)
                answer += 1
    answer += n - sum_cnt
    return answer

solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])