import sys; input = lambda : sys.stdin.readline().rstrip(); sys.setrecursionlimit(150000)

def DFS(cur, cycle, result):
    visited[cur] = True
    cycle.append(cur)
    if visited[students[cur]]:
        if students[cur] in cycle:
            result += cycle[cycle.index(students[cur]):]
    else:
        DFS(students[cur], cycle, result)
        
print_value = []
for _ in range(int(input())):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    result = []
    
    for cur in range(1, n+1):
        if not visited[cur]:
            cycle = []
            DFS(cur, cycle, result)
    print_value.append(str(n - len(result)))
print("\n".join(print_value))