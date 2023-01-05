def check_grade(customer):
    period, payment = customer
    if period < 24:
        return False
    elif period < 60:
        if sum(payment) < 900000:
            return False
    else:
        if sum(payment) < 600000:
            return False
    return True


def solution(periods, payments, estimates):
    answer = [0, 0]
    for i in range(len(periods)):
        cur_month = check_grade((periods[i], payments[i]))
        next_month = check_grade((periods[i] + 1, payments[i][1:] + [estimates[i]]))

        if not cur_month and next_month:
            answer[0] += 1

        if cur_month and not next_month:
            answer[1] += 1

    return answer

print(solution(
    [24, 59, 59, 60],
    [
        [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
        [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
        [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
        [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]
    ],
    [350000, 50000, 40000, 50000])
)