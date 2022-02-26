import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque; 

result = []
for t in range(int(input())):
    p, n = input(), int(input())
    q = deque(input()[1:-1].split(","))
    flag = 0;
    
    for c in p:
        if c == "R":
            flag = (flag + 1) % 2
        else:
            if q and q[0] != '': 
                if flag == 0:   q.popleft()
                else:   q.pop()
            else: 
                result.append("error")
                break
    else:
        if(flag == 1): q.reverse()
        result.append("[" + ",".join(map(str, q)) + "]")
        
print("\n".join(map(str, result)))