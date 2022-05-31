def mul(a, b, c):
    if b == 1:
        return a % c
    
    tmp = mul(a, b // 2, c)
    
    if b % 2:
        return tmp * tmp * a % c
    else:
        return tmp * tmp % c
    
a, b, c = map(int, input().split())
print(mul(a, b, c))