import sys; input = lambda : sys.stdin.readline().rstrip(); sys.setrecursionlimit(150000)

def DFS(cur, start, check, temp):
    if students[cur] == start:
        return True
    elif not check[students[cur]] or students[cur] in temp:
        return False
    else:
        temp.add(students[cur])
        return DFS(students[cur], start, check, temp)

result = []
for _ in range(int(input())):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    answer = 0
    check = [True] * (n+1)
    cycle = set()
    for cur in range(1, n+1):
        if cur not in cycle:
            temp = set()
            temp.add(cur)
            if DFS(cur, cur, check, temp):  
                cycle = cycle | temp
                check[cur] = False
    result.append(str(n - len(cycle)))
print("\n".join(result))