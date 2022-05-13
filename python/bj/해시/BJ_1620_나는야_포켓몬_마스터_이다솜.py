N, M = map(int, input().split())
pocketmon_dict_word = {}
pocketmon_num = ['']
for i in range(1, N+1):
    s = input()
    pocketmon_num.push(s)
    pocketmon_dict_word[s] = str(i)

for _ in range(M):
    s = input()
    if s.isdigit():
        print(pocketmon_num[int(s)])
    else:
        print(pocketmon_dict_word[s])