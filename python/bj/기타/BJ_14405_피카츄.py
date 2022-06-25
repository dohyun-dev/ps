import re

s = input()
find = re.fullmatch("(pi|ka|chu)+", s)
print("YES" if find else "NO")
