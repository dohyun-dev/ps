import sys; input = lambda : sys.stdin.readline().rstrip()

def DFS(node, visited, nodes, first, list):
    if nodes[node] in not_cycle:
        return False
    
    visited[node] = True
    list.add(node)
    if visited[nodes[node]]:
        if nodes[node] == first:
            return True
    else:
        return DFS(nodes[node], visited, nodes, first, list)
    return False
    
result = []
for _ in range(int(input())):
    N = int(input())
    nodes = [0] + list(map(int, input().split()))
    visited = [False] * (N + 1)
    is_cycle, not_cycle = set(), set()
    answer = N
    for i in range(1, N+1):
        temp = set()
        if not visited[i]:
            if DFS(i, visited, nodes, i, temp):    
                is_cycle |= temp
            else:
                not_cycle.add(i)
    result.append(str(len(not_cycle)))
print("\n".join(result))