from collections import defaultdict

# 시간계산 => 분 단위로 
def calc_clock(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute

# 요금을 계산한다
def calc_fee(calc_time_dict, fees):
    result = {}
    default_time, default_fee, p_time, p_fee = fees
    
    for num, total in calc_time_dict.items():
        temp_fee = default_fee
        if total > default_time:
            total -= default_time
            if total % p_time == 0:
                temp_fee += total // p_time * p_fee
            else:
                temp_fee += (total // p_time + 1) * p_fee
        result[num] = temp_fee
    return result

def solution(fees, records):
    calc_time = defaultdict(int)
    car = {}
    for r in records:
        time, num, order = r.split()
        
        if order == "IN":
            car[num] = calc_clock(time)
        else:
            calc_time[num] += calc_clock(time) - car[num]
            del car[num]
    
    for num, time in car.items():
        calc_time[num] += calc_clock("23:59") - time
        
    calc_fee_dict = calc_fee(calc_time, fees)
    
    return [v for k, v in sorted(calc_fee_dict.items(), key=lambda x: x[0])]