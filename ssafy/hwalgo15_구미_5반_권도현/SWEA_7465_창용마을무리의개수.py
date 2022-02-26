def find(node, parents):
    if parents[node] == node:    return node
    parents[node] = find(parents[node], parents)
    return parents[node]

def union(a, b, parents):
    p_a = find(a, parents)
    p_b = find(b, parents)
    
    if p_a > p_b:
        parents[p_a] = p_b
    elif p_a < p_b:
        parents[p_b] = p_a

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    parents = [i for i in range(N+1)]
    result = set()
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b, parents)
    
    for i in range(1, N+1):
        result.add(find(i, parents))
    
    print(f'#{t} {len(result)}')
    
