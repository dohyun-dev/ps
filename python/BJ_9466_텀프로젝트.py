import sys; input = lambda : sys.stdin.readline().rstrip(); sys.setrecursionlimit(150000)

def DFS(cur, start, cnt = 1):
    global n
    if students[cur] == start:
        n -= cnt
        return True
    if students[cur] not in visited:
        visited.add(students[cur])
        if not DFS(students[cur], start, cnt + 1):
            visited.remove(students[cur])
    return False

for _ in range(int(input())):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    visited = set()
    for i in range(1, n+1):
        if i not in visited:
            visited.add(i)
    print(n)