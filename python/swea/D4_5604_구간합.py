f = {}
result = []

def V(num):
    v = 1
    while num >= 10:
        v *= 10
        num //= 10;
    return v
        
def F(num):
    if num in f:
        return f[num]
    if num < 10:
        return f[num]
    
    v_num = V(num)
    f_num = F(num - 1 - num % v_num)
    g_num = (num // v_num) * (num % v_num + 1) + F(num % v_num)
    result_num = f_num + g_num
    
    f[num] = result_num
    
    return result_num

for t in range(1, int(input()) + 1):
    start, end = map(int, input().split())
    
    sum_num = 0
    for i in range(10):
        sum_num += i
        f[i] = sum_num
    
    if start > 0:
        answer = F(end) - F(start-1)
    else:
        answer = F(end) - F(start)
    
    result.append(f'#{t} {answer}')
print("\n".join(result))