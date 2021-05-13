'''
https://www.acmicpc.net/problem/2493
'''


n = int(input())
tower = list(map(int, input().split()))
stack = []
res = [0]*n

for i in range(n-1, -1, -1):
    while stack and tower[stack[-1]] < tower[i]:
        tmp = stack.pop()
        res[tmp] = i+1
    stack.append(i)
print(*res)