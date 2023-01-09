from itertools import product

def calc(p, gates, airlines):
    answer = set()
    for date, gate in enumerate(gates, 1):
        copy_airlines = list(airlines)
        for i, value in enumerate(gate):
            if copy_airlines[p[i]] < value:
                break
            copy_airlines[p[i]] -= value
        else:
            answer.add(date)
    return answer


def solution(gates, airlines):
    answer = set()
    for p in product(range(0, 3), repeat=len(gates[0])):
        return_value = calc(p, gates, airlines)
        answer = answer | return_value
    return list(answer) if answer else [-1]