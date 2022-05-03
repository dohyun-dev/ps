import heapq

def solution(prices):
    result = [i for i in range(len(prices) - 1, -1, -1)]
    q = []
    
    for idx, price in enumerate(prices):
        while q and -q[0][0] > price:
            p, i = heapq.heappop(q)
            result[i] = idx - i
        heapq.heappush(q, (-price, idx))
        
    return result

solution([1, 2, 3, 2, 3])