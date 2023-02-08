def pre(node):
    result1 = pre(graph[node][0]) if graph[node][0] != "." else ""
    result2 = pre(graph[node][1]) if graph[node][1] != "." else ""
    return node + result1 + result2

def mid(node):
    result1 = mid(graph[node][0]) if graph[node][0] != "." else ""
    result2 = mid(graph[node][1]) if graph[node][1] != "." else ""
    return result1 + node + result2

def post(node):
    result1 = post(graph[node][0]) if graph[node][0] != "." else ""
    result2 = post(graph[node][1]) if graph[node][1] != "." else ""
    return result1 + result2 + node

N = int(input())
visited = {}
graph = {}

for _ in range(N):
    a, b, c = input().split()
    visited[a] = False
    graph[a] = [b, c]

print(pre("A"))
print(mid("A"))
print(post("A"))
