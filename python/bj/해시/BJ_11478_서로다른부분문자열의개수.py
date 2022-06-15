data = input()
check = set()

for i in range(len(data)):
    for j in range(i+1, len(data)+1):
        check.add(data[i:j])

print(len(check))