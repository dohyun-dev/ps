import re

def solution(phone_number):
    return re.sub("\d", "*", phone_number[:-4]) + phone_number[-4:]