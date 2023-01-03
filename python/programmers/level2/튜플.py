def solution(s):
    result = set()
    answer = []
    set_list = [set(map(int, t.replace("{", "").replace("}", "").split(","))) for t in s.split("},{")]
    set_list.sort(key=lambda x: len(x))
    for s in set_list:
        answer += s - result
        result = result | s
    return answer