# 투포인터

# 1.

def solution(word):
    result = ""
    for i in range(2, len(word)+1):
        for j in range(i):

            if word[j:i] == "".join(reversed(word[j:i])) and len(result) < i - j:
                result = word[j:i]
    return result

print(solution("badad"))