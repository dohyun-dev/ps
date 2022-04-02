import re;  p = re.compile('(100+1+|01)+')
print("\n".join(["YES" if p.fullmatch(input()) else "NO" for _ in range(int(input()))]))
