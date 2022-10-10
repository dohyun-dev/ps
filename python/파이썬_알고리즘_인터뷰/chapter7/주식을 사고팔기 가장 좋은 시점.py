import sys


def solution(arr:list) -> list:
    profit = -sys.maxsize
    low_price = sys.maxsize
    for price in arr:
        low_price = min(price, low_price)
        profit = max(profit, price - low_price)
    return profit
print(solution([7,1,5,3,6,4]))