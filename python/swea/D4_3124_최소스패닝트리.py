from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def find(node, parent):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node], parent)
    return parent[node]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    
    if a == b:
        return False
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        return True

for t in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    parent = [i for i in range(a+1)]
    edges = deque(sorted([tuple(map(int, input().split())) for _ in range(b)], key=lambda x : x[2]))
    answer = 0
    
    for i in range(b):
        n1, n2, cost = edges[i]
        if union(n1, n2, parent):
            answer += cost
    print(f'#{t} {answer}')
            
    