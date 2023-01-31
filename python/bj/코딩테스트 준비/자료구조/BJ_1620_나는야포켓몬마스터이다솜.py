N, M = map(int, input().split())
dict_word, dict_num = {}, {}
answer = []

for i in range(1, N+1):
    name = input()
    dict_word[name] = str(i)
    dict_num[i] = name

for _ in range(M):
    o = input()
    if o.isdigit():
        answer.append(dict_num[int(o)])
    else:
        answer.append(dict_word[o])

print("\n".join(answer))