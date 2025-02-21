from collections import defaultdict

def solution(clothes):
    answer = 1
    cloths = defaultdict(list)
    
    for kind, type in clothes:
        cloths[type].append(kind)
        
    for key, value in cloths.items():
        answer *= (len(value) +1)
    return answer -1