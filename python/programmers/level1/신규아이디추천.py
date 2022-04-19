import re

def solution(new_id):
    answer = new_id.lower()
    answer = re.sub("[^\w\d\-_.]", "", answer)
    answer = re.sub("[.]{2,}", ".", answer)
    answer = answer[1:] if answer and answer[0] == '.' else answer
    answer = answer[:-1] if answer and answer[-1] == '.' else answer
    answer = "a" if not answer else answer
    answer = answer[:15] if len(answer) >= 16 else answer
    answer = answer[:-1] if answer and answer[-1] == '.' else answer
    answer = answer + answer[-1] * (3 - len(answer)) if len(answer) <= 2 else answer
    return answer