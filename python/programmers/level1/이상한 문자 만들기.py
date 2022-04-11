def solution(s):
    return " ".join("".join(c.upper() if idx % 2 == 0 else c.lower() for idx, c in enumerate(x)) for x in s.split(" "))