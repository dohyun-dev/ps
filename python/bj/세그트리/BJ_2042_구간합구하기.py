import sys; input = lambda : sys.stdin.readline().rstrip()

def init(node, start, end): 
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) + init(node * 2 + 1, (start + end) // 2 + 1, end)
        return tree[node]

def prefix_Sum(node, start, end, left, right) :
    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    return prefix_Sum(node * 2, start, (start + end) // 2, left, right) + prefix_Sum(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

def update(node, start, end, index, diff) :
    if index < start or index > end :
        return
    
    tree[node] += diff
    
    if start != end :
        update(node * 2, start, (start + end) // 2, index, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * 10000000
    
init(1, 0, N-1)

for _ in range(M+K) :
    a, b, c = map(int, input().rstrip().split())
    
    if a == 1 :
        b = b-1
        diff = c - arr[b]
        arr[b] = c
        update(1, 0, N-1, b, diff)
    elif a == 2 :                
        print(prefix_Sum(1, 0, N-1 ,b-1, c-1))