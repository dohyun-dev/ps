from collections import deque

def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)

    a, b, answer = 0, 0, 0
    while a < len(A):
        if A[a] < B[b]:
            answer += 1
            a, b = a + 1, b + 1
        elif A[a] >= B[b]:
            a += 1
    return answer

print(solution([5, 1, 3, 7], [2, 2, 6, 8]))