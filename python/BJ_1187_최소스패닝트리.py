import sys; input = lambda : sys.stdin.readline().rstrip()

def find(node, parents):
    if parents[node] == node:
        return node
    parents[node] = find(parents[node], parents)
    return parents[node]

def union(a, b, parents):
    p_a = find(a, parents)
    p_b = find(b, parents)
    
    if p_a == p_b:
        return False
    if p_a > p_b:
        parents[p_a] = p_b
    else:
        parents[p_b] = p_a
    return True


V, E = map(int, input().split())
parents = [i for i in range(V+1)]
edges = sorted([tuple(map(int, input().split())) for _ in range(E)], key=lambda x: x[2])
result, cnt = 0, 0

for edge in edges:
    v1, v2, c = edge
    if union(v1, v2, parents):
        result += c
        cnt += 1
    if cnt == V-1:  break
print(result)