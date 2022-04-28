def solution(record):
    nicknames = {}
    result = []
    for r in record:
        temp = r.split()
        if temp[0] == "Enter" or temp[0] == "Change":
            order, id, name = r.split()
            nicknames[id] = name
    for r in record:
        temp = r.split()
        if temp[0] == "Enter":
            order, id, name = temp
            result.append(f'{nicknames[id]}님이 들어왔습니다.')
        elif temp[0] == "Leave":
            order, id = temp
            result.append(f'{nicknames[id]}님이 나갔습니다.') 
    return result