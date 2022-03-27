def find(node, parent):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node], parent)
    return parent[node]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    
    if a != b:
        if a < b:
            parent[b] = a
        elif a > b:
            parent[a] = b
    
def solution(n, computers):
    parent = [i for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                union(i, j, parent)

    return len(set(find(i, parent) for i in range(n)))

n = 5
computers = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1], [1, 0, 0, 0, 1]]

print(solution(n, computers))