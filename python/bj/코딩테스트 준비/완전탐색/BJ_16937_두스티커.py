from itertools import combinations

def attach(l, c, sticker):
    flag, tmp = True, []
    for i in range(sticker[0]):
        for j in range(sticker[1]):
            if (l + i >= H) or (c + j >= W):
                flag = False
                break
            tmp.append((l+i, c+j))
            board[l+i][c+j] = True
        if not flag:
            for x, y in tmp:
                board[x][y] = False
            return []
    return tmp

def DFS(l, combi):
    global answer
    if l == 2:
        answer = max(answer, sum(1 for j in range(W) for i in range(H) if board[i][j]))
        return

    for s in range(2):
        for i in range(H):
            for j in range(W):
                tmp = attach(i, j, stickers[l][s])
                if len(tmp):
                    DFS(l + 1, combi)
                    for x, y in tmp:
                        board[x][y] = False

H, W = map(int, input().split())
N = int(input())
stickers = [tuple(map(int, input().split())) for _ in range(N)]
answer = 0

for combi in combinations(stickers, 2):
    r1, c1 = combi[0]
    r2, c2 = combi[1]

    if ((r1 + r2 <= H) and max(c1, c2) <= W) or (max(r1, r2) <= H and c1 + c2 <= W):
        answer = max(answer, r1 * c1 + r2 * c2)
    if ((r1 + c2 <= H) and max(c1, r2) <= W) or (max(r1, c2) <= H and c1 + r2 <= W):
        answer = max(answer, r1 * c1 + r2 * c2)
    if ((c1 + r2 <= H) and max(r1, c2) <= W) or (max(c1, r2) <= H and r1 + c2 <= W):
        answer = max(answer, r1 * c1 + r2 * c2)
    if ((c1 + c2 <= H) and max(r1, r2) <= W) or (max(c1, c2) <= H and r1 + r2 <= W):
        answer = max(answer, r1 * c1 + r2 * c2)

print(answer)