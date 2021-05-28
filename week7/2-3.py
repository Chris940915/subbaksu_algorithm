


n = int(input())
numbers = list(map(int, input().split()))
res = [-1]*n
stack = []

for i in range(n):

    while stack and numbers[stack[-1]] < numbers[i]:
        temp = stack.pop()
        res[temp] = numbers[i]
    stack.append(i)
print(*res)