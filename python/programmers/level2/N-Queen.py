answer = 0

def nqueen(n):
    global answer
    check = [0] * n

    def is_available(l):
        for i in range(l):
            if check[l] == check[i] or abs(check[l] - check[i]) == l - i:
                return False
        return True

    def dfs(l, n):
        global answer
        if l == n:
            answer += 1
        else:
            for i in range(n):
                check[l] = i
                if is_available(l):
                    dfs(l+1, n)
    dfs(0, n)
    return answer

def solution(n):
    nqueen(n)
    return answer

print(solution(4))