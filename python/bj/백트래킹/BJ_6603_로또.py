import sys; input = lambda : sys.stdin.readline().rstrip()

def combinations(l=0, start=0, result=[]):
    if l == 6:
        print(" ".join(result))
        return
    for i in range(start, K):
        result.append(str(num_arr[i]))
        combinations(l+1, i+1, result)
        result.pop()

while True:
    arr = list(map(int, input().split()))
    
    if arr[0] == 0:
        break
    
    K, num_arr = arr[0], arr[1:]
    combinations()
    print()