from collections import defaultdict

def solution(id_list, report, k):
    report_list = defaultdict(set)
    id_mapper = dict()
    result = [0] * len(id_list)
    
    for idx, id in enumerate(id_list):
        id_mapper[id] = idx
        
    for r in report:
        a, b = r.split()
        a, b = id_mapper[a], id_mapper[b]
        report_list[b].add(a)
    
    for key, value in report_list.items():
        if len(value) >= k:
            for i in value:
                result[i] += 1
    return result