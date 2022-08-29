from collections import deque

def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    CACHE_HIT, CACHE_MISS = 1, 5
    exec_time = 0
    for city in cities:
        city = city.lower()
        if not city in cache:
            cache.append(city)
            exec_time += CACHE_MISS
        else:
            if cache:
                cache.remove(city)
                cache.append(city)
                exec_time += CACHE_HIT
    return exec_time

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
