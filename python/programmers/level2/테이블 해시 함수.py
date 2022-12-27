from functools import reduce

def solution(data, col, row_begin, row_end):
    data, answer = sorted(data, key=lambda x: (x[col-1], -x[0])), 0
    for idx, value in enumerate(data[row_begin-1: row_end], row_begin):
        answer ^= reduce(lambda acc, cur: acc + cur % idx, value, 0)
    return answer