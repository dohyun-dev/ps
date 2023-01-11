N, K = map(int, input().split())
print(len([1 for i in range(N+1) for j in range(60) for k in range(60)
           if str(K) in ''.join([str(i) if i >= 10 else '0' + str(i),
                         str(j) if j >= 10 else '0' + str(j),
                         str(k) if k >= 10 else '0' + str(k)])]))