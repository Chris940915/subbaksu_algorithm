

'''
https://www.acmicpc.net/problem/2504

'''

def check(enter):
    stack = list()
    n = len(enter)

    for i in range(n):
        if enter[i] == '(' or enter[i] == '[':
            stack.append(enter[i])
        
        elif enter[i] == ')' and stack:
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(enter[i])
        
        elif enter[i] == ']' and stack:
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(enter[i])
        else:
            stack.append(enter[i])
    if stack:
        return False
    else:
        return True


def solution(enter):
    n = len(enter)
    stack = []

    for i in range(n):
        s = enter[i]

        if s == '(' or s == '[':
            stack.append(s)
        elif s == ']':
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                tmp = 0
                while stack[-1] != '[':
                    tmp += stack.pop()
                stack[-1] = tmp*3
        elif s == ')':
            if stack[-1] == '(':
                stack[-1] == 2
            else:
                tmp = 0
                while stack[-1] != '(':
                    tmp += stack.pop()
                stack[-1] = tmp*2
    return sum(stack)

enter = list(input())

if check(enter):
    solution(enter)
else:
    print(0)