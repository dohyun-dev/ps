def solution(logs:list):
    logs = [log.split() for log in logs]
    digit, alpha = [], []

    for log in logs:
        if log[1].isdigit():
            digit.append(log)
        else:
            alpha.append(log)
    alpha.sort(key=lambda x: (x[1:], x[0]))
    return [" ".join(a) for a in alpha] + [" ".join(d) for d in digit]

print(solution(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
