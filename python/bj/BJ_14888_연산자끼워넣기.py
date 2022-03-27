import sys; input = lambda : sys.stdin.readline().rstrip()

temp = []

def calc():
    tempNum = num[:]
    for i in range(N-1):
        if temp[i] == 0:
            tempNum[i+1] = tempNum[i] + tempNum[i+1]
        elif temp[i] == 1:
            tempNum[i+1] = tempNum[i] - tempNum[i+1]
        elif temp[i] == 2:
            tempNum[i+1] = tempNum[i] * tempNum[i+1]
        else:
            if tempNum[i] < 0:
                tempNum[i+1] = -(-tempNum[i] // tempNum[i+1])
            else:
                tempNum[i+1] = tempNum[i] // tempNum[i+1]
            
    return tempNum[N-1]
        
def DFS(l=0):
    if l == N-1:
        result.append(calc())
    else:
        for i in range(4):
            if operator[i] != 0:
                operator[i] -= 1
                temp.append(i)
                DFS(l+1)
                operator[i] += 1
                temp.pop()

N = int(input())    # 수의 개수
num = list(map(int, input().split()))
operator = list(map(int, input().split()))
result = []
DFS()
print(max(result))
print(min(result))
