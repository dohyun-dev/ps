
def dfs(l, wish_word, total):
    global answer
    if wish_word == "":
        answer = min(answer, total)
        return

    if l == N:
        return
    dfs(l+1, wish_word, total)
    price, name = int(books[l][0]), books[l][1]
    tmp = wish_word
    for i in name:
        if i in tmp:
            tmp = wish_word.replace(i, "", 1)
    dfs(l+1, tmp, total+price)

wish_word, N = input(), int(input())
books = [input().split() for _ in range(N)]
answer = float("inf")
dfs(0, wish_word, 0)
print(-1 if float("inf") == answer else answer)