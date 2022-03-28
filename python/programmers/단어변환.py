def permutation():
    
    
    answer = 0
    visited = [False] * len(begin)
    DFS(begin, target, words)
    
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))