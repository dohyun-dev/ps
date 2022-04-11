def solution(n):
    return ''.join(["수", "박"] * (n // 2) + (["수"] if n % 2 == 1 else [""]))