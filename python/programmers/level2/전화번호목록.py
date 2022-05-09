def solution(phone_book):
    hash_map = set(phone_book)
    for p in phone_book:
        for i in range(1, len(p)+1):
            if p != p[:i] and p[:i] in hash_map:
                return False
    return True