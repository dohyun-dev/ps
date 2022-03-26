import sys; input = lambda : sys.stdin.readline().rstrip()

a, b = map(int, input().split())
result = sorted(set(input().split()) - set(input().split()), key= lambda x: int(x))
print(len(result))
if result:  print(" ".join(result))