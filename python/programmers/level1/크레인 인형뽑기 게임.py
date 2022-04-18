def solution(board, moves):
    stack = []
    answer = 0
    for m in moves:
        m -= 1
        for i in range(len(board)):
            if board[i][m] != 0:
                cur = board[i][m]
                if stack and stack[-1] == cur:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(cur)
                board[i][m] = 0
                break
    return answer