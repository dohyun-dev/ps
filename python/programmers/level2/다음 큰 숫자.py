def convert_binary_one_count(number):
    return len(list(filter(lambda x: x == '1', bin(number))))

def solution(n):
    one_count = convert_binary_one_count(n)
    for i in range(n+1, 1000001):
        if convert_binary_one_count(i) == one_count:
            return i