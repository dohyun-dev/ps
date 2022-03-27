from sys import prefix


arr = [1,2,3,2,5]

summary = 0
end = 0
m = 5
cnt = 0

for start in range(5):
    while summary < m and end < m:
        summary += arr[end]
        end += 1
    if summary == m:
       cnt += 1
    summary -= arr[start] 
    

