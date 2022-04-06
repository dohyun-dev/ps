import sys; input = lambda : sys.stdin.readline().rstrip()

arr = [1,2,3,4]
mul = 1
for i in arr:   mul *= i
out = [mul // i for i in arr]