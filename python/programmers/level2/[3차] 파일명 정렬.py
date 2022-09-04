def solution(files):
    result = []
    for f in files:
        temp_arr = []
        temp = ""
        for c in f:
            if len(temp_arr) == 0:
                if not c.isdigit():
                    temp += c
                else:
                    temp_arr.append(temp)
                    temp = c
            elif len(temp_arr) == 1:
                if c.isdigit():
                    temp += c
                else:
                    temp_arr.append(temp)
                    temp = c
            else:
                temp += c
        temp_arr.append(temp)
        result.append(temp_arr)
    return ["".join(c) for c in sorted(result, key=lambda x: (x[0].lower(), int(x[1])))]
