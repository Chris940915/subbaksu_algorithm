
'''
https://www.acmicpc.net/problem/10799

'''


enter = list(input())
n = len(enter)

stack = []
result = 0

for idx in range(n):
    if enter[idx] == '(':
        stack.append('(')
    else:
        if enter[idx] == ')':
            stack.pop()
            result += 1
        elif enter[idx-1] == '(':
            stack.pop()
            result += len(stack)
print(result)