def pow(num, n):
    if n == 0:
        return 1
    
    half = pow(num, n//2)
    
    if n % 2 == 0:
        return ((half % 1234567891) * (half % 1234567891)) % 1234567891
    else:
        return (((half * num) % 1234567891) * (half % 1234567891)) % 1234567891

result = []
for t in range(1, int(input())+1):
    n, r = map(int, input().split())
    fact = [0 for i in range(n+1)]
    fact[0] = 1
    for i in range(1, n+1): fact[i] = (fact[i-1] * i) % 1234567891
    
    top = (fact[n]) % 1234567891
    bot = ((fact[n-r] % 1234567891) * fact[r] % 1234567891) % 1234567891
    
    result.append(f'#{t} {(top * pow(bot, 1234567889) % 1234567891)}')
print("\n".join(result))