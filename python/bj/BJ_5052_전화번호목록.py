import sys; input = lambda : sys.stdin.readline().rstrip()

def solution():
    phone_book = [input() for _ in range(int(input()))]
    hash_map = set(phone_book)
    for p in phone_book:
        for i in range(1, len(p)+1):
            if p != p[:i] and p[:i] in hash_map:
                return "NO"
    return "YES"

for _ in range(int(input())):
    print(solution())