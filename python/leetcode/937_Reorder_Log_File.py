import re
logs = ["dig1 8 1 5 1", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
s = []
digit = []
for log in logs:
    if re.fullmatch("\d+", log.split()[1]) is not None:
        digit.append(log)
    else:
        s.append(log)
s.sort(key=lambda x: (x.split()[1:], x.split()[0]))
print(s + digit)