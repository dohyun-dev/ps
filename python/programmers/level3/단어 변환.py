from collections import deque

def solution(begin, target, words):

    if target not in words:
        return 0

    q = deque([(begin, 0)])

    while q:
        cur, cnt = q.popleft()

        if cur == target:
            return cnt

        for word in words:
            tmp = 0
            for idx, c in enumerate(word):
                if cur[idx] != c:
                   tmp += 1
            if tmp == 1:
                q.append((word, cnt + 1))

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))