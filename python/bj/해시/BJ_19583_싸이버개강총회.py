import sys; input = lambda : sys.stdin.readline().rstrip()

start_time, end_time, end_streaming = [x[0] * 60 + x[1] for x in [tuple(map(int, s.split(":"))) for s in input().split()]]
attend_list = set()
result = set()

while True:
    try:
        time, user_id = input().split()
        hour, minute = map(int, time.split(":"))
        time = hour * 60 + minute
        if time <= start_time:
            attend_list.add(user_id)
        if end_time <= time <= end_streaming and user_id in attend_list:
            result.add(user_id)
    except e:
        break
print(len(result))