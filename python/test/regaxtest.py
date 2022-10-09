import re

def solution(k:int, dic:list, chat:str) -> str:
    result = ""
    for word in chat.split():
        if word in dic:
            result += "#" * len(word) + " "
        else:
            regax_str = re.sub("[.]", '[a-z]{{1,{0}}}'.format(k), word)
            for check in dic:
                if re.fullmatch(regax_str, check):
                    result += "#" * len(check) + " "
                    break
            else:
                result += word + " "
    return result