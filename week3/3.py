def solution(board, moves):
    answer = 0

    stack = []
    n = len(board)

    for move in moves:

        for idx in range(n):
            val = board[idx][move-1]
            if val != 0:
                # 아무것도 없거나 직전이 같지 않으면
                if not stack or stack[-1] != val:
                    stack.append(val)
                
                elif stack[-1] == val:
                    stack.pop()
                    answer += 2
                board[idx][move-1] = 0
                break
    return answer