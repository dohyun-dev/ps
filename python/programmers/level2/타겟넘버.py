temp = []
answer = 0

def calc(numbers):
    result = 0
    for i in range(len(numbers)):
        if temp[i] == "+":
            result += numbers[i]
        else:
            result -= numbers[i]
    return result

def dfs(l, N, numbers, target):
    global answer
    if l == N:
        if target == calc(numbers):
            answer += 1
        return
    
    temp.append("+")
    dfs(l+1, N, numbers, target)
    temp.pop()
    
    temp.append("-")
    dfs(l+1, N, numbers, target)
    temp.pop()

def solution(numbers, target):
    dfs(0, len(numbers), numbers, target)
    return answer