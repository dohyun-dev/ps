from collections import defaultdict
graph = defaultdict(list)

course = set()
answer = 10000000
def dfs(cur, end, c, intensity=0):
    global answer, course
    if cur == end:
        if answer > intensity:
            answer = intensity
            course = c
    else:
        for next, cost in graph[cur]:
            if not in c:
                visited[next] = True
                c.add(next)
                dfs(next, end, c, max(intensity, cost))
                c.remove(next)
                visited[next] = False
            
def make_graph(paths):
    for p in paths:
        a, b, c = p
        graph[a].append((b, c))

def solution(n, paths, gates, summits):
    global answer, visited
    make_graph(paths)
    result = [10000000, 0]
    for start in gates:
        for summit in summits:
            answer = 10000000
            
            visited[start] = True
            dfs(start, summit, set([start]))
            
            visited[start] = False
            dfs(summit, start, set())
            
            if result[0] > max(answer, summit):
                result = [answer, summit]
    return [result[1], result[0]]
    

solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])
