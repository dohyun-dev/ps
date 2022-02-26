s = ["N"] + list(*input().split())
cnt = 0

for i in range(1, len(s)):
    if s[i] == "Y":
        for j in range(i, len(s), i):
            if s[j] == "Y":
                s[j] = "N"
            else:
                s[j] = "Y"
        cnt += 1
print(cnt)